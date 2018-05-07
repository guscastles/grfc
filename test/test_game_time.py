"""
Test module for game time
"""
import os
import pytest
from grfc import game_time as gt, GRFC_FILE
from . import ROUND


def test_overall_time_offs():
    data = [gt.time_for_players(GRFC_FILE, f'Round {round_nbr}') for round_nbr in range(1, 19)]
    stats = gt.data_stats(*gt.valid_data(data))
    assert len(stats) == 4 and len(stats.columns) == 10
    assert 'turns as goalie' in stats.index
    assert dict(stats.loc[:, 'Nicholas']) == {'matches played': 5.0,
                                              'average time played': 33.4,
                                              'total time played': 167.0,
                                              'turns as goalie': 1.0}


@pytest.mark.wip
def test_run():
    gt.run()
    assert os.path.isfile('report.html')


def test_time_for_players():
    times = gt.time_for_players(GRFC_FILE, ROUND)
    assert times[0]['Angus'] == 34.0
