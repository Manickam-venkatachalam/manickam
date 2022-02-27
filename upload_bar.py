import boto3
s3= boto3.client('s3')
BUCKET_NAME = 'torrentdownload-1'
FILE_NAME = "C:\\Users\\devve_n0wjm5e\\bacholer.mkv"
OBJECT_NAME= FILE_NAME
import os
import sys
import threading
file_size =int(os.path.getsize(FILE_NAME)/1024)/1024
class ProgressPercentage(object):
    
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = (0/1024)/1024
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s mb  (%.2f%%)" % (
                    self._filename, self._seen_so_far, file_size,
                    percentage))
            sys.stdout.flush()


s3.upload_file(
    FILE_NAME, BUCKET_NAME, OBJECT_NAME,
    Callback=ProgressPercentage(FILE_NAME)
)


print("\n file uploaded successfully")