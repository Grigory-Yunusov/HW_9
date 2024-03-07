# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class TestSpyderPipeline:
#     def process_item(self, item, spider):
#         return item

import json
from connect import connect_to_db

connect_to_db()

class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.quotes_file = open('quotes.json', 'w')
        self.authors_file = open('authors.json', 'w')
        self.quotes_data = []
        self.authors_data = []

    def close_spider(self, spider):
        self.quotes_file.write(json.dumps(self.quotes_data, indent=4))
        self.quotes_file.close()
        self.authors_file.write(json.dumps(self.authors_data, indent=4))
        self.authors_file.close()

    def process_item(self, item, spider):
        if 'fullname' in item:
            self.authors_data.append(dict(item))
        else:
            self.quotes_data.append(dict(item))
        return item
