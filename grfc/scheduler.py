"""
Scheduler for the GRFC team players.
"""
import os
from functools import reduce
import pandas as pd
import xlrd


PLAYERS = ['Mitch', 'Ollie', 'Lachie', 'Nick', 'Henrik',
           'Noah', 'Elliot', 'Diesel', 'Angus', 'Xavier']
TOTAL_TIME = 40
INPUT_FOLDER = f'{os.environ["HOME"]}{os.sep}input{os.sep}'


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


def time_for_players(filename, round_nbr):

    def get_time(player, time_offs):
        return TOTAL_TIME - timeoff if player in goalies_list else TOTAL_TIME - timeoff * time_offs

    def data_is_ok():
        return players_list and goalies_list and timeoff and nbr_of_time_offs

    players_list, goalies_list, timeoff, nbr_of_time_offs = match_data(filename, round_nbr)
    if data_is_ok():
        return {player: get_time(player, nbr_of_time_offs[player]) for player in players_list}
    return None


def time_offs_per_player(data):

    def players_from_shifts():

        def get_shift(shift_nbr):
            return list(data.loc[:13, f'Player {shift_nbr}'].dropna().values)

        return reduce(lambda a, b: a + b, [get_shift(nbr) for nbr in range(1, 4)])
        
    players = players_from_shifts()
    return {player: players.count(player) for player in players}
