"""
Scheduler for the GRFC team players.
"""
from functools import reduce
import pandas as pd
import xlrd
from grfc import PLAYERS, INPUT_FOLDER


GOALIE = 'Goalie'


def time_off(number_of_players):
    return 1.5 * (4 - len(PLAYERS) + number_of_players) if number_of_players > 7 else 0


def read_data_file(filename, sheetname=None):
    try:
        return pd.read_excel(f'{INPUT_FOLDER}{filename}', sheet_name=sheetname)
    except xlrd.biffh.XLRDError:
        return None


def time_data(data):
    return data.iloc[:15, :7]


def players(data, column='Present'):
    return [player.strip() for player in data.loc[:13, column].dropna()] if data is not None else data


def goalies(data, column=GOALIE):
    return players(data, column);


def match_data(filename, round_nbr):
    data = read_data_file(filename, round_nbr)
    players_list = players(data)
    if data is not None:
        return players_list, players(data, GOALIE), time_off(len(players_list)), time_offs_per_player(data)
    return None, None, None, None


def time_offs_per_player(data):
    """
    Calculates the number of time offs per player from the given data
    """

    def players_from_shifts():

        def get_shift(shift_nbr):
            return list(data.loc[:13, f'Player {shift_nbr}'].dropna())

        return reduce(lambda a, b: a + b, [get_shift(nbr) for nbr in range(1, 4)])

    shift_players = players_from_shifts()
    return {player: shift_players.count(player) for player in shift_players}
