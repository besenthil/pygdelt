from modules.processor import *
from modules.uploader import *
from modules.downloader import *

daily_downloader = DailyProcessor(Uploader=LocalFileSystemUploader())
daily_downloader.process(start_event_date=20171101,
                         end_event_date=20171130)

