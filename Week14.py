import boto3
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('MyfavoriteMovies')
response = table.scan()
data = response['Item']

for item in data:
    print(item)
    
