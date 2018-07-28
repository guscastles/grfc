"""
Test module for game time
"""
import os
import pytest
from shutil import os as shos
from grfc.game import play_time as pt, INPUT_FOLDER, GRFC_FILE, \
     game_data as gd, play_time_support as pts
from . import ROUND


def _data_from_file(round_nbr):
    return gd.read_data_file(GRFC_FILE, round_nbr)


def test_file_available():
    assert os.path.isfile(f'{INPUT_FOLDER}{GRFC_FILE}'), 'File is not present'


def test_overall_time_offs():
    data = [pts._time_for_players(_data_from_file(f'Round {round_nbr}')) for round_nbr in range(1, 6)]
    stats = pt.data_stats(*pt.valid_data(data))
    assert len(stats) == 4 and len(stats.columns) == 10
    assert 'turns in goals' in stats.index
    assert dict(stats.loc[:, 'Nathan']) == {'matches played': 5.0,
                                              'average time played': 33.4,
                                              'total time played': 167.0,
                                              'turns in goals': 1.0}


def test_no_data_stats():
    data = []
    assert pt.data_stats(*pt.valid_data(data)).empty


def test_generate_report():
    report = pt.generate_report(GRFC_FILE)
    assert report.startswith('<table ')


def test_report_file():
    if os.path.isfile('report.html'):
        shos.unlink('report.html')
    pt.write_report(pt.generate_report(GRFC_FILE))
    assert os.path.isfile('report.html')
    shos.unlink('report.html')


def test_time_for_players():
    times = pts._time_for_players(_data_from_file(ROUND))
    assert times[0]['Albert'] == 34.0


def test_goalies_stats():
    goalies_list = ['Nathan', 'Henry', 'Nathan', 'Norbert']
    stats = pts.goalies_stats(goalies_list)
    assert 'Nathan' in stats

