# -*- coding: utf-8 -*-
"""
Tests the reading of the file from the Google Sheets website.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
SPREADSHEET_ID = '1Cwq8ZzjjNuWu6zz83pxGfHEZQFqWp2J8A7cfmcQSTVg'
RANGE_NAME = 'Round 1!A1:H29'


def credentials():
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    return creds
    

def spreadsheets(creds):
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    return service.spreadsheets()


def spreadsheet_data(spreadsheets, spreadsheet_id, range_name):
    return spreadsheets.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    

def test_fetch_round_1_data_from_google_sheets():
    all_spreadsheets = spreadsheets(credentials())
    grfc_spreadsheet = spreadsheet_data(all_spreadsheets, SPREADSHEET_ID, RANGE_NAME)
    values = grfc_spreadsheet.get('values', [])
    assert values
    import pandas as pd
    round_data = pd.DataFrame(values[1:], columns=values[0])
    assert round_data.loc[0, 'Player 1'] == 'Elliot'
