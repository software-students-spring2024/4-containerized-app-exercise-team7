from flask import Flask, render_template
from dotenv import load_dotenv
from pymongo import MongoClient
import os
from bson.objectid import ObjectId
import datetime

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI")
mongo_dbname = os.getenv("MONGO_DBNAME")
client = MongoClient(mongo_uri)
db = client[mongo_dbname]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit")
def add():
    return render_template("submit.html")

@app.route("/view")
def see():
    return render_template("view.html")

@app.route("/analyze")
def notes():
    return render_template("analyze.html")

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("FLASK_PORT", 5000))