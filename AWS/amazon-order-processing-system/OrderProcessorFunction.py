import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")


def lambda_handler(event, context):

    table = dynamodb.Table(os.environ["TABLE_NAME"])
    topic_arn = os.environ["SNS_TOPIC_ARN"]

    for record in event["Records"]:

        order = json.loads(record["body"])

        order_id = order["orderId"]
        now = datetime.utcnow().isoformat()

        table.update_item(
            Key={
                "orderId": order_id
            },
            UpdateExpression="SET #s = :s, updatedAt = :u",
            ExpressionAttributeNames={
                "#s": "status"
            },
            ExpressionAttributeValues={
                ":s": "CONFIRMED",
                ":u": now
            }
        )

        message = f"""
Order Confirmed!

Order ID : {order_id}

Customer : {order['customerName']}

Product : {order['product']}

Quantity : {order['quantity']}

Amount : ₹{order['amount']}

Status : CONFIRMED
"""

        sns.publish(
            TopicArn=topic_arn,
            Subject="Your Order is Confirmed",
            Message=message
        )

    return {
        "statusCode": 200,
        "body": json.dumps("Order processed successfully")
    }
