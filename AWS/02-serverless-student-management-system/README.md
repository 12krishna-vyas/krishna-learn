# AWS Serverless Student Management System

## Project Overview

This project demonstrates a serverless web application using AWS services.

### Services Used

* Amazon S3 (Static Website Hosting)
* AWS Lambda
* Amazon DynamoDB
* IAM

## Architecture

User → S3 Static Website → Lambda Function URL → Lambda → DynamoDB

## Workflow

1. User opens the website hosted on S3.
2. User enters student details.
3. Frontend sends request to Lambda Function URL.
4. Lambda processes the request.
5. Student data is stored in DynamoDB.
6. Lambda returns a response to the website.

## Features

* Add Student
* View Students
* Serverless Architecture
* No EC2 Required

## Screenshots
Screenshots are available in the screenshots folder.




