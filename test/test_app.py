"""
Unit tests for the mobile app.
"""
import pytest
import flask
from bs4 import BeautifulSoup
import os
os.environ["FLASK_ENV"] = "development"
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
    body = BeautifulSoup(response.data, 'html5lib')
    assert body.find("input", attrs={"name": "username"})
    assert body.find("input", attrs={"name": "password"})
    assert body.find("input", type="submit")


def test_authenticate_with_short_password(client):
    response = client.post("/authenticate",
                           data={"username": "test", "password": "test"})
    message = response.json.get("errors").get("password").pop()
    assert message == 'Field must be between 12 and 20 characters long.'


def test_authenticate_with_no_username(client):
    response = client.post("/authenticate",
                           data={"username": "", "password": "test"})
    message = response.json.get("errors").get("username").pop()
    assert message == "This field is required."


def test_authenticate_with_invalid_username(client):
    response = client.post("/authenticate",
                           data={"username": "<script>alert('Alert')</script>",
                                 "password": "test"})
    message = response.json.get("errors").get("username").pop()
    assert message == "Invalid username"


def test_game_report_page():
    with app.test_request_context('/game/report/round/2'):
        assert flask.request.path == '/game/report/round/2'


def test_game_report_with_wrong_round(client):
    response = client.get("/game/report/round/0")
    body = BeautifulSoup(response.data, 'html5lib')
    report_tag = body.find("div", attrs={"name": "round_0"})
    assert report_tag
    assert report_tag.text.strip() == 'Report not available.'


def test_game_report(client):
    response = client.get("/game/report/round/2")
    body = BeautifulSoup(response.data, 'html5lib')
    report_tag = body.find("div", attrs={"name": "round_2"})
    assert report_tag
    assert len(report_tag.text.strip()) > 50


def test_no_page_found(client):
    response = client.get("/not_there")
    body = BeautifulSoup(response.data, 'html5lib')
    message_div = body.find("div", attrs={"name": "not_found"})
    assert message_div
    message = message_div.find("p") 
    assert message.text.strip() == ("Oops! This page is not there. Please "
                                    "contact the administrator for further"
                                        " information.")
