from flask import render_template
from sites import app


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/taissa4nj")
def taissa4nj():
    return render_template("taissa4nj.html")