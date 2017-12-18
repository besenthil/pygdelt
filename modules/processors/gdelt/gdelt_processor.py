from conf.global_settings import USE_CDC_HANDLER


from modules.processors.processor import Processor
from modules.downloader import Downloader
from modules.uploader import LocalFileSystemUploader
from modules.cdc_handler import CDCHandler


class GDELTProcessor(Processor):

    def __init__(
            self,
            Downloader=Downloader(),
            Uploader=LocalFileSystemUploader()
    ):
        self.downloader = Downloader
        self.uploader = Uploader
        self.cdc_handler = None

        if USE_CDC_HANDLER:
            self.cdc_handler = CDCHandler()

    def process(self,processor_type):
        processor_type.process(self.downloader,self.uploader,self.cdc_handler)




