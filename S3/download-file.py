import boto3

def download_file(bucket_name, object_name, file_path):
    try:
        s3 = boto3.client('s3')
        # Download a file from S3 bucket
        s3.download_file(bucket_name, object_name, file_path)
        print(f"File '{object_name}' downloaded from '{bucket_name}' to '{file_path}'.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    bucket_name = 'siddhesh-01052024'  # Replace with your bucket name
    object_name = 'file.png'  # Replace with the object name in the bucket
    file_path = '/Users/siddheshpatil/Downloads/file.png'  # Replace with your local file path
    download_file(bucket_name, object_name, file_path)
