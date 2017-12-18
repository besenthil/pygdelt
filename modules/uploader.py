from conf.global_settings import *
import boto3

import io

class Uploader(object):
    def __init__(self):
        pass

    def upload(self):
        pass

class s3Uploader(Uploader):

    def __init__(self):
        self.s3_conn = boto3.resource('s3',
                                    region_name= REGION_NAME,
                                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    def upload(self,key_name,response_obj):
        self.s3_conn.Bucket(BUCKET_NAME).put_object(Key=KEY_PREFIX + key_name, Body=io.BytesIO(response_obj.content))

class LocalFileSystemUploader(Uploader):

    def __init__(self):
        pass

    def upload(self,file_name,response_obj):
        with open(DOWNLOAD_DIRECTORY+str(file_name), 'wb') as f:
                for block in response_obj.iter_content(1024):
                    f.write(block)
