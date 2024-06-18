import boto3
import json
import os
import requests
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    sts = boto3.client('sts')
    webhook_url = os.environ['WEBHOOK_URL']
    
    # Get AWS account ID and region
    account_id = sts.get_caller_identity()["Account"]
    region = ec2.meta.region_name
    
    # Describe all EBS volumes
    volumes = ec2.describe_volumes()
    
    volumes_found = False
    volume_details = []

    for volume in volumes['Volumes']:
        # Check if the volume is in 'available' state, meaning it's unused
        if volume['State'] == 'available':
            # Get the current time
            current_time = datetime.now(timezone.utc)
            # Get the volume creation time
            creation_time = volume['CreateTime']
            # Calculate the age of the volume
            age = current_time - creation_time
            
            if age > timedelta(days=15):
                volumes_found = True
                # Append volume details to the list
                volume_details.append({
                    "VolumeId": volume['VolumeId'],
                    "Size": volume['Size'],
                    "CreationTime": creation_time.strftime('%Y-%m-%d %H:%M:%S'),
                    "AgeDays": age.days
                })

    if volumes_found:
        # Construct the message payload for Google Chat
        message = {
            "text": (
                f"Unused EBS volumes older than 15 days found in account {account_id}, region {region}:\n" +
                "\n".join(
                    [f"VolumeId: {v['VolumeId']}, Size: {v['Size']} GiB, CreationTime: {v['CreationTime']}, Age: {v['AgeDays']} days"
                     for v in volume_details]
                )
            )
        }
        try:
            response = requests.post(webhook_url, headers={'Content-Type': 'application/json'}, data=json.dumps(message))
            if response.status_code != 200:
                raise ValueError(f"Request to Google Chat returned an error {response.status_code}, the response is: {response.text}")
        except Exception as e:
            print(f"Error sending notification to Google Chat: {e}")
    else:
        print("No unused EBS volumes older than 15 days found.")

    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent to Google Chat!')
    }
