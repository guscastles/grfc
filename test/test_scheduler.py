import pytest
from math import ceil


PLAYERS = ['Mitch', 'Ollie', 'Lachie', 'Nick', 'Henrik', 'Noah', 'Elliot', 'Diesel', 'Angus', 'Xavier']
TOTAL_TIME = 20


def test_wait_time():

    def calculate_time(players):
        if players == 7:
            return 0.0
        return 1.5 * (4 - num_players + players)
     
    num_players = len(PLAYERS)
    half_time = 20
    players_present = [7, 8, 9, 10]
    times = [calculate_time(players) for players in players_present]
    assert times == [0, 3.0, 4.5, 6.0]
