"""
Game data collected on the GRFC team players.
"""
from functools import reduce
from pandas import read_excel, options
import xlrd
from . import PLAYERS, INPUT_FOLDER


GOALIE = 'Goalie'


def time_off(number_of_players):
    return 1.5 * (4 - len(PLAYERS) + number_of_players) if number_of_players > 7 else 0


def read_data_file(filename, sheetname=None):
    """Fetches the raw data from an Excel spreadsheet"""
    try:
        options.display.float_format = '{:,.1f}'.format
        return read_excel(f'{INPUT_FOLDER}{filename}', sheet_name=sheetname)
    except xlrd.biffh.XLRDError:
        return None


def time_data(data):
    return data.iloc[:15, :7]


def match_data(data):
    players_list = players(data)
    if data is not None:
        return players_list, goalies(data), time_off(len(players_list)), \
               time_offs_per_player(data), goals_scored(data)
    return None, None, None, None, None


def players(data, column='Present'):
    return [rec.strip() for rec in  data.loc[:13, column].dropna()] if data is not None else data


def goalies(data, column=GOALIE):
    return players(data, column)


def goals_scored(data):
    return data.iloc[16:, 2].dropna()


def time_offs_per_player(data):
    """Calculates the number of time offs per player from the given data"""

    def _players_from_shifts():

        def _get_shift(shift_nbr):
            return list(data.loc[:13, f'Player {shift_nbr}'].dropna())

        return reduce(lambda a, b: a + b, [_get_shift(nbr) for nbr in range(1, 4)])

    shift_players = _players_from_shifts()
    return {player: shift_players.count(player) for player in shift_players}

