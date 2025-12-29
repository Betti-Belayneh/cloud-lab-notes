# Cloud Lab Notes

This repository documents my hands-on practice with AWS cloud services.  
I completed structured labs focused on configuring secure resources, troubleshooting permissions, and deploying test environments.

## Topics Covered
- EC2: launch, connect, stop/start instances
- S3: create buckets, upload/download files, lifecycle rules
- IAM: users, roles, policies, least-privilege
- Billing basics and cost awareness
- Basic Linux commands in cloud environments

## Demo Script
The `list_s3_buckets.py` script demonstrates how to connect to AWS using IAM credentials and list available S3 buckets.

> Credentials are **never** stored in code. I used environment variables and IAM best practices.

## Run the Script

1. Install boto3:


2. Configure AWS CLI (one time):


3. Run:

