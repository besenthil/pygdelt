from modules.processors.processor import Processor
from conf.global_settings import GDELT_ZIP_FILE_EXTENSION_PATTERN, VERBOSE



class GDELTMonthlyProcessor(Processor):

    def __init__(self,start_event_month=None,end_event_month=None):
        self.start_event_month = start_event_month
        self.end_event_month = end_event_month
        self.downloader = None
        self.uploader = None
        self.cdc_handler = None

    def process(self,downloader,uploader,cdc_handler=None):
        self.downloader=downloader
        self.uploader=uploader
        self.cdc_handler = cdc_handler

        if self.cdc_handler:
            self.start_event_month,self.end_event_month = \
                self.cdc_handler._get_next_incremental_date_range()

        for month in range(self.start_event_month,self.end_event_month+1):
            self.process_month(month)

    def process_month (self,file_month):
        file_name = str(file_month) + GDELT_ZIP_FILE_EXTENSION_PATTERN['monthly']

        try:
            response_obj=self.downloader.download(file_name)

            # If successfully downloaded
            self.uploader.upload(file_name,response_obj)

            if self.cdc_handler:
                self.cdc_handler._update_incremental_date(file_month)

            if VERBOSE:
                print ("Finished downloading {}".format(file_month))

            return file_name

        except Exception as excp:

            if VERBOSE:
                print ("Downloading of {} had an issue ".format(file_month))