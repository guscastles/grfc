"""
Season history module, created from a Jupyter Notebook.
"""
import functools as ft
from pandas import DataFrame
from . import game_data as gd


def read_raw_data(filename):
    """Returns the goals for each match"""
    return [gd.read_data_file(filename, f'Round {nbr}').iloc[15:, 2:4] for nbr in range(1, 19)]


def change_name(raw_data):
    """Creates the specific game metadata"""

    def _rename_columns(data):
        names = data.iloc[0, 0:2]
        return data.rename(columns={'Player 2': names[0], 'Player 3': names[1]}).drop(15, axis=0)

    new_names = _rename_columns(raw_data)
    return new_names.reset_index(drop=True)


def raw_scoreboard(raw_data):
    """Draft scoreboard from the given unprocessed data"""
    return [change_name(rdt) for rdt in raw_data]


def scoreboard(data):
    """Scoreboard from the given data"""
    return [scores.count() for scores in data]


def match_results(scoreboard_data):
    """Match results from the given scoreboard."""

    def _result(match_score):

        def _game_result(diff):
            return 'win' if diff > 0 else 'loss' if diff < 0 else 'tie'

        diff = match_score[0] - match_score[1]
        return _game_result(diff), match_score[0], match_score[1], match_score.index[1]

    return [_result(score) for score in scoreboard_data]


def results(data):
    """Presents the results in a table format"""
    return DataFrame(data, columns=['Result', 'Goals Scored', 'Goals Taken', 'Opponent'])


def raw_goals_by_player(data):
    """From the raw scoreboard, extracts the
    number of goals scored by each player
    """
    return ft.reduce(lambda a, b: a.append(b), [dt['Tigers'].dropna() for dt in data])


def goals_by_player(data):
    """Number of goals by player"""
    return data.value_counts()

