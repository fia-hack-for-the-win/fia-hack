from troposphere import Template
from troposphere.s3 import Bucket


class CloudFormationTemplate(object):

    def __init__(self):
        self.template = Template()
        self.template.add_description('Creating Stack for FIA Hackathon')

        self.template.add_resource(Bucket(
            'fiaHackathon',
            BucketName='fia-hackathon',
            AccessControl='PublicRead'
        ))

    def print_template(self):
        print self.template.to_json()

if __name__ == '__main__':
    CloudFormationTemplate().print_template()
