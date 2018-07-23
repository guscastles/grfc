# -*- coding: utf-8 -*-
"""
Tests the reading of the file from the Google Sheets website.
"""
import pytest
import pandas as pd
from grfc.game import remote_handler as rh, RANGE_NAME


@pytest.fixture(scope="module")
def all_sheets():
    return rh.all_spreadsheets(rh.credentials())


def test_fetch_round_1_data_from_google_sheets(all_sheets):
    round_1_spreadsheet = rh.spreadsheet_data(all_sheets, RANGE_NAME.format(1))
    values = round_1_spreadsheet.get('values', [])
    round_1 = pd.DataFrame(values[1:], columns=values[0])
    assert round_1.loc[0, 'Player 1'] == 'Elliot'


def test_fecth_invalid_round_from_google_sheets(all_sheets):
    no_round = rh.spreadsheet_data(all_sheets, RANGE_NAME.format(0))
    values = no_round.get('values', [])
    assert not values


def test_fetch_all_rounds_data_from_google_sheets(all_sheets):
    all_rounds = [rh.spreadsheet_data(all_sheets, RANGE_NAME.format(round)) for round in range(1, 19)]
    round_1_values = all_rounds[0].get('values', [])
    round_1 = pd.DataFrame(round_1_values[1:], columns=round_1_values[0])
    assert round_1.loc[0, 'Player 1'] == 'Elliot'


@pytest.mark.sst
def test_fetch_whole_tigers_spreadsheet(all_sheets):
    ranges = [f"'Round {round}'!A1:G29" for round in range(1, 19)]
    tigers = rh.spreadsheet_data(all_sheets, ranges)
    assert tigers.get('valueRanges', [])

