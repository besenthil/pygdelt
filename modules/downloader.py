# coding=utf-8
"""
# Copyright 2016 Senthilkumar Bala. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
"""

from conf.global_settings import PROXY_SERVERS,DOWNLOAD_TIME_OUT,GDELT_URL,TOO_LONG_IN_MB
import requests


class Downloader(object):

    def __init__(self):
        self.url = GDELT_URL
        self.response_obj = None

    def download(self,file_name):
        self.response_obj = requests.get(self.url + str(file_name),
                                                proxies=PROXY_SERVERS,
                                                stream=True,
                                                timeout=DOWNLOAD_TIME_OUT)

        item_size = int(self.response_obj.headers['x-goog-stored-content-length'])

        if self.response_obj.status_code == requests.codes.ok and \
                        item_size < TOO_LONG_IN_MB:
            return self.response_obj
        else:
            return requests.RequestException \
                    ("Failed to download : Error code {}".format(self.response_obj.status_code))








