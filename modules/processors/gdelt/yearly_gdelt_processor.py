from modules.processors.processor import Processor
from conf.global_settings import GDELT_ZIP_FILE_EXTENSION_PATTERN, VERBOSE


class GDELTYearlyProcessor(Processor):

    def __init__(self,start_event_year=None,end_event_year=None):
        self.start_event_year = start_event_year
        self.end_event_year = end_event_year
        self.downloader = None
        self.uploader = None
        self.cdc_handler = None

    def process(self,downloader,uploader,cdc_handler=None):
        self.downloader=downloader
        self.uploader=uploader
        self.cdc_handler = cdc_handler

        if self.cdc_handler:
            self.start_event_year,self.end_event_year = \
                self.cdc_handler._get_next_incremental_date_range()

        for year in range(self.start_event_year,self.end_event_year+1):
            self.process_month(year)

    def process_month (self,file_year):
        file_name = str(file_year) + GDELT_ZIP_FILE_EXTENSION_PATTERN['yearly']

        try:
            response_obj=self.downloader.download(file_name)

            # If successfully downloaded
            self.uploader.upload(file_name,response_obj)

            if self.cdc_handler:
                self.cdc_handler._update_incremental_date(file_year)

            if VERBOSE:
                print ("Finished downloading {}".format(file_year))

            return file_name

        except Exception as excp:

            if VERBOSE:
                print ("Downloading of {} had an issue ".format(file_year))