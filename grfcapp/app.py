"""
Flask Application

Flask module holding the main routes for the mobile application.
"""
from flask import Flask, render_template
app = Flask(__name__)
"""Main Flask object"""


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
    return "OK"
