from flask import Flask
from flask import render_template


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
