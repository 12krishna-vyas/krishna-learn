# Amazon Order Processing System (AWS Serverless Project)

## Overview

This project demonstrates a serverless Amazon-style order processing system built using AWS services. Customers submit orders through an API Gateway endpoint. Orders are stored in DynamoDB, processed asynchronously using Amazon SQS, and confirmed through AWS Lambda and Amazon SNS.

The project follows an event-driven architecture and showcases how multiple AWS services can be integrated to build a scalable backend application.

---


## Architecture

```text
                Customer
                    │
                    ▼
              API Gateway
                    │
                    ▼
        CreateOrder Lambda
            │               │
            │               ▼
            │         Amazon SQS
            │               │
            ▼               ▼
      Amazon DynamoDB   OrderProcessor Lambda
      (Store Order)          │
                              │
               ┌──────────────┴──────────────┐
               ▼                             ▼
      Amazon DynamoDB                 Amazon SNS
     (Update Status)             (Email Notification)
               │
               ▼
      Status: CONFIRMED
```



## AWS Services Used

- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- Amazon SQS
- Amazon SNS
- AWS IAM
- Amazon CloudWatch

---

## Workflow

1. Customer places an order through the API.
2. API Gateway invokes the CreateOrder Lambda.
3. Lambda validates the request.
4. Order is stored in DynamoDB with status **PENDING**.
5. Order details are sent to Amazon SQS.
6. OrderProcessor Lambda is triggered automatically.
7. Order status is updated to **CONFIRMED**.
8. Amazon SNS sends an email confirmation.
9. CloudWatch stores logs for monitoring.

---

## Sample Request

```json
{
  "customerName": "Krishna",
  "email": "example@gmail.com",
  "product": "Laptop",
  "quantity": 1,
  "amount": 55000
}
```

---

## Sample Response

```json
{
  "message": "Order Created",
  "orderId": "b4945e20-bedf-436e-8168-2ae8c0afddf0",
  "status": "PENDING"
}
```

---

## DynamoDB Order Lifecycle

Before Processing

```
Status : PENDING
```

After Processing

```
Status : CONFIRMED
```

---

## Features

- Serverless Architecture
- Event-Driven Processing
- Asynchronous Order Processing
- Automatic Email Notifications
- Order Status Tracking
- CloudWatch Logging
- IAM Role-based Security

---

## Screenshots

### API Response

(Add Screenshot)

### DynamoDB (PENDING)

(Add Screenshot)

### DynamoDB (CONFIRMED)

(Add Screenshot)

### SQS Queue

(Add Screenshot)

### SNS Email Notification

(Add Screenshot)

### CloudWatch Logs

(Add Screenshot)

---

## Learning Outcomes

- Building Serverless Applications
- API Gateway Integration
- Lambda Event Processing
- DynamoDB CRUD Operations
- Amazon SQS Queue Processing
- Amazon SNS Notifications
- IAM Role Permissions
- CloudWatch Monitoring

---

## Author

**Krishna Vyas**

AWS Cloud & DevOps Associate

GitHub: https://github.com/<your-github-username>

LinkedIn: https://linkedin.com/in/<your-linkedin-profile>

