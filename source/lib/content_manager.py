__author__ = 'onurbaran'

import boto
import sys, os
from boto.s3.key import Key
from source.config.content_manager import content_local_importer_config as config
from source.actors.Base import Importer

class ContentLocalImporter(object):

    def __init__(self):
        conn = boto.connect_s3(config['aws_access_key'], config['aws_secret_key'])
        self.bucket = conn.get_bucket(config['s3_bucket_name'])
        self.new_content_notifier = Importer()
        self.new_content_notifier.start()

    def get_content_list(self):
        return self.bucket.list()

    def download_files(self):
        contents = self.get_content_list()
        for content in contents:
            keyString = str(content.key)
            if not os.path.exists(config['download_path']+keyString):
                content.get_contents_to_filename(config['download_path']+keyString)
                self.new_content_notifier.inbox.put(config['download_path']+keyString)
