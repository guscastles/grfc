"""
Web module for the GRFC app.
"""
from flask import Flask
APP = Flask(__name__)


@APP.route("/")
def index():
    return "Georges River Tigers - 8H"

