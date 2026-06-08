Build a Student Assignment Submission System where:
● App runs on EC2
● File stored in S3
● Student record stored in RDS
● Submission metadata stored in DynamoDB
● SQS used for background processing
● SNS used for email notification
● All inside a custom VPC

● EC2 is in Public Subnet
● RDS is in Private Subnet
● RDS is NOT publicly accessible
● EC2 talks to AWS services over public internet (no NAT needed)

�� Step-by-Step Infrastructure Guide

1️⃣ Create VPC
VPC CIDR:
10.0.0.0/16
Create:
● 1 Public Subnet → 10.0.1.0/24
● 1 Private Subnet → 10.0.2.0/24
● Attach Internet Gateway
● Public Route Table:
o 0.0.0.0/0 → IGW
● Associate public subnet to public route table

● Private subnet has no internet route

2️⃣ Security Groups
EC2 Security Group
Allow:
● 22 (SSH)
● 5000 (App testing)
Outbound: Allow all

RDS Security Group
Allow:
● MySQL (3306)
Source:
● EC2 Security Group (NOT 0.0.0.0/0)
This enforces VPC-level isolation.

3️⃣ Launch EC2 (Ubuntu)
Attach IAM Role with policy allowing:
● s3:PutObject
● dynamodb:PutItem
● dynamodb:GetItem
● sqs:SendMessage
● sqs:ReceiveMessage
● sns:Publish
No access keys.

4️⃣ Create S3 Bucket
Name:
student-assignment-bucket-&lt;unique&gt;
● Block public access ON
● Versioning enabled (optional)

5️⃣ Create RDS (Private Subnet)
● Engine: MySQL
● Public access: NO
● Subnet group: include private subnet
● Security group: RDS SG
Create table:
CREATE DATABASE studentdb;

USE studentdb;

CREATE TABLE students (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100) UNIQUE,
course VARCHAR(100),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

6️⃣ Create DynamoDB Table
Table:
submission_metadata

Partition key:
submission_id (String)

7️⃣ Create SQS
Queue:
assignment-processing-queue

8️⃣ Create SNS
Topic:
assignment-notification-topic
Create email subscription.
Confirm subscription.

When student submits form:
1. Insert student record in RDS
2. Upload file to S3
3. Insert metadata into DynamoDB
4. Send message to SQS
5. Publish message to SNS
All executed from EC2 Flask app.

�� Background Processing (Without Lambda)
Students must create a simple worker script:
worker.py
It will:
● Poll SQS
● Read message

● Update DynamoDB status to “Processed”
● Delete message from queue
Run worker manually in second terminal:
python3 worker.py
Output:
● Asynchronous processing
● Queue consumption
● Distributed systems basics

Below are the requested items:
1. ✅ Full working Flask app (EC2 → S3, RDS, DynamoDB, SQS, SNS)
2. ✅ worker.py for SQS processing
3. ✅ IAM policy JSON
4. ✅ Architecture diagram visuals
Services used:
● Amazon EC2
● Amazon S3
● Amazon RDS
● Amazon DynamoDB
● Amazon SQS
● Amazon SNS
● Amazon VPC
