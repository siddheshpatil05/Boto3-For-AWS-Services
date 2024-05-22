import boto3

def create_group(group_name):
    try:
        iam = boto3.client('iam')
        # Create IAM group
        iam.create_group(GroupName=group_name)
        print(f"IAM group '{group_name}' created.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    group_name = 'Cloud-GRP'  # Replace with your desired group name
    create_group(group_name)
