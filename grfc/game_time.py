"""
Gives the mains statistics for the Tigers team.
"""
import pandas as pd
from . import scheduler as sc, GRFC_FILE


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
    goalies.name = 'turns as goalie'
    return pd.DataFrame([count, mean, goalies])


def data_stats(data, goalies=None):
    stats = rename_stats_fields(data.describe().loc[['count', 'mean']], goalies.sum())
    total_time = data.sum()
    total_time.name = 'total time played'
    return stats.append(total_time).fillna(0.0)


if __name__ == '__main__':

    def get_data():
        return [sc.time_for_players(GRFC_FILE, f'Round {round_nbr}') for round_nbr in range(1, 19)]

    print(data_stats(*valid_data(get_data())).to_html())
