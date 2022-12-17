import boto3

from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb', region_name= 'us-east-1')
table = dynamodb.Table('MyFavoriteMovies')
print("Who is the author of Cybersecurity Incident?")

response = table.query(
    KeyConditionExpression=Key('author').eq('Gilbert')
)

for i in response['Item']:
    print(i['author'], ":", i['MovieTitle'])
    