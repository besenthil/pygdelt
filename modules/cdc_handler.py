import boto3
from boto3.dynamodb.conditions import Key, Attr
from boto3 import resource

from gdelt.conf.global_settings import *
import time

class CDCHandler(object):

    def __init__(self):
        self.dynamodb = None
        if USE_CDC_HANDLER:
            self.dynamodb = boto3.resource('dynamodb',
                                  region_name= REGION_NAME,
                                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
            self.cdc_metadata = self.dynamodb.Table('cdc_metadata')

        if USE_CDC_HANDLER:
            self.end_date = int(time.strftime("%Y%m%d"))

    def _get_next_incremental_date_range(self):
        if USE_CDC_HANDLER:
            gdelt = self.cdc_metadata.get_item(Key={
            'app_name': 'gdelt'
            }
            )
            self.start_date = int(gdelt['Item']['last_extracted_date'])
            self.end_date = int(time.strftime("%Y%m%d"))

        return self.start_date,self.end_date

    def _update_incremental_date(self,next_date):
        if USE_CDC_HANDLER:
            self.cdc_metadata.update_item(Key = {
                 'app_name': 'gdelt'
            },
                    UpdateExpression='SET last_extracted_date = :val1',
                    ExpressionAttributeValues={
                        ':val1': next_date
                    }
            )
