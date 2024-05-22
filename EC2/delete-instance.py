import boto3

def delete_ec2_instance(ec2, instance_id):
    # Terminate EC2 instance
    response = ec2.terminate_instances(
        InstanceIds=[instance_id]
    )
    
    print(f"Instance '{instance_id}' terminated.")

def main():
    # Initialize the EC2 client
    ec2 = boto3.client('ec2')

    # Instance ID of the instance you want to delete
    instance_id = 'i-05eeecb2578662d3a'  # Example instance ID, replace with your actual instance ID

    # Delete EC2 instance
    delete_ec2_instance(ec2, instance_id)

if __name__ == "__main__":
    main()
