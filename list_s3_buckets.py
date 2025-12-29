import boto3

# Uses IAM credentials from environment variables or AWS CLI profile
# Never hard-code keys into code.

def list_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()

    print("Your S3 buckets:")
    for bucket in response["Buckets"]:
        print(f"- {bucket['Name']}")

if __name__ == "__main__":
    list_buckets()
