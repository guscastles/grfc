"""
Gives the mains statistics for the Tigers team.
"""
import subprocess
import pandas as pd
from . import scheduler as sc, GRFC_FILE, TOTAL_TIME


def valid_data(data):

    def no_empty_data():
        return filter(lambda dt: dt is not None, data)

    time_stats = pd.DataFrame(list(map(lambda record: record[0], no_empty_data())))
    goalies = pd.DataFrame(list(map(lambda record: record[1], no_empty_data())))
    return time_stats, goalies


def rename_stats_fields(stats, goalies):
    count = stats.loc['count']
    count.name = 'matches played'
    mean = stats.loc['mean']
    mean.name = 'average time played'
    goalies.name = 'turns in goals'
    return pd.DataFrame([count, mean, goalies])


def data_stats(data, goalies=None):
    stats = rename_stats_fields(data.describe().loc[['count', 'mean']], goalies.sum())
    total_time = data.sum()
    total_time.name = 'total time played'
    return stats.append(total_time).fillna(0.0)


def goalies_stats(goalies_list):
    return {player: goalies_list.count(player) for player in goalies_list}


def time_for_players(filename, round_nbr):
    """
    Read the data file and returns tuples with time stats and goalies stats.
    """

    def get_time(player, time_offs):
        return TOTAL_TIME - timeoff if player in goalies_list else TOTAL_TIME - timeoff * time_offs

    def data_is_ok():
        return players_list and goalies_list and timeoff and nbr_of_time_offs

    def time_stats():
        return {player: get_time(player, nbr_of_time_offs[player]) for player in players_list}

    players_list, goalies_list, timeoff, nbr_of_time_offs, _ = sc.match_data(filename, round_nbr)
    if data_is_ok():
        return time_stats(), goalies_stats(goalies_list)
    return None


def run():

    def get_data():
        return [time_for_players(GRFC_FILE, f'Round {round_nbr}') for round_nbr in range(1, 19)]

    with open('report.html', 'w') as report:
        report.write(data_stats(*valid_data(get_data())).to_html())
    subprocess.run(['firefox', 'report.html'])


if __name__ == '__main__':
    run()
