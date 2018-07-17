"""
Web module for the GRFC app.
"""
from flask import Flask
import grfc_game.play_time as pt
APP = Flask(__name__)


@APP.route("/")
def index():
    return "Georges River Tigers - 8H"


@APP.route("/report")
def report():
    return pt.generate_report()
