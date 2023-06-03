import boto3
from pymongo import MongoClient
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')

mongodb_collection = 'doctors2'

dynamodb_table = dynamodb.Table('doctors')

response = dynamodb_table.scan()

items = response['Items']

def convert_decimal(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

mongodb_client = MongoClient('localhost', 27017)

mongodb_db = mongodb_client['doctrue']

mongodb_collection = mongodb_db[mongodb_collection]

for item in items:
    converted_item = {k: convert_decimal(v) for k, v in item.items()}
    mongodb_collection.insert_one(converted_item)

mongodb_client.close()

print("Data inserted into MongoDB successfully.")
