import json
import urllib3
import boto3

from datetime import datetime

ec2 = boto3.client('ec2')


http = urllib3.PoolManager()

# Google Chat webhook URL
GOOGLE_CHAT_WEBHOOK_URL = 'CHAT_WEBHOOK_URL'

def send_message_to_google_chat(message):
    headers = {
        'Content-Type': 'application/json; charset=UTF-8'
    }
    body = {
        'text': message
    }
    encoded_body = json.dumps(body).encode('utf-8')
    response = http.request('POST', GOOGLE_CHAT_WEBHOOK_URL, body=encoded_body, headers=headers)
    return response

def lambda_handler(event, context):
    print(event['Records'])
    for record in event['Records']:
        sns_message = json.loads(record['Sns']['Message'])
        detail = sns_message['detail']
        instance_id = detail['instance-id']
        instance_action = detail.get('instance-action', 'none')
        state = 'interrupted' if instance_action in ['terminate', 'stop', 'hibernate'] else 'unknown'
        timestamp = sns_message['time']
        tags = get_instance_tags(instance_id)

        if detail_type == 'EC2 Spot Instance Interruption Warning':
            if tags.get('Environment') == 'Development':
                message = f"EC2 Spot Instance {instance_id} is being interrupted (action: {instance_action}) at {timestamp}."
            else:
                continue
        elif detail_type == 'EC2 Spot Instance Request Fulfillment' and state == 'running':
            if tags.get('Environment') == 'Development':
                message = f"EC2 Spot Instance {instance_id} is running again in Development at {timestamp}."
            else:
                continue

        response = send_message_to_google_chat(message)
        print(response.status, response.data)

    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to Google Chat successfully!')
    }
