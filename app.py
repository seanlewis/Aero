#! /usr/bin/env python

from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB at localhost:27017 
client = MongoClient()

# Connect to the aerodb database
db = client.aerodb

@app.route("/")
def test_connection():
    items = db.aerodromes.find()

    return render_template('index.html',
        items=items)

@app.route("/<icao>")
def test_connection(icao):
    items = db.aerodromes.find()

    return render_template('index.html',
        items=items)

if __name__ == "__main__":
	app.run(debug = True)