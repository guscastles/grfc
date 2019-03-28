from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/authenticate", methods=["POST"])
def authenticate():
    return "OK"
