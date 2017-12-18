from modules.processors.processor import Processor
from conf.global_settings import GDELT_ZIP_FILE_EXTENSION_PATTERN, VERBOSE

class GDELTDailyProcessor(Processor):

    def __init__(self,start_event_date=None,end_event_date=None):
        self.start_event_date = start_event_date
        self.end_event_date = end_event_date
        self.downloader = None
        self.uploader = None
        self.cdc_handler = None

    def process(self,downloader,uploader,cdc_handler=None):
        self.downloader=downloader
        self.uploader=uploader
        self.cdc_handler = cdc_handler

        if self.cdc_handler:
            self.start_event_date,self.end_event_date = \
                self.cdc_handler._get_next_incremental_date_range()

        for day in range(self.start_event_date,self.end_event_date+1):
                self.process_day(day)

    def process_day (self,file_date):
        file_name = str(file_date) + GDELT_ZIP_FILE_EXTENSION_PATTERN['daily']

        response_obj=self.downloader.download(file_name)

        # If successfully downloaded
        if type(response_obj) == 'Response':
            self.uploader.upload(file_name,response_obj)

        if self.cdc_handler:
            self.cdc_handler._update_incremental_date(file_date)

        if VERBOSE:
            print ("Finished downloading {}".format(file_date))

        return file_name