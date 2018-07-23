# -*- coding: utf-8 -*-
"""
Handles the access and fetching of remote spreadsheets in Google Sheets.
"""
from apiclient.discovery import build
from googleapiclient.errors import HttpError
from httplib2 import Http
from oauth2client import file as credentials_file, client, tools
import pandas as pd


SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
SPREADSHEET_ID = '1Cwq8ZzjjNuWu6zz83pxGfHEZQFqWp2J8A7cfmcQSTVg'


def credentials():
    """Get the credentials for the Google Sheet authentication"""
    store = credentials_file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)
    return creds


def all_spreadsheets(user_credentials):
    """Fetches all spreadsheets from the Google Sheets account"""
    service = build('sheets', 'v4', http=user_credentials.authorize(Http()))
    return service.spreadsheets()


def spreadsheet_data(spreadsheets, ranges_names, spreadsheet_id=SPREADSHEET_ID):
    """Fetches a specific data range in a specific spreadsheet"""
    try:
        values = spreadsheets.values()
        if isinstance(ranges_names, list):
            return values.batchGet(spreadsheetId=spreadsheet_id, ranges=ranges_names).execute()
        return values.get(spreadsheetId=spreadsheet_id, range=ranges_names).execute()
    except HttpError:
        return {}


def fetch_data(round_name):
    """Convenience function to retrieve the data from a specific round"""
    round_data = spreadsheet_data(all_spreadsheets(credentials()), round_name)
    round_values = round_data.get('values', [])
    return pd.DataFrame(round_values[1:], columns=round_values[0])
    
