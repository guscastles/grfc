"""
Source module for the GRFC stats application.
"""
import os


__all__ = ['game_data', 'play_time', 'remote_handler', 'season_history']
GRFC_FILE = 'GRFC U8.xlsx'
PLAYERS = ['Mitch', 'Ollie', 'Lachie', 'Nick', 'Henrik',
           'Noah', 'Elliot', 'Diesel', 'Angus', 'Xavier']
TOTAL_TIME = 40
RANGE_NAME = 'Round {}!A1:G29'


def _input_folder():
    home_folder = 'HOME' if 'HOME' in os.environ else 'USERPROFILE'
    return f'{os.environ[home_folder]}{os.sep}input{os.sep}'


INPUT_FOLDER = _input_folder()
