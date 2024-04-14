
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv
from pymongo import MongoClient
import os
from bson.objectid import ObjectId
import datetime

load_dotenv()

app = Flask(__name__)

#mongo_uri = os.getenv("MONGO_URI")
mongo_dbname = str(os.getenv("MONGO_DBNAME"))
client = MongoClient("mongodb://localhost:27017/?directConnection=true&serverSelectionTimeoutMS=2000")
db = client[mongo_dbname]
try:
    # verify the connection works by pinging the database
    db.command("ping")  # Use the db object to ping
    print(" *", "Connected to MongoDB!")  
except Exception as e:
    # the ping command failed, so the connection is not available.
    print(" * MongoDB connection error:", e)

@app.route("/")
def home():
    melodies = list(db.melodies.find())
    analytics = {"total melodies": len(melodies)}
    return render_template("index.html", melodies=melodies, analytics=analytics)

@app.route("/submit", methods=["GET","POST"])
def add():
    if request.method == "POST":
        melodydata = request.form['melody']
        db.melodies.insert_one({"melody": melodydata, "date":datetime.datetime.now()})
        return redirect(url_for("home"))
    return render_template("submit.html")

@app.route("/view")
def see():
    melodies = list(db.melodies.find())
    return render_template("view.html", melodies=melodies)

@app.route("/analyze/<id>")
def notes():
    melody = db.melodies.find_one({"_id": ObjectId(id)})
    notes =  analyze_melody(melody["melody"])
    return render_template("analyze.html", melody=melody, notes=notes)

def analyze_melody(melody):
    return["Note1", "Note2", "Note3"]

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("FLASK_PORT", 5000))

