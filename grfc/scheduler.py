"""
Scheduler for the GRFC team players.
"""
import pandas as pd
import os


PLAYERS = ['Mitch', 'Ollie', 'Lachie', 'Nick', 'Henrik', 'Noah', 'Elliot', 'Diesel', 'Angus', 'Xavier']
TOTAL_TIME = 20
INPUT_FOLDER = f'{os.environ["HOME"]}{os.sep}input{os.sep}'


def calculate_time(players):
    if players == 7:
        return 0.0
    return 1.5 * (4 - len(PLAYERS) + players)


def read_data_file(filename, sheetname=None):
    """Reads the Excel file with a given round data especified by filename
       in the standard input folder.
    """
    return pd.read_excel(f'{INPUT_FOLDER}{filename}', sheet_name=sheetname)
