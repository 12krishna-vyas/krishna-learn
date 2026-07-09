import os
import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
sqs = boto3.client("sqs")


def lambda_handler(event, context):

    table = dynamodb.Table(os.environ["TABLE_NAME"])
    queue_url = os.environ["QUEUE_URL"]

    body = json.loads(event["body"])

    order_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()

    order = {
        "orderId": order_id,
        "customerName": body["customerName"],
        "email": body["email"],
        "product": body["product"],
        "quantity": body["quantity"],
        "amount": body["amount"],
        "status": "PENDING",
        "createdAt": now,
        "updatedAt": now
    }

    table.put_item(Item=order)

    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(order)
    )

    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "Order Created",
            "orderId": order_id,
            "status": "PENDING"
        })
    }
