"""
Test module for the web component, powered by Flask.
"""
import pytest
from grfc import web


@pytest.fixture
def client():
    web.APP.config['TESTING'] = True
    client = web.APP.test_client()

    with web.APP.app_context():
        yield client


@pytest.mark.flask
def test_index(client):
    response = client.get('/')
    assert response.data.decode('UTF-8').startswith('Georges River')
