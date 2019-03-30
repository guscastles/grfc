"""
Unit tests for the mobile app.
"""
import pytest
import flask
from bs4 import BeautifulSoup
from grfcapp.app import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_login_path():
    with app.test_request_context('/login'):
        assert flask.request.path == '/login'


def test_login_screen(client):
    response = client.get("/login")
    body = BeautifulSoup(response.data)
    assert body.find("input", attrs={"name": "username"})
    assert body.find("input", attrs={"name": "password"})
    assert body.find("input", type="submit")


def test_authenticate_with_short_password(client):
    response = client.post("/authenticate", data={"username": "test", "password": "test"})
    message = response.json.get("errors").get("password").pop()
    assert message == 'Field must be between 12 and 20 characters long.'


def test_authenticate_with_no_username(client):
    response = client.post("/authenticate", data={"username": "", "password": "test"})
    message = response.json.get("errors").get("username").pop()
    assert message == "This field is required."


def test_authenticate_with_invalid_username(client):
    response = client.post("/authenticate", data={"username": "<script>alert('Alert')</script>", "password": "test"})
    message = response.json.get("errors").get("username").pop()
    assert message == "Invalid username"


#    body = BeautifulSoup(response.data)
#    assert body.find("div", attrs={"name": "choice"})