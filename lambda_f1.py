import boto3
import json
sns = boto3.client('sns')

print('Loading function')

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    #sns = boto3.client('sns')
    
    print("Received event: " + json.dumps(event, indent=2))
    try:
        body = json.loads(event['body'])
        msg = body['Key1']
        try:
            number = '+1' + body['Key2']
        except:
            number = '+17322667762'
        print body
        response = sns.publish(PhoneNumber = number, Message=msg)
        print response
        return respond('', body)
    except Exception as e:
        print e
        raise e
