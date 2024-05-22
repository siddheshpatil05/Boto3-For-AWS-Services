import boto3

def delete_user(user_name):
    try:
        iam = boto3.client('iam')
        # Delete IAM user
        iam.delete_user(UserName=user_name)
        print(f"IAM user '{user_name}' deleted.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    user_name = 'Rohit-Patil'  # Replace with the username you want to delete
    delete_user(user_name)
