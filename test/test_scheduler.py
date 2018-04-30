import pytest
from grfc import scheduler as sc


def time_data(data):
    return data.iloc[:15, :7]


def test_wait_time():
    players_present = [7, 8, 9, 10]
    times = [sc.calculate_time(players) for players in players_present]
    assert times == [0, 3.0, 4.5, 6.0]


def test_read_data_file():
    data = time_data(sc.read_data_file('GRFC 8H-1.xlsx', 'Round 4'))
    assert list(data.columns) == ['Shift', 'Player 1', 'Player 2', 'Player 3', 'Goalie', 'Present', 'Time Out (min)']
    players = data['Present'].dropna()
    assert list(players) == ['Angus', 'Diesel', 'Henrik', 'Lachlan ', 'Mitchell', 'Nicholas', 'Oliver', 'Xavier']
