"""
Test module for the game data module
"""
from grfc.game import game_data as gd
from . import GRFC_TEST_FILE
from . import ROUND


def read_data(func):
    return func(gd.read_data_file(GRFC_TEST_FILE, ROUND))


def read_empty_data(func):
    return func(gd.read_data_file('no_file')) is None


def test_wait_time():
    players_present = [7, 8, 9, 10]
    times = [gd.time_off(players) for players in players_present]
    assert times == [0, 3.0, 4.5, 6.0]


def test_read_data_file():
    assert list(read_data(gd.time_data).columns) == ['Shift', 'Player 1', 'Player 2', 'Player 3',
                                                     'Goalie', 'Present', 'Time Out (min)']


def test_players_present():
    assert read_data(gd.players) == ['Albert', 'Donald', 'Harry', 'Louis',
                                     'Mark', 'Nathan', 'Oswald', 'Charles']


def test_goalies():
    assert read_data(gd.goalies) == ['Donald', 'Louis']


def test_time_off_per_player():
    data = gd.read_data_file(GRFC_TEST_FILE, ROUND)
    time_offs = gd.time_offs_per_player(data)
    assert time_offs['Nathan'] == 1


def test_match_data_with_empty_values():
    assert gd.match_data(None) == (None, None, None, None, None)

