import boto3
from datetime import datetime, timedelta

def generate_usage_report(start_date, end_date):
    # Initialize the Cost Explorer client
    ce_client = boto3.client('ce', region_name='us-east-1')  # Replace 'us-east-1' with your desired AWS region

    # Format dates
    start = start_date.strftime('%Y-%m-%d')
    end = end_date.strftime('%Y-%m-%d')

    # Define the request parameters
    request_params = {
        'TimePeriod': {
            'Start': start,
            'End': end
        },
        'Granularity': 'DAILY',  # Can be DAILY, MONTHLY, or HOURLY
        'Metrics': ['BlendedCost']  # Can include additional metrics such as UnblendedCost, UsageQuantity, etc.
    }

    # Get the usage data
    try:
        response = ce_client.get_cost_and_usage(**request_params)
        print("Usage report generated successfully:")
        print(response)
    except Exception as e:
        print(f"Error generating usage report: {str(e)}")

# Example usage:
if __name__ == "__main__":
    # Define the start and end dates for the report
    start_date = datetime.now() - timedelta(days=7)  # Start date (7 days ago)
    end_date = datetime.now()  # End date (today)

    # Generate the usage report
    generate_usage_report(start_date, end_date)
