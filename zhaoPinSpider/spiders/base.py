# -*- coding: utf-8 -*-
import scrapy
import sys
import os
from scrapy.spiders import Spider
from scrapy import signals
from openpyxl import Workbook
import redis


class BaseSpider(scrapy.Spider):
    name = "base"
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BaseSpider,cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        self.log('---------------spider_closed-------------')
        r = redis.Redis(host='127.0.0.1',port=6379)
        xls_name = self.name+r"_all.xlsx"
        if not os.path.isfile(xls_name) :
            os.mknod(xls_name)
            self.wb = Workbook()
            self.ws = self.wb.active
            self.ws.append(['工作名称', '联系方式'])
            self.log(r.hkeys(self.name))
            for phone in r.hkeys(self.name):
                line = [r.hget(self.name,phone),phone]
                self.ws.append(line)
            self.wb.save(xls_name)

