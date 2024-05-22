import boto3

def attach_policy_to_user(policy_arn, user_name):
    try:
        iam = boto3.client('iam')
        # Attach policy to user
        iam.attach_user_policy(UserName=user_name, PolicyArn=policy_arn)
        print(f"IAM policy '{policy_arn}' attached to user '{user_name}'.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    policy_arn = 'arn:aws:iam::705231325387:policy/s3-policy'  # Replace with the ARN of the policy
    user_name = 'Rohit-Patil'  # Replace with the username
    attach_policy_to_user(policy_arn, user_name)
