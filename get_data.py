import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Test-table')


response = table.scan()
items = response['Items']
print(items)