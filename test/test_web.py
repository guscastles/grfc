"""
Test module for the web component, powered by Flask.
"""
import pytest
from bs4 import BeautifulSoup as BSoup
from grfc import web


@pytest.fixture
def client():
    web.APP.config['TESTING'] = True
    client = web.APP.test_client()

    with web.APP.app_context():
        yield client


def test_index(client):
    response = client.get('/')
    assert response.data.decode('UTF-8').startswith('Georges River')


@pytest.mark.flask
def test_report(client):
    response = client.get('/report')
    soup = BSoup(response.data, 'html5lib')
    assert soup.find('table').find('tbody').find('th').text == 'matches played'
