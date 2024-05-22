import boto3

def attach_user_to_group(user_name, group_name):
    try:
        iam = boto3.client('iam')
        # Attach user to group
        iam.add_user_to_group(UserName=user_name, GroupName=group_name)
        print(f"IAM user '{user_name}' attached to group '{group_name}'.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    user_name = 'Rohit-Patil'  # Replace with the username
    group_name = 'Cloud-GRP'  # Replace with the group name
    attach_user_to_group(user_name, group_name)
