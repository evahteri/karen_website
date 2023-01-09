from flask import Flask
from flask import redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("gallery.html")

@app.route("/info")
def info():

    return render_template("info.html")

@app.route("/gallery")
def gallery():

    return render_template("gallery.html")
