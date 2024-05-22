import boto3

def delete_bucket(bucket_name):
    try:
        s3 = boto3.client('s3')
        # Delete S3 bucket
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    bucket_name = 'siddhesh-01052024'  # Replace with your bucket name
    delete_bucket(bucket_name)
