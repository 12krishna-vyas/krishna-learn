Replace placeholders.
from flask import Flask, request, render_template_string
import boto3
import MySQLdb
from datetime import datetime
import uuid

app = Flask(__name__)

# CONFIG
BUCKET_NAME = "your-bucket-name"
DYNAMO_TABLE = "submission_metadata"
SQS_QUEUE_URL = "your-sqs-queue-url"
SNS_TOPIC_ARN = "your-sns-topic-arn"

DB_HOST = "your-rds-endpoint"
DB_USER = "admin"
DB_PASS = "password"
DB_NAME = "studentdb"

# AWS clients (IAM role based)
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
sqs = boto3.client("sqs")
sns = boto3.client("sns")

table = dynamodb.Table(DYNAMO_TABLE)

HTML = """
<h2>Assignment Submission</h2>
<form method="POST" enctype="multipart/form-data">
Name:<br><input type="text" name="name"><br><br>
Email:<br><input type="email" name="email"><br><br>
Course:<br><input type="text" name="course"><br><br>
PDF:<br><input type="file" name="file"><br><br>
<button type="submit">Submit</button>
</form>
"""

@app.route("/", methods=["GET","POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]
        file = request.files["file"]

        if not file.filename.endswith(".pdf"):
            return "Only PDF allowed"

        submission_id = str(uuid.uuid4())
        filename = f"{submission_id}.pdf"

        # 1. Insert into RDS
        conn = MySQLdb.connect(host=DB_HOST,user=DB_USER,passwd=DB_PASS,db=DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name,email,course) VALUES (%s,%s,%s)",
            (name,email,course)
        )
        conn.commit()
        cursor.close()
        conn.close()

        # 2. Upload to S3
        s3.upload_fileobj(file, BUCKET_NAME, filename)

        # 3. Store metadata in DynamoDB
        table.put_item(Item={
            "submission_id": submission_id,
            "student_email": email,
            "file_name": filename,
            "status": "Submitted",
            "submitted_at": datetime.utcnow().isoformat()
        })

        # 4. Send message to SQS
        sqs.send_message(
            QueueUrl=SQS_QUEUE_URL,
            MessageBody=submission_id
        )

        # 5. Notify via SNS
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=f"New submission received: {submission_id}"
        )
