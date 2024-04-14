import boto3

def list_ec2_instances():
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2', region_name='us-east-1')  # Replace 'us-east-1' with your desired AWS region

    # Get a list of all EC2 instances
    try:
        response = ec2_client.describe_instances()
        instances = []

        # Extract instance information from the response
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_state = instance['State']['Name']
                instance_type = instance['InstanceType']
                instance_public_ip = instance.get('PublicIpAddress', 'N/A')
                instance_private_ip = instance.get('PrivateIpAddress', 'N/A')
                instances.append({
                    'InstanceID': instance_id,
                    'State': instance_state,
                    'Type': instance_type,
                    'PublicIP': instance_public_ip,
                    'PrivateIP': instance_private_ip
                })

        # Print the list of instances
        print("List of EC2 instances:")
        for instance in instances:
            print(f"Instance ID: {instance['InstanceID']}, State: {instance['State']}, Type: {instance['Type']}, "
                  f"Public IP: {instance['PublicIP']}, Private IP: {instance['PrivateIP']}")
    except Exception as e:
        print(f"Error listing EC2 instances: {str(e)}")

# Example usage:
if __name__ == "__main__":
    list_ec2_instances()
