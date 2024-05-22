import boto3

def create_user(user_name):
    try:
        iam = boto3.client('iam')
        # Create IAM user
        iam.create_user(UserName=user_name)
        print(f"IAM user '{user_name}' created.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    user_name = 'Rohit-Patil'  # Replace with your desired username
    create_user(user_name)
