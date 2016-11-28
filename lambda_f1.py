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
    number = '+17322667762'
    print("Received event: " + json.dumps(event, indent=2))
    try:
        body = json.loads(event['body'])
        body = body['Key1']
        print body
        response = sns.publish(PhoneNumber = number, Message=body)
        print response
        #statusCode = '200'
        #headers = response['ResponseMetadata']['HTTPHeaders']
        #apigResponse = {'statusCode': statusCode, 'body': json.dumps(response), 'headers': headers}
        #print event
        #print 'body ' + body
        #return apigResponse #['ResponseMetadata'] #['HTTPHeaders']['content-type']
        
        return respond('', body)
    except Exception as e:
        print e
        raise e
