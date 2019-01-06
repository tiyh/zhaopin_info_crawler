# -*- coding: utf-8 -*-
import scrapy


class ZhaopinSpider(scrapy.Spider):
    name = "zhaopin"
    allowed_domains = ["sou.zhaopin.com"]
    start_urls = ['http://sou.zhaopin.com/']

    def parse(self, response):
        pass
