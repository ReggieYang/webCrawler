import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class DmozSpider(scrapy.spiders.Spider):
    name = "ebay_item"
    allowed_domains = ["ebay.com"]
    start_urls = []
    url_prefix = "http://www.ebay.com/itm/"
    # rules = [Rule(LinkExtractor(allow=['/tor/\d+']), 'parse')]

    file_object = open('/Users/kaimaoyang/PycharmProjects/webCrawler/mySpider/spiders/itemList', 'rb')

    for line in file_object:
        start_urls.append(url_prefix + str(line, encoding="utf-8")[:-1])

    def parse(self, response):
        item = EbayItem()
        price = response.xpath('//span[@id=\'prcIsum\']//@content').extract()[0]
        item['price'] = price
        item['itemId'] = str(response.url)[-12:]
        item['test'] = response.xpath('//span[@id=\'prcIsum\']/text()').extract()[0]
        return item


class EbayItem(scrapy.Item):
    price = scrapy.Field()
    itemId = scrapy.Field()
    test = scrapy.Field()
