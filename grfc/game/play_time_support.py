# -*- coding: utf-8 -*-
from functools import reduce
from . import TOTAL_TIME


def get_data(time_for_players, filename):
    return [time_for_players(f'Round {round_nbr}', filename) for round_nbr in range(1, 19)]


def set_column_name(column, name):
    column.name = name
    return column


def no_empty_data(data):
    """Filters out empty records from the given data."""
    return filter(lambda dt: dt is not None, data)


def time_stats(players_list, timeoff, nbr_of_time_offs):
    """Returns the time statistics from the given parameters"""

    def _get_time(player, time_offs):
        return TOTAL_TIME - timeoff * time_offs

    return {player: _get_time(player, nbr_of_time_offs[player]) for player in players_list}


def data_is_ok(goalies_list):
    """Checks is the data is non-empty by checking if the goalies list is not empty"""
    if goalies_list:
        return reduce(lambda x, y: f'{x}{y}', goalies_list, '')
    return False
 