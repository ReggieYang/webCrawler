import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import myItem

class DmozSpider(scrapy.spiders.Spider):
    name = "ebay_item"
    allowed_domains = ["ebay.com"]
    start_urls = []
    url_prefix = "http://www.ebay.com/itm/"
    rules = [Rule(LinkExtractor(allow=['/tor/\d+']), 'parse')]

    file_object = open('/home/reggieyang/itemList', 'rb')

    for line in file_object:
        lineStr = str(line)
        start_urls.append(url_prefix + lineStr[0:len(lineStr)-1])

    def parse(self, response):
        price = str(response.xpath('//span[@id=\"prcIsum\"]//@content').extract())
        price = price[3:len(price) - 2]
        item = ebayItem()
        item['price'] = price
        url = str(response.url)
        item['itemId'] = url[len(url)-12:len(url)-1]
        return item


class ebayItem(scrapy.Item):
    price = scrapy.Field()
    itemId = scrapy.Field()