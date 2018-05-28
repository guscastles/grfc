"""
Source module for the GRFC stats application.
"""
import os


__all__ = ['scheduler', 'game_time']
GRFC_FILE = 'GRFC 8H-1.xlsx'
PLAYERS = ['Mitch', 'Ollie', 'Lachie', 'Nick', 'Henrik',
           'Noah', 'Elliot', 'Diesel', 'Angus', 'Xavier']
TOTAL_TIME = 40


def __input_folder__():
    home_folder = 'HOME' if 'HOME' in os.environ else 'USERPROFILE'
    return f'{os.environ[home_folder]}{os.sep}input{os.sep}'


INPUT_FOLDER = __input_folder__()
