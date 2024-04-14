import boto3

# Specify the AWS region (replace with your desired region)
region_name = "us-east-1"

# Create an EC2 client
ec2_client = boto3.client('ec2', region_name=region_name)

def list_ec2_instances():
  """
  Lists all EC2 instances in the specified region.
  """
  
  try:
    # Get all running EC2 instances
    reservations = ec2_client.describe_instances()
    
    # Print instance details for each reservation
    for reservation in reservations['Reservations']:
      for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        state = instance['State']['Name']
        public_ip = instance.get('PublicIpAddress', 'Not available')  # Check if PublicIpAddress exists
        print(f"Instance ID: {instance_id}")
        print(f"  Type: {instance_type}")
        print(f"  State: {state}")
        print(f"  Public IP: {public_ip}")
        print("")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  list_ec2_instances()
