"""
Gives the mains statistics for the Tigers team.
"""
from functools import reduce
import pandas as pd
from . import game_data as gd, TOTAL_TIME


def valid_data(data):

    def _no_empty_data():
        return filter(lambda dt: dt is not None, data)

    time_stats = pd.DataFrame(list(map(lambda record: record[0], _no_empty_data())))
    goalies = pd.DataFrame(list(map(lambda record: record[1], _no_empty_data())))
    return time_stats, goalies


def _set_column_name(column, name):
    column.name = name
    return column


def rename_stats_fields(stats, goalies):
    matches_played = _set_column_name(stats.loc['count'], 'matches played')
    average_time_played = _set_column_name(stats.loc['mean'], 'average time played')
    turns_in_goals = _set_column_name(goalies, 'turns in goals')
    return pd.DataFrame([matches_played, average_time_played, turns_in_goals])


def data_stats(data, goalies):
    if not data.empty:
        stats = rename_stats_fields(data.describe().loc[['count', 'mean']], goalies.sum())
        total_time = data.sum()
        total_time.name = 'total time played'
        return stats.append(total_time).fillna(0.0)
    return data


def goalies_stats(goalies_list):
    return {player: goalies_list.count(player) for player in goalies_list}


def time_for_players(round_nbr, filename):
    """
    Read the data file and returns tuples with time stats and goalies stats.
    """

    def _get_time(player, time_offs):
        return TOTAL_TIME - timeoff if player in goalies_list else TOTAL_TIME - timeoff * time_offs

    def _data_is_ok():
        if goalies_list:
            return reduce(lambda x, y: f'{x}{y}', goalies_list, '')
        return False

    def _time_stats():
        return {player: _get_time(player, nbr_of_time_offs[player]) for player in players_list}

    players_list, goalies_list, timeoff, nbr_of_time_offs, _ = gd.match_data(round_nbr, filename)
    if _data_is_ok():
        return _time_stats(), goalies_stats(goalies_list)
    return None


def generate_report(filename=None):
    """Generates the final report with time played and other
    information.
    """

    def _get_data():
        return [time_for_players(f'Round {round_nbr}', filename) for round_nbr in range(1, 19)]

    return data_stats(*valid_data(_get_data())).to_html()


def write_report(report):
    with open('report.html', 'w') as output:
        output.write(report)
