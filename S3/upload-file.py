import boto3
import os

def upload_file(bucket_name, file_path, object_name=None):
    try:
        s3 = boto3.client('s3')
        # If object_name is not specified, use file name
        if object_name is None:
            object_name = os.path.basename(file_path)
        # Upload a file to S3 bucket
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded to '{bucket_name}' as '{object_name}'.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    bucket_name = 'siddhesh-01052024'  # Replace with your bucket name
    file_path = '/Users/siddheshpatil/Downloads/file.png'  # Replace with your local file path
    upload_file(bucket_name, file_path)
