# -*- coding: utf-8 -*-
from functools import reduce
from . import TOTAL_TIME


def get_data(time_for_players, filename):
    return [time_for_players(f'Round {round_nbr}', filename) for round_nbr in range(1, 19)]


def set_column_name(column, name):
    column.name = name
    return column


def no_empty_data(data):
    return filter(lambda dt: dt is not None, data)


def time_stats(nbr_of_time_offs, players_list, timeoff, goalies_list):

    def _get_time(player, time_offs):
        return TOTAL_TIME - timeoff if player in goalies_list else TOTAL_TIME - timeoff * time_offs

    return {player: _get_time(player, nbr_of_time_offs[player]) for player in players_list}


def data_is_ok(goalies_list):
    if goalies_list:
        return reduce(lambda x, y: f'{x}{y}', goalies_list, '')
    return False
 