import scrapy
from scrapy.crawler import CrawlerProcess
from items import QuoteItem, AuthorItem
from connect import connect_to_db

connect_to_db()

# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'
#     start_urls = ['http://quotes.toscrape.com']

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             item = QuoteItem()
#             item['tags'] = quote.css('div.tags a.tag::text').getall()
#             item['quote'] = quote.css('span.text::text').get()
#             item['author'] = quote.css('small.author::text').get()
#             yield item

#             author_url = response.urljoin(quote.css('small.author + a::attr(href)').get())
#             request = scrapy.Request(author_url, callback=self.parse_author)
#             request.meta['item'] = item
#             yield request

#         next_page = response.css('li.next a::attr(href)').get()
#         if next_page is not None:
#             yield response.follow(next_page, self.parse)

#     def parse_author(self, response):
#         item = response.meta['item']
#         author_item = AuthorItem()
#         author_item['fullname'] = response.css('h3.author-title::text').get().strip()
#         author_item['born_date'] = response.css('span.author-born-date::text').get().strip()
#         author_item['born_location'] = response.css('span.author-born-location::text').get().strip()
#         author_item['description'] = response.css('div.author-description::text').get().strip()
#         item['author'] = author_item
#         yield item


class QuotesSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
 
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                "tags": quote.css('div.tags a.tag::text').extract(),
                "author": quote.css('span small.author::text').extract_first(),
                "quote": quote.css('span.text::text').get()
            }

            author_url = response.urljoin(quote.css('span a::attr(href)').extract_first())
            yield scrapy.Request(author_url, callback=self.parse_author)

        next_link = response.css('li.next a::attr(href)').get()
        if next_link:
            yield scrapy.Request(url=response.urljoin(next_link), callback=self.parse)

    def parse_author(self, response):
        yield {
            "fullname": response.css('h3.author-title::text').extract_first().strip(),
            "born_date": response.css('span.author-born-date::text').extract_first().strip(),
            "born_location": response.css('span.author-born-location::text').extract_first().strip(),
            "description": response.css('div.author-description::text').extract_first().strip()
        }


# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'
#     start_urls = ['http://quotes.toscrape.com']

#     def parse(self, response):
#         for quote in response.xpath('//div[@class="quote"]'):
#             item = QuoteItem()
#             item['tags'] = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
#             item['quote'] = quote.xpath('.//span[@class="text"]/text()').get()
#             item['author'] = quote.xpath('.//small[@class="author"]/text()').get()
#             yield item

#             author_url = response.urljoin(quote.xpath('.//small[@class="author"]/following-sibling::a/@href').get())
#             request = scrapy.Request(author_url, callback=self.parse_author)
#             request.meta['item'] = item
#             yield request

#         next_page = response.xpath('//li[@class="next"]/a/@href').get()
#         if next_page is not None:
#             yield response.follow(next_page, self.parse)

#     def parse_author(self, response):
#         item = response.meta['item']
#         author_item = AuthorItem()
#         author_item['fullname'] = response.xpath('//h3[@class="author-title"]/text()').get().strip()
#         author_item['born_date'] = response.xpath('//span[@class="author-born-date"]/text()').get().strip()
#         author_item['born_location'] = response.xpath('//span[@class="author-born-location"]/text()').get().strip()
#         author_item['description'] = response.xpath('//div[@class="author-description"]/text()').get().strip()
#         item['author'] = author_item
#         yield item