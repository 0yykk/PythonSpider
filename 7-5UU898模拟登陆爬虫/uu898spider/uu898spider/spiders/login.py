# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['uu898.com']
    start_urls = ['http://uu898.com/']
    header={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
#编写star_request(self)，第一次会默认调取该方法中的请求
    def start_requests(self):
        #先爬一次登录页，然后进入回调函数parse
        return [Request("https://user.uu898.com/Login.aspx",meta={"cookiejar":1},callback=self.parse)]
    def parse(self, response):
        #设置要传递的post信息，此时没有验证码字段
        data = {
            
        }
