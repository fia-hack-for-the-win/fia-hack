from troposphere import GetAtt, Join, Template
from troposphere.s3 import Bucket
from troposphere.kinesis import Stream
from troposphere.awslambda import Code, Function


class CloudFormationTemplate(object):

    def __init__(self):
        self.template = Template()
        self.template.add_description('Creating Stack for FIA Hackathon')

        self.template.add_resource(Bucket(
            'fiaHackathonS3Bucket',
            BucketName='fia-hackathon',
            AccessControl='PublicRead'
        ))

        self.template.add_resource(Stream(
            'fiaHackathonKinesisStream',
            ShardCount=5
        ))

        with open('lambda_f1.py', 'r') as code_f1_file:
            code_f1_array = code_f1_file.readlines()

        self.template.add_resource(Function(
            'sendRequestDataToKinesis',
            Code=Code(
                ZipFile=Join("", code_f1_array)
            ),
            Description='Function to get request, and send it to Kinesis',
            Handler='lambda_function.lambda_handler',
            Role=GetAtt("LambdaExecutionRole", "Arn"),
            Runtime='python'
        ))

    def print_template(self):
        print self.template.to_json()

if __name__ == '__main__':
    CloudFormationTemplate().print_template()
