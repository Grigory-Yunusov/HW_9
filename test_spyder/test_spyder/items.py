# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from connect import connect_to_db

connect_to_db()

class TestSpyderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QuoteItem(scrapy.Item):
    tags = scrapy.Field()
    author = scrapy.Field()
    quote = scrapy.Field()


class AuthorItem(scrapy.Item):
    fullname = scrapy.Field()
    born_date = scrapy.Field()
    born_location = scrapy.Field()
    description = scrapy.Field()


class ContactItem(scrapy.Item):
    full_name = scrapy.Field()
    email = scrapy.Field()
    nitfed = scrapy.Field()