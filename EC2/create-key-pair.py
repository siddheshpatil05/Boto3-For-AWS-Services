import boto3

def create_key_pair(ec2, key_name):
    try:
        # Create a new key pair
        key_pair = ec2.create_key_pair(KeyName=key_name)
        print(f"Key pair '{key_name}' created.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    # Initialize the EC2 client
    ec2 = boto3.client('ec2')

    # Key pair name
    key_name = 'Rashmi-key-Pair'

    # Create key pair
    create_key_pair(ec2, key_name)

if __name__ == "__main__":
    main()
