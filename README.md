### Publishing messages with AWS IoT Core to DynamoDB
#### Prerequisites: 
Configured AWS credentials, Python libraries **boto3, paho-mqtt, aws-cli**

#### Create a DynamoDB table:
* Run *create_table.py* 
* The table in the example script only has a hash key. Add range key if necessary. Read the section under `Primary key` [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)

#### Create an IoT Core thing:
* Go to IoT core from the AWS Console
* Give it any name, e.g. iotmarine, no need to fill other info
* Add a certificate: 'One-click certificate creation'
* Download and store certificate paths to *credentials.py* (including root CA) 

#### Edit the paths to certificate files in credentials.py and add an endpoint 
To find your endpoint, go to IoT Core -> Settings ->Endpoint

#### Give access to DynamoDB in the policies section of your IoT thing:
* Go to IoT core -> Secure -> Policies
* Add a new policy
* Copy paste from *policy.txt* (delete what is there already)

#### Create a rule for storing messages in DynamoDB:
* 'AWS IoT' -> 'Act' -> 'Create'
* Name: Name for the rule, e.g. IoTtoDynamo
* Description: e.g. Rule for sending IoT data to Dynamo
* Query statement: SELECT * FROM '#'
* Add action: choose "Split message into multiple columns of a DynamoDB table (DynamoDBv2)", -> 'Configure action'
* Choose a resource: Choose the table created earlier

#### Publish messages:
* Run *simulator.py*
* Sample data is published every 5s
* Run *get_data.py* to view table data

#### Useful sources: 
1. Boto3 documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
2. IoT Core overview: https://aws.amazon.com/iot-core/ 
3. IoT Rules Engine: https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules-tutorial.html
4. DynamoDB: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SettingUp.html







