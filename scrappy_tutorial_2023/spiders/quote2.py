import scrapy


class Quote2Spider(scrapy.Spider):
    name = "quote2"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
       "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            yield {
                "author": quote.xpath('span/small[@class="author"]/text()').get(),
                "text": quote.xpath('span[@class="text"]/text()').get(),
                "tags": quote.xpath('div[@class="tags"]/a[@class="tag"]/text()').getall(),
            }