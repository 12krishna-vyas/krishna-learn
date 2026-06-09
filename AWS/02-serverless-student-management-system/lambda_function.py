import json
import boto3
import uuid
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

def lambda_handler(event, context):

    method = event.get(
        "requestContext",
        {}
    ).get(
        "http",
        {}
    ).get(
        "method",
        "POST"
    )

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Allow-Methods": "*"
    }

    if method == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": headers,
            "body": ""
        }

    if method == "POST":

        body = json.loads(event["body"])

        student = {
            "id": str(uuid.uuid4()),
            "name": body["name"],
            "course": body["course"]
        }

        table.put_item(Item=student)

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({
                "message": "Student Added",
                "student": student
            })
        }

    elif method == "GET":

        response = table.scan()

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps(
                response["Items"],
                cls=DecimalEncoder
            )
        }

    return {
        "statusCode": 400,
        "headers": headers,
        "body": json.dumps({
            "message": "Invalid Request"
        })
    }
