# -*- coding: utf-8 -*-
import scrapy
import sys
import os
from scrapy.spiders import Spider
from scrapy import signals
from openpyxl import Workbook
import redis
import ConfigParser


class BaseSpider(scrapy.Spider):
    name = "base"
    new_element_name = "_new_1"
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BaseSpider,cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        self.log('---------------spider_closed-------------')

        cf = ConfigParser.ConfigParser()
        cf.read("scrapy.cfg")
        db_host = cf.get("redis", "host")
        db_port = cf.getint("redis", "port")
        db_pass = cf.get("redis", "pass")
        if db_pass.strip():
            r = redis.Redis(host=db_host,password=db_pass,port=db_port)
        else:
            r = redis.Redis(host=db_host,port=db_port)

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

        new_element_xls_name = self.name+self.new_element_name+r".xlsx"
        if not os.path.isfile(new_element_xls_name) :
            os.mknod(new_element_xls_name)
            self.wb = Workbook()
            self.ws = self.wb.active
            self.ws.append(['工作名称', '联系方式'])
            hname =self.name+self.new_element_name
            self.log(r.hkeys(hname))
            for phone in r.hkeys(hname):
                line = [r.hget(hname,phone),phone]
                self.ws.append(line)
            self.wb.save(new_element_xls_name)

