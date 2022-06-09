from flask import Flask,render_template

import csv


app = Flask(__name__)

@app.route('/calc')


def me():
    return render_template("me.html")


import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()