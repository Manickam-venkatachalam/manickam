from sre_constants import SUCCESS
import string
import boto3
import botocore
BUCKET_NAME = 'torrentdownload-1'
KEY = 'muthukarthi.png'
FILE_NAME = input('Enter the file name: ')

# client = boto3.client('s3')

s3 = boto3.client('s3')
# response = s3.list_buckets()
# print('existing buckets: ', response['Buckets'])
import os
import sys
import threading

class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()

from botocore.exceptions import ClientError
import logging

# To upload a file to s3 bucket 
s3.upload_file(
    FILE_NAME, BUCKET_NAME, KEY,
    ExtraArgs={'ACL': 'public-read'},
    # callback= ProgressPercentage(FILE_NAME)
)
# def upload_file(file_name, bucket, object_name=None):
#  if FILE_NAME is None:
#         object_name = os.path.basename(FILE_NAME)
        
#  try:
#         response = s3.upload_file(file_name, bucket, object_name)
#  except ClientError as e:
#         logging.error(e)
#         return False
#  return True

# print ('SUCCESS')

#To download a file from s3 bucket
# s3 = boto3.resource('s3')

# s3.Bucket(BUCKET_NAME).download_file(KEY, FILE_NAME)

# print('success')


# import os
# import sys
# import threading

# class ProgressPercentage(object):

#     def __init__(self, filename):
#         self._filename = filename
#         self._size = float(os.path.getsize(filename))
#         self._seen_so_far = 0
#         self._lock = threading.Lock()

#     def __call__(self, bytes_amount):
#         # To simplify, assume this is hooked up to a single filename
#         with self._lock:
#             self._seen_so_far += bytes_amount
#             percentage = (self._seen_so_far / self._size) * 100
#             sys.stdout.write(
#                 "\r%s  %s / %s  (%.2f%%)" % (
#                     self._filename, self._seen_so_far, self._size,
#                     percentage))
#             sys.stdout.flush()