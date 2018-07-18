"""
Gives the mains statistics for the Tigers team.
"""
import pandas as pd
from . import game_data as gd
from .play_time_support import no_empty_data, set_column_name, get_data, data_is_ok, time_stats


def valid_data(data):
    time_stats = pd.DataFrame(list(map(lambda record: record[0], no_empty_data(data))))
    goalies = pd.DataFrame(list(map(lambda record: record[1], no_empty_data(data))))
    return time_stats, goalies


def rename_stats_fields(stats, goalies):
    matches_played = set_column_name(stats.loc['count'], 'matches played')
    average_time_played = set_column_name(stats.loc['mean'], 'average time played')
    turns_in_goals = set_column_name(goalies, 'turns in goals')
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
    players_list, goalies_list, timeoff, nbr_of_time_offs, _ = gd.match_data(round_nbr, filename)
    if data_is_ok(goalies_list):
        return time_stats(nbr_of_time_offs, players_list, timeoff, goalies_list), goalies_stats(goalies_list)
    return None


def generate_report(filename=None):
    """Generates the final report with time played and other
    information.
    """
    return data_stats(*valid_data(get_data(time_for_players, filename))).to_html()


def write_report(report):
    with open('report.html', 'w') as output:
        output.write(report)
