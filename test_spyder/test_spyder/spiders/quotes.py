import scrapy
from scrapy.crawler import CrawlerProcess
from items import QuoteItem, AuthorItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['tags'] = quote.css('div.tags a.tag::text').getall()
            item['quote'] = quote.css('span.text::text').get()
            item['author'] = quote.css('small.author::text').get()
            yield item

            author_url = response.urljoin(quote.css('small.author + a::attr(href)').get())
            request = scrapy.Request(author_url, callback=self.parse_author)
            request.meta['item'] = item
            yield request

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        item = response.meta['item']
        author_item = AuthorItem()
        author_item['fullname'] = response.css('h3.author-title::text').get().strip()
        author_item['born_date'] = response.css('span.author-born-date::text').get().strip()
        author_item['born_location'] = response.css('span.author-born-location::text').get().strip()
        author_item['description'] = response.css('div.author-description::text').get().strip()
        item['author'] = author_item
        yield item