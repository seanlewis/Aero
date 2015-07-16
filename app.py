#! /usr/bin/env python

from flask import Flask, render_template, request
from flask.ext.pymongo import PyMongo

from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB at localhost:27017 
mongo = PyMongo(aerodb)

# Access the collection
aero = mongo.db.aerodromes

@app.route("/test")
def test_connection():
    icao_codes = mongo.db.aerodromes.find({'ICAO Codes': 'NZAA'})
    return render_template('index.html',
        icao_codes=icao_codes)

@app.route("/")
def index():
	connection = mysql.connect("127.0.0.1", "root", "root", "<SERVER ADDRESS>", 3306)
	c = connection.cursor(mysql.cursors.DictCursor)
	
	q = "SELECT * FROM media"

	if request.args.get('category', False):
		q += " WHERE category = '%s'" % request.args.get("category")

	c.execute(q)
	media = c.fetchall()

	cat = "SELECT distinct(category) from media"
	c.execute(cat)
	category = c.fetchall()

	connection.close()
	return render_template("index.html", media=media, categories=category)

if __name__ == "__main__":
	app.run(debug = True)