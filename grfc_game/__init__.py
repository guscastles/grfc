"""
Source module for the GRFC stats application.
"""
import os


__all__ = ['game_data', 'play_time']
GRFC_FILE = 'GRFC 8H-1.xlsx'
PLAYERS = ['Mitch', 'Ollie', 'Lachie', 'Nick', 'Henrik',
           'Noah', 'Elliot', 'Diesel', 'Angus', 'Xavier']
TOTAL_TIME = 40


def _input_folder():
    home_folder = 'HOME' if 'HOME' in os.environ else 'USERPROFILE'
    return f'{os.environ[home_folder]}{os.sep}input{os.sep}'


INPUT_FOLDER = _input_folder()
