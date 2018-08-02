"""
Test module for the web component, powered by Flask.
"""
import pytest
from bs4 import BeautifulSoup as BSoup
from grfc import web


@pytest.fixture
def client():
    web.application.config['TESTING'] = True
    client = web.application.test_client()

    with web.application.app_context():
        yield client


def test_index(client):
    response = client.get('/')
    assert response.data.decode('UTF-8').startswith('Georges River')


@pytest.mark.file_report
def test_report_from_file(client):
    response = client.get('/report/grfc_file')
    soup = BSoup(response.data, 'html5lib')
    assert soup.find('table').find('tbody').find('th').text == 'matches played'


@pytest.mark.report
def test_report_from_google(client):
    response = client.get('/report/')
    soup = BSoup(response.data, 'html5lib')
    assert soup.find('table').find('tbody').find('th').text == 'matches played'
