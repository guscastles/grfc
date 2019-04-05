"""
GRFC Stats Collector Application

Flask module holding the main routes for the mobile application.
"""
from os import environ as env
from flask import Flask, render_template, redirect, url_for
from flask_talisman import Talisman
from grfcapp.validation import check_request_params
app = Flask(__name__)
"""Main Flask object"""

if env.get('FLASK_ENV', None) != 'development':
    Talisman(app)

app.before_request(check_request_params)

@app.route("/")
@app.route("/index")
@app.route("/login")
def login():
    """Login router function. Returns the *login.html* template."""
    return render_template("login.html")


@app.route("/authenticate", methods=["POST"])
def authenticate():
    """Authenticate router function. Once user is authenticated, redirects
    to the game choice page."""
    return redirect(url_for("game"))


@app.route("/game")
def game():
    """Displays the choice for either a new game, the current one or an already finished."""
    return render_template("game.html")
