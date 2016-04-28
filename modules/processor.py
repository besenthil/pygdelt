from gdelt.conf.global_settings import *
import requests
from gdelt.modules.cdc_handler import CDCHandler
from gdelt.modules.downloader import Downloader
from gdelt.modules.uploader import s3Uploader,LocalFileSystemUploader


class DailyProcessor(object):
    def __init__(self,Downloader=Downloader(),Uploader=s3Uploader()):
        self.downloader = Downloader
        self.uploader = Uploader

        if USE_CDC_HANDLER:
            self.cdc_handler = CDCHandler()

    def process(self,start_event_date=None,end_event_date=None):
            if USE_CDC_HANDLER:
                start_event_date,end_event_date = self.cdc_handler._get_next_incremental_date_range()

            for file_date in range(start_event_date+1,end_event_date):
                file_name = str(file_date) + GDELT_ZIP_FILE_EXTENSION_PATTERN

                response_obj=self.downloader.download(file_name)
                item_size = int(response_obj.headers['x-goog-stored-content-length'])

                if response_obj.status_code == requests.codes.ok and item_size < TOO_LONG_IN_MB:
                    self.uploader.upload(file_name,response_obj)
                if USE_CDC_HANDLER:
                    self.cdc_handler._update_incremental_date(file_date)