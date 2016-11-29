import json
import logging
import pymysql
import sys

# rds settings
rds_host = "fia-hack.cluster-clbxdqdbb51w.us-west-2.rds.amazonaws.com"
name = "sqlmaster"
password = "mastersql"
db_name = "fia_hackdb"
db_port = 3306

logger = logging.getLogger()
logger.setLevel(logging.INFO)
try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, port=db_port)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    """
    This function inserts content from mysql RDS instance
    """

    params = json.loads(event['body'])
    name = params['name']
    phone = params['phone']
    zip_code = params['zip_code']
    twitter = params['twitter']
    email = params['email']
    comment = params['comment']

    with conn.cursor() as cur:
        cur.execute('insert into user_details (name, phone_no, zipcode, Twitter, Email, Comments) values("{0}", "{1}", "{2}", "{3}", "{4}", "{5}")'.format(name, phone, zip_code, twitter, email, comment))
        conn.commit()

    return respond(None, 'User successfully added')
