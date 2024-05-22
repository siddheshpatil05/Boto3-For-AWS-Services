import boto3

def delete_file(bucket_name, object_name):
    try:
        s3 = boto3.client('s3')
        # Delete a file from S3 bucket
        s3.delete_object(Bucket=bucket_name, Key=object_name)
        print(f"File '{object_name}' deleted from '{bucket_name}'.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    bucket_name = 'siddhesh-01052024'  # Replace with your bucket name
    object_name = 'file.png'  # Replace with the object name in the bucket
    delete_file(bucket_name, object_name)
