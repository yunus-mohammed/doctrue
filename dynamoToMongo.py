import boto3
from pymongo import MongoClient

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('doctors')

client = MongoClient('mongodb://localhost:27017/')
db = client['doctors2']
collection = db['doctors2']

response = table.scan()

for item in response['Items']:
    collection.insert_one(item)

print("Data copied successfully from 'doctors' to 'doctors2'.")
