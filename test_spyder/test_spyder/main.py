from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.quotes import QuotesSpider
from connect import connect_to_db

connect_to_db()

def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(QuotesSpider)
    process.start()

if __name__ == '__main__':
    run_spider()