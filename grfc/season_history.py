"""
Season history module, created from a Jupyter Notebook.
"""
from functools import reduce
from pandas import DataFrame
from . import game_data as gd


# Get the goals for each match
def read_raw_data(filename):
    return [gd.read_data_file(filename, f'Round {nbr}').iloc[15:, 2:4] for nbr in range(1, 9)]


# Create the specific game data
def change_name(raw_data):

    def __rename_columns__(data):
        names = data.iloc[0, 0:2]
        return data.rename(columns={'Player 2': names[0], 'Player 3': names[1]}).drop(15, axis=0)

    new_names = __rename_columns__(raw_data)
    return new_names.reset_index(drop=True)


def raw_scoreboard(raw_data):
    """Draft scoreboard from the given unprocessed data"""
    return [change_name(rdt) for rdt in raw_data]


def scoreboard(data):
    """Scoreboard from the given data"""
    return [scores.count() for scores in data]


# Now, we add the logic to show that it is a win, loss, or tie.
def match_results(scoreboard_data):
    """Match results from the given scoreboard."""

    def __result__(match_score):

        def __game_result__(diff):
            return 'win' if diff > 0 else 'loss' if diff < 0 else 'tie'

        diff = match_score[0] - match_score[1]
        return __game_result__(diff), match_score[0], match_score[1], match_score.index[1]

    return [__result__(score) for score in scoreboard_data]



# We present the results in a table
def results(data):
    return DataFrame(data, columns=['Result', 'Goals Scored', 'Goals Taken', 'Opponent'])


# From the raw scoreboard, we can then extract the number of goals scored by each player
def raw_goals_by_player(data):
    return reduce(lambda a, b: a.append(b), [dt['Tigers'].dropna() for dt in data])


def goals_by_player(data):
    return data.value_counts()
