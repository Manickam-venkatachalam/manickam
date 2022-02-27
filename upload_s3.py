from fileinput import filename
import boto3
import botocore
import os
from mysql_connect import *
from s3files import *
s3 = boto3.client('s3')
BUCKET_NAME = manickam()
FILE_NAME = input("Enter the file name: ")
file_name = os.path.basename(FILE_NAME)
print ("press 1 to give a new name or press anykey to use the default name")
object_name = (input("enter the number: "))

if object_name == '1':
    KEY = input("enter the object name: ")
else : 
    a_string = file_name
    KEY = a_string.replace(" ", "_")

print(KEY)
file_size = os.path.getsize(FILE_NAME)
size = (file_size/1024)/1024
print("size of the file is {} mb".format(size))
print("the {} is selected".format(file_name))

print("1: binary/octet-stream")
print("2: image/png")
print("3: image/jpg")
print("4: image/gif")
print("5: image/bmp")
print("6: image/tiff")
print("7: svg+xml")
print("8: text/plain")
print("9: text/rtf")
print("10: application/msword")
print("11: application/zip")
print("12: audio/mpeg")
print("13: application/pdf")
print("14: application/x-gzip")
print("15: application/x-compressed")
print("if you want to upload other file type then enter the file type by pressing 'enter key'")

contentType = int(input("select the file format from the above list: "))

if contentType == 1:
    contentType = 'binary/octet-stream'
    
elif contentType == 2:
    contentType = 'image/png'
    
elif contentType == 3:
    contentType = "image/jpg"

elif contentType == 4:
    contentType = "image/gif"

elif contentType == 5:
    contentType = "image/bmp"

elif contentType == 6:
    contentType = "image/tiff"

elif contentType == 7:
    contentType = "svg+xml"

elif contentType == 8:
    contentType = "text/plain"

elif contentType == 9:
    contentType = "text/rtf"

elif contentType == 10:
    contentType = "application/msword"

elif contentType == 11:
    contentType = "application/zip"

elif contentType == 12:
    contentType = "audio/mpeg"

elif contentType == 13:
    contentType = "application/pdf"

elif contentType == 14:
    contentType = "application/x-gzip"

elif contentType == 15:
    contentType = "application/x-compressed"

elif contentType == 16:
    contentType = "application/vnd.android.package-archive"

else:
    contentType = input("enter the custom input: ")

print ("You entered: ", contentType)


print("1: private")
print("2: public-read")
print("3: public-read-write")
print("4: aws-exec-read")
print("5: authenticated-read")
print("6: bucket-owner-read	")
print("7: bucket-owner-full-control")
print("8: log-delivery-write")
print("if u need detailed explination about this one click the following line /n  https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl")

file_type= int(input("enter the file permission of that object: "))

if file_type == 1:
    file_type = 'private'
elif file_type == 2:
    file_type = 'public-read'
elif file_type == 3:
   file_type = 'public-read-write' 
elif file_type == 4:
    file_type = 'aws-exec-read'
elif file_type == 5:
    file_type = 'authenticated-read'
elif file_type == 6:
  file_type = 'bucket-owner-read'
elif file_type == 7:
    file_type = 'bucket-owner-full-control'
elif file_type == 8:
   file_type = 'log-delivery-write'
else: 
   print("plese enter the valid input")

s3.upload_file(
    FILE_NAME, BUCKET_NAME, KEY,
    ExtraArgs={'Metadata': {'mykey': 'myvalue'}, 'ACL': file_type, 'ContentType' : contentType},
)

print("the {} is uploaded sucessfully".format(FILE_NAME))

config = botocore.client.Config(signature_version=botocore.UNSIGNED)
object_url = boto3.client('s3', config=config).generate_presigned_url('get_object', ExpiresIn=36000, Params={'Bucket': BUCKET_NAME, 'Key': KEY})
print(object_url)

print("press 1 to store the value to mysql")
mySqlSelector = (input("enter the value of the mysql database: "))
if mySqlSelector == '1':
        s3_mysql(KEY, object_url, file_size, file_name)
        
else :
    print("ok bye")


