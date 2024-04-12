from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
mongo_dbname = os.getenv("MONGO_DBNAME")
client = MongoClient(mongo_uri)
db = client[mongo_dbname]