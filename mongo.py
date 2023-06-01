from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['doctors2']

collection = db['doctors2']

print("Collection 'doctors2' created successfully.")
