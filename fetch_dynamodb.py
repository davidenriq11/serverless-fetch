import boto3
import os

def fetch_data(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])

    response = table.scan()
    data = response['Items']
    return(response)
