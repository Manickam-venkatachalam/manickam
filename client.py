import os
import boto3

session = boto3.session.Session()
client = session.client('s3',
                        region_name='sgp1',
                        endpoint_url='https://torrentdownload.sgp1.digitaloceanspaces.com',
                        aws_access_key_id=os.getenv('SPACES_KEY'),
                        aws_secret_access_key=os.getenv('SPACES_SECRET'))



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

contentType = int(input("select the file format : "))

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
