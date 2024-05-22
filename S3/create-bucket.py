import boto3

def create_bucket(bucket_name, region=None):
    try:
        s3 = boto3.client('s3')
        # Create S3 bucket
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
        print(f"Bucket '{bucket_name}' created.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    bucket_name = 'siddhesh-01052024'  # Replace with your bucket name
    create_bucket(bucket_name)
