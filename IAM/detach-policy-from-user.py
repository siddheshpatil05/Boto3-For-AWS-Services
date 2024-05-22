import boto3

def detach_policy_from_user(policy_arn, user_name):
    try:
        iam = boto3.client('iam')
        # Detach policy from user
        iam.detach_user_policy(UserName=user_name, PolicyArn=policy_arn)
        print(f"IAM policy '{policy_arn}' detached from user '{user_name}'.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    policy_arn = 'arn:aws:iam::705231325387:policy/s3-policy'  # Replace with the ARN of the policy
    user_name = 'Rohit-Patil'  # Replace with the username
    detach_policy_from_user(policy_arn, user_name)
