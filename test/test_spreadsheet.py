# -*- coding: utf-8 -*-
"""
Tests the reading of the file from the Google Sheets website.
"""
import pandas as pd
from grfc import remote_handler as rh


RANGE_NAME = 'Round {}!A1:H29'


def test_fetch_round_1_data_from_google_sheets():
    all_sheets = rh.all_spreadsheets(rh.credentials())
    grfc_spreadsheet = rh.spreadsheet_data(all_sheets, RANGE_NAME.format(1))
    values = grfc_spreadsheet.get('values', [])
    round_1 = pd.DataFrame(values[1:], columns=values[0])
    assert round_1.loc[0, 'Player 1'] == 'Elliot'
