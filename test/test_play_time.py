"""
Test module for game time
"""
import os
import pytest
from grfc import play_time as gt, INPUT_FOLDER, GRFC_FILE
from . import ROUND


def test_file_available():
    assert os.path.isfile(f'{INPUT_FOLDER}{GRFC_FILE}'), 'File is not present'


def test_overall_time_offs():
    data = [gt.time_for_players(GRFC_FILE, f'Round {round_nbr}') for round_nbr in range(1, 6)]
    stats = gt.data_stats(*gt.valid_data(data))
    assert len(stats) == 4 and len(stats.columns) == 10
    assert 'turns in goals' in stats.index
    assert dict(stats.loc[:, 'Nicholas']) == {'matches played': 5.0,
                                              'average time played': 33.4,
                                              'total time played': 167.0,
                                              'turns in goals': 1.0}


def test_generate_report():
    gt.generate_report()
    assert os.path.isfile('report.html')


def test_time_for_players():
    times = gt.time_for_players(GRFC_FILE, ROUND)
    assert times[0]['Angus'] == 34.0


def test_goalies_stats():
    goalies_list = ['Nicholas', 'Herik', 'Nicholas', 'Noah']
    stats = gt.goalies_stats(goalies_list)
    assert 'Nicholas' in stats
