from fileinput import filename
import boto3
import botocore
import os

BUCKET_NAME = 'torrentdownload-1'
FILE_NAME = input("Enter the file name: ")
KEY = input("enter the object name: ")
s3 = boto3.client('s3')
file_size = os.path.getsize(FILE_NAME)
size = (file_size/1024)/1024
print("size of the file is {} mb".format(size))
print("the {} is uploading...".format(FILE_NAME))



s3.upload_file(
    FILE_NAME, BUCKET_NAME, KEY,
    ExtraArgs={'Metadata': {'mykey': 'myvalue'}, 'ACL': 'public-read', 'ContentType': 'image/jpg','Body': 'fileStream'},
)

print("the {} is uploaded sucessfully".format(FILE_NAME))

config = botocore.client.Config(signature_version=botocore.UNSIGNED)
object_url = boto3.client('s3', config=config).generate_presigned_url('get_object', ExpiresIn=36000, Params={'Bucket': BUCKET_NAME, 'Key': KEY})
print(object_url)
