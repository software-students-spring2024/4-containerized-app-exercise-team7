from flask import Flask
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



if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("FLASK_PORT", 5000))