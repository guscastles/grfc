"""
Moduel that gives the mains statistics for the Tigers team.
"""
import pandas as pd
import grfc.game.play_time_support as pts
from . import game_data as gd


def valid_data(data):
    """Returns onle non-empty records from the given data"""
    time_stats = pd.DataFrame(list(map(lambda record: record[0], pts.no_empty_data(data))))
    goalies = pd.DataFrame(list(map(lambda record: record[1], pts.no_empty_data(data))))
    return time_stats, goalies


def rename_stats_fields(stats, goalies):
    """Renames the statistics fields to be more descriptive"""
    matches_played = pts.set_column_name(stats.loc['count'], 'matches played')
    average_time_played = pts.set_column_name(stats.loc['mean'], 'average time played')
    turns_in_goals = pts.set_column_name(goalies, 'turns in goals')
    return pd.DataFrame([matches_played, average_time_played, turns_in_goals])


def data_stats(data, goalies):
    """Returns the statistics from the game data and the turn in goals data"""
    if not data.empty:
        stats = rename_stats_fields(data.describe().loc[['count', 'mean']], goalies.sum())
        total_time = data.sum()
        total_time.name = 'total time played'
        stts = stats.append(total_time).fillna(0.0)
        for col in stts:
            stts[col] = stts[col].map('{:,.1f}'.format)
        return stts
    return data


def generate_report(filename=None):
    """Generates the final report with time played and other
    information.
    """
    return data_stats(*valid_data(pts.all_players_times(filename))).style.data.to_html()


def write_report(report):
    """Writes the report to a file 'report.html'."""
    with open('report.html', 'w') as output:
        output.write(report)
