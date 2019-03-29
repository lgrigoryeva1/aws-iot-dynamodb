import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='Table-1',
    KeySchema=[
        {
            'AttributeName': 'Time',
            'KeyType': 'HASH'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Time',
            'AttributeType': 'N'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }

)
table.meta.client.get_waiter('table_exists').wait(TableName='Table-1')