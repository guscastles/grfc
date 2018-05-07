from grfc import scheduler as sc, GRFC_FILE
from . import ROUND


def read_data(func):
    return func(sc.read_data_file(GRFC_FILE, ROUND))


def test_wait_time():
    players_present = [7, 8, 9, 10]
    times = [sc.time_off(players) for players in players_present]
    assert times == [0, 3.0, 4.5, 6.0]


def test_read_data_file():
    assert list(read_data(sc.time_data).columns) == ['Shift', 'Player 1', 'Player 2', 'Player 3', 'Goalie', 'Present', 'Time Out (min)']


def test_players_present():
    assert read_data(sc.players) == ['Angus', 'Diesel', 'Henrik', 'Lachlan', 'Mitchell', 'Nicholas', 'Oliver', 'Xavier']


def test_goalies():
    assert read_data(sc.goalies) == ['Diesel', 'Lachlan']


def test_time_for_players():
    times = sc.time_for_players(GRFC_FILE, ROUND)
    assert times[0]['Angus'] == 34.0


def test_time_off_per_player():
    data = sc.read_data_file(GRFC_FILE, ROUND)
    time_offs = sc.time_offs_per_player(data)
    assert time_offs['Nicholas'] == 1
