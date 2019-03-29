# -*- coding: utf-8 -*-
"""
**play_time_support.py**

Supporing functions for module play_time. 

@author: Nick Miamoto-Garcia
"""
from functools import reduce
import pandas as pd
from grfc.game import TOTAL_TIME
import grfc.game.game_data as gd
import grfc.game.remote_handler as rh


def all_players_times(time_for_players, filename):

    def _create_dataframe(round_sheet):
        values = round_sheet.get('values', [])
        return pd.DataFrame(values[1:], columns=values[0])
    
    def _remote_data():
        ranges = [f"'Round {round}'!A1:G29" for round in range(1, 19)]
        sheet = rh.spreadsheet_data(ranges)
        return [_create_dataframe(round_sheet) for round_sheet in sheet.get('valueRanges', [])]

    def _get_data(round_nbr):
        return gd.read_data_file(filename, f'Round {round_nbr}') if filename else remote_data[round_nbr - 1]

    remote_data = _remote_data()
    return [time_for_players(_get_data(round_nbr)) for round_nbr in range(1, 19)]


def time_for_players(data):
    """ Read the data file and returns tuples with time stats and goalies stats.
    """
    players_list, goalies_list, timeoff, nbr_of_time_offs, _ = gd.match_data(data)
    if data_is_ok(goalies_list):
        return time_stats(players_list, timeoff, nbr_of_time_offs), \
               goalies_stats(goalies_list)
    return None


def data_is_ok(goalies_list):
    """Checks is the data is non-empty by checking if the goalies list is not empty"""
    if goalies_list:
        return reduce(lambda x, y: f'{x}{y}', goalies_list, '')
    return False


def time_stats(players_list, timeoff, nbr_of_time_offs):
    """Returns the time statistics from the given parameters"""

    def _get_time(player, time_offs):
        return TOTAL_TIME - timeoff * (0 if time_offs is None else time_offs)

    return {player: _get_time(player, nbr_of_time_offs.get(player)) for player in players_list}


def goalies_stats(goalies_list):
    """Returns the number of turn in goals for each player"""
    return {player: goalies_list.count(player) for player in goalies_list}


def set_column_name(column, name):
    """Sets the new name for the given column."""
    column.name = name
    return column


def no_empty_data(data):
    """Filters out empty records from the given data."""
    return filter(lambda dt: dt is not None, data)

