"""
Web module for the GRFC app.
"""
from flask import Flask
from grfc.game import play_time as pt, GRFC_FILE
application = Flask(__name__)


@application.route("/")
def index():
    return "Georges River Tigers - 8H"


@application.route("/report/")
def report():
    return pt.generate_report()


@application.route("/report/<grfc_file>")
def report_from_file(grfc_file):
    return pt.generate_report(GRFC_FILE)
