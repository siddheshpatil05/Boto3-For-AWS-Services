import boto3

def detach_user_from_group(user_name, group_name):
    try:
        iam = boto3.client('iam')
        # Detach user from group
        iam.remove_user_from_group(UserName=user_name, GroupName=group_name)
        print(f"IAM user '{user_name}' detached from group '{group_name}'.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    user_name = 'Rohit-Patil'  # Replace with the username
    group_name = 'Cloud-GRP'  # Replace with the group name
    detach_user_from_group(user_name, group_name)
