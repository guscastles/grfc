"""
Source module for the GRFC stats application.
"""
import os


__all__ = ['scheduler', 'game_time']
GRFC_FILE = 'GRFC 8H-1.xlsx'
PLAYERS = ['Mitch', 'Ollie', 'Lachie', 'Nick', 'Henrik',
           'Noah', 'Elliot', 'Diesel', 'Angus', 'Xavier']
TOTAL_TIME = 40
INPUT_FOLDER = f'{os.environ["HOME"]}{os.sep}input{os.sep}'
