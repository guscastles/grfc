"""
Scheduler for the GRFC team players.
"""
import os
from functools import reduce
import pandas as pd


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
    return pd.read_excel(f'{INPUT_FOLDER}{filename}', sheet_name=sheetname)


def time_data(data):
    return data.iloc[:15, :7]


def players(data):
    return list(map(lambda player: player.strip(), data['Present'].dropna()))


def goalies(data):
    return list(map(lambda goalie: goalie.strip(), data.loc[:1, 'Goalie']))


def match_data(filename, round_nbr):
    data = read_data_file(filename, round_nbr)
    players_list = players(data)
    return players_list, goalies(data), time_off(len(players_list))


def time_for_players(filename, round_nbr):

    def get_time(player):
        return TOTAL_TIME - timeoff if player in goalies_list else TOTAL_TIME - timeoff * 2

    players_list, goalies_list, timeoff = match_data(filename, round_nbr)
    return {player: get_time(player) for player in players_list}


def time_offs_per_player(data):

    def players_from_shifts():

        def get_shift(shift_nbr):
            return list(data.loc[:13, f'Player {shift_nbr}'].dropna().values)

        return reduce(lambda a, b: a + b, [get_shift(nbr) for nbr in range(1, 4)])
        
    players = players_from_shifts()
    return {player: players.count(player) for player in players}
