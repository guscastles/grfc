"""
Scheduler for the GRFC team players.
"""
from functools import reduce
import pandas as pd
import xlrd
from grfc import PLAYERS, INPUT_FOLDER


def time_off(number_of_players):
    if number_of_players == 7:
        return 0.0
    return 1.5 * (4 - len(PLAYERS) + number_of_players)


def read_data_file(filename, sheetname=None):
    """Reads the Excel file with a given round data especified by filename
       in the standard input folder.
    """
    try:
        return pd.read_excel(f'{INPUT_FOLDER}{filename}', sheet_name=sheetname)
    except xlrd.biffh.XLRDError:
        return None


def time_data(data):
    return data.iloc[:15, :7]


def players(data):
    return list(map(lambda player: player.strip(), data['Present'].dropna()))


def goalies(data):
    return list(map(lambda goalie: goalie.strip(), data.loc[:1, 'Goalie'].dropna()))


def match_data(filename, round_nbr):
    data = read_data_file(filename, round_nbr)
    if data is not None:
        players_list = players(data)
        nbr_of_time_offs = time_offs_per_player(data)
        return players_list, goalies(data), time_off(len(players_list)), nbr_of_time_offs
    return None, None, None, None


def time_offs_per_player(data):
    """
    Calculates the number of time offs per player from the given data
    """

    def players_from_shifts():

        def get_shift(shift_nbr):
            return list(data.loc[:13, f'Player {shift_nbr}'].dropna().values)

        return reduce(lambda a, b: a + b, [get_shift(nbr) for nbr in range(1, 4)])

    shift_players = players_from_shifts()
    return {player: shift_players.count(player) for player in shift_players}
