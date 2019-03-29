"""
Statistics Web Module

Web module for the GRFC app, presenting statisitcs for the season.
"""
from flask import Flask
from grfc.game import play_time as pt, GRFC_FILE
APP = Flask(__name__)


@APP.route("/")
def index():
    """Main route for the web app. Returns just the name of the team."""
    return "Georges River Tigers - 8H"


@APP.route("/report/")
def report():
    """Generates the report from the Google Sheets datasource."""
    return pt.generate_report()


@APP.route("/report/<grfc_file>")
def report_from_file(grfc_file):
    """Generates the report from a spreadsheet file."""
    return pt.generate_report(GRFC_FILE)
