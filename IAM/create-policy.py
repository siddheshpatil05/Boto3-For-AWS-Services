import boto3

def create_policy(policy_name, policy_document):
    try:
        iam = boto3.client('iam')
        # Create IAM policy
        iam.create_policy(PolicyName=policy_name, PolicyDocument=policy_document)
        print(f"IAM policy '{policy_name}' created.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    policy_name = 's3-policy'  # Replace with your desired policy name
    policy_document = '{"Version": "2012-10-17","Statement": [{"Effect": "Allow","Action": "s3:*","Resource": "*"}]}'  # Replace with your policy document
    create_policy(policy_name, policy_document)
