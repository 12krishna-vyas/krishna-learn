#  **Serverless Face Recognition System using AWS**

A serverless face recognition application built using **Amazon EC2, Amazon S3, AWS Lambda, Amazon Rekognition, Amazon DynamoDB, IAM, Flask, Python, HTML, and CSS**.

The application allows users to upload their name and image through a web interface hosted on Amazon EC2. Once the image is uploaded, Amazon S3 automatically triggers an AWS Lambda function, which uses Amazon Rekognition to compare the uploaded face with a collection of known faces. If a match is found, the user's metadata is stored in Amazon DynamoDB.

---

##  Features

- Web application hosted on Amazon EC2
- Upload name and image using a Flask-based frontend
- Store uploaded images in Amazon S3
- Automatic S3 event trigger for AWS Lambda
- Face matching using Amazon Rekognition
- Store matched user metadata in Amazon DynamoDB
- IAM Roles for secure access without hardcoded AWS credentials

---

##  AWS Services Used

- Amazon EC2
- Amazon S3
- AWS Lambda
- Amazon Rekognition
- Amazon DynamoDB
- AWS IAM

---

##  Project Workflow

User
   │
   ▼
Flask Web Application (EC2)
   │
   ▼
Amazon S3 (face-upload123)
   │
   ▼
S3 ObjectCreated Event
   │
   ▼
AWS Lambda
   │
   ▼
Amazon Rekognition Collection
   │
   ▼
Compare with Known Faces
   │
   ▼
Match Found
   │
   ▼
Amazon DynamoDB (FaceMetadata)

1. The user enters their **name** and uploads an image through the web application hosted on Amazon EC2.
2. The Flask backend uploads the image to the **face-upload123** S3 bucket.
3. Amazon S3 automatically triggers an AWS Lambda function.
4. Lambda retrieves the uploaded image and searches for a matching face in the Rekognition Collection.
5. The Rekognition Collection is built using the reference images stored in the **known-faces123** S3 bucket.
6. If a matching face is found, Lambda stores the user's metadata (Name, Image Name, Timestamp, and Similarity Score) in the **FaceMetadata** DynamoDB table.

---

## Learning Outcomes

- Event-driven architecture on AWS
- Amazon S3 Event Notifications
- AWS Lambda automation
- Face recognition using Amazon Rekognition
- Metadata storage with DynamoDB
- IAM Roles and secure AWS access
- Flask application deployment on Amazon EC2
- Boto3 integration with AWS services

---

## Author

**Krishna Vyas**

If you found this project useful, feel free to ⭐ this repository and connect with me on LinkedIn.
https://www.linkedin.com/posts/krishna-vyas-b80183240_aws-amazonwebservices-cloudcomputing-ugcPost-7478668755531759616-b_cI/?utm_source=share&utm_medium=member_desktop&rcm=ACoAADvTbtABCfCXWoDoz470UMjzlL1TEx48AgE
