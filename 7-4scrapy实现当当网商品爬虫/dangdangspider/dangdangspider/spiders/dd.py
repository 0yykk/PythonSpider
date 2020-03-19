# -*- coding: utf-8 -*-
import scrapy
from dangdangspider.items import DangdangspiderItem
from scrapy.http import Request

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4008154.html']

    def parse(self, response):
        item=DangdangspiderItem()
        item["title"]=response.xpath("//a[@name='itemlist-picture']/@title").extract()
        item["link"]=response.xpath("//a[@name='itemlist-picture']/@href").extract()
        item["comment"]=response.xpath("//a[@name='itemlist-review']/text()").extract()
        item["price"]=response.xpath("//span[@class='price_n']/text()").extract()
        #print(item["price"])
        yield item
        for i in range(2,100):
            url='http://category.dangdang.com/pg'+str(i)+'-cid4008154.html'
            yield Request(url,callback=self.parse)

