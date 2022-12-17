#This will be the syntax to create the DynamoDB table:
import boto3

#Here we will interact with the AWS service
neew_dynamodb = boto3.resource('dynamodb')
#Below is the syntax to create the table
table = new_dynamodb.create_table (
     AttributeDefinitions=[
        {
            'AttributeName': 'author',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'MovieTitle',
            'AttributeType': 'S'
        }
    ],
    TableName='Myfavoritemovies',
    KeySchema=[
        {
            'AttributeName': 'author',
            'KeyType': 'HASH'
        },
        {
                    'AttributeName': 'MovieTitle',
                    'KeyType': 'RANGE'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
        },
        
        )