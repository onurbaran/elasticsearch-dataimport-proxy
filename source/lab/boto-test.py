__author__ = 'onurbaran'
import boto
import sys, os
from boto.s3.key import Key

LOCAL_PATH = '/backup/s3/'
AWS_ACCESS_KEY_ID = '...'
AWS_SECRET_ACCESS_KEY = '...'

bucket_name = 'bucket_name'
# connect to the bucket
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket(bucket_name)
# go through the list of files
bucket_list = bucket.list()

for l in bucket_list:
    keyString = str(l.key)

    if not os.path.exists(LOCAL_PATH+keyString):
        l.get_contents_to_filename(LOCAL_PATH+keyString)
