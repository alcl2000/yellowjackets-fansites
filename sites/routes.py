from flask import render_template
from sites import app
import json


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/taissa4nj")
def taissa4nj():
    data = []
    goals = []
    profiles = []
    with open("sites/content/taissa_instagram.json", "r") as pictures:
        profiles = json.load(pictures)
    with open("sites/content/taissa_info.json", "r") as json_data:
        data = json.load(json_data)
        goals = data[0]['article']
    return render_template("taissa4nj.html", details=data, tais_goals=goals,
                           profiles=profiles)
