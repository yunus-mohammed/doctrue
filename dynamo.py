import boto3
import os

#os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000', region_name='us-west-2')
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

table = dynamodb.create_table(
    TableName='doctors',
    KeySchema=[
        {
            'AttributeName': 'doctor_id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'doctor_id',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName='doctors')

print("Table 'doctors' created successfully.")
