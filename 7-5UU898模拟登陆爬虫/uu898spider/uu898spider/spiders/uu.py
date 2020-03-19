# -*- coding: utf-8 -*-
import scrapy


class UuSpider(scrapy.Spider):
    name = 'uu'
    allowed_domains = ['uu898.com']
    start_urls = ['http://uu898.com/']

    def parse(self, response):
        pass
