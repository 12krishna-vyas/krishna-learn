import boto3
from datetime import datetime

QUEUE_URL = "your-sqs-queue-url"
TABLE_NAME = "submission_metadata"

sqs = boto3.client("sqs")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

while True:
    response = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10
    )

    messages = response.get("Messages", [])
    for msg in messages:
        submission_id = msg["Body"]

        table.update_item(
            Key={"submission_id": submission_id},
            UpdateExpression="SET #s = :val, processed_at = :time",
            ExpressionAttributeNames={"#s":"status"},
            ExpressionAttributeValues={
                ":val":"Processed",
                ":time":datetime.utcnow().isoformat()
            }
        )

        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=msg["ReceiptHandle"]
        )

        print(f"Processed {submission_id}")

