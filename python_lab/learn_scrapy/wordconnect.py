import scrapy
class StackOverflowSpider(scrapy.Spider):
    name = 'wordconnect'
    start_urls = ['http://wordconnect.net/']
    def parse(self, response):
        for href in response.css('.lcp_catlist a::attr(href)'):
            full_url = href.extract()
            yield scrapy.Request(full_url, callback=self.parse_sub1)
    def parse_sub1(self, response):
        for href in response.css('.ulcat a::attr(href)'):
            full_url = href.extract()
            yield scrapy.Request(full_url, callback=self.parse_question)
    def parse_question(self, response):
        yield {
            'link': response.url,
            'answer': response.css('.answers').extract(),
        }
