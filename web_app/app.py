from flask import Flask, render_template, request
from dotenv import load_dotenv
from pymongo import MongoClient
import os
from bson.objectid import ObjectId
import datetime
import requests

load_dotenv()


app = Flask(__name__)
app.secret_key = '232323112@@11'

# mongo_uri = os.getenv("MONGO_URI")
# mongo_dbname = os.getenv("MONGO_DBNAME")
# client = MongoClient(mongo_uri)
# db = client[mongo_dbname]

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

@app.route("/send", methods=['GET', 'POST'])
def send_file_to_ml_app():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            url = 'http://goofy_austin:5001/upload'
            files = {'file': (file.filename, file)}
            response = requests.post(url, files=files)
            return response.json()
    return render_template('upload.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=os.getenv("FLASK_PORT", 5000))