import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes" # is like id, can't be repeated for spiders

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
