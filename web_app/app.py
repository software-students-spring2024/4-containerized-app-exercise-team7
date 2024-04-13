import os
import pymongo

connection = pymongo.MongoClient(os.getenv('MONGO_URI'))
db = connection[os.getenv('MONGO_DBNAME')]
users = db.users
strategies_docs = db.strategies
try:
    connection.admin.command("ping")  
    print(" *", "Connected to MongoDB!")  
except Exception as e:
    print(" * MongoDB connection error:", e)


