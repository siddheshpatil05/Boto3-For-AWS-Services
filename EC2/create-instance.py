import boto3

def create_ec2_instance(ec2, key_name, instance_type, image_id, subnet_id):
    # Create EC2 instance
    response = ec2.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SubnetId=subnet_id,
        MinCount=1,
        MaxCount=1
    )
    
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Instance '{instance_id}' created.")

def main():
    # Initialize the EC2 client
    ec2 = boto3.client('ec2')

    # Key pair name (ensure this key pair exists in your AWS account)
    key_name = 'Rashmi-key-Pair'

    # Instance type and AMI ID
    instance_type = 't2.micro'  # Example instance type, choose according to your needs
    image_id = 'ami-07caf09b362be10b8'  # Example AMI ID, choose according to your needs

    # Specify the subnet ID (replace 'subnet-1234567890abcdef0' with your subnet ID)
    subnet_id = 'subnet-0696838481bc1dd05'

    # Create EC2 instance
    create_ec2_instance(ec2, key_name, instance_type, image_id, subnet_id)

if __name__ == "__main__":
    main()
