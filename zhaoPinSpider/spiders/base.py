# -*- coding: utf-8 -*-
import scrapy
import sys
import os
from scrapy.spiders import Spider
from scrapy import signals
from openpyxl import Workbook
import redis
import ConfigParser
import logging


class BaseSpider(scrapy.Spider):
    name = "base"
    new_element_name = "_1"
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BaseSpider,cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        self.log('---------------spider_closed-------------')
        CONFIG_FILE_PATH = os.path.abspath('.')+r"/scrapy.cfg"
        logging.warning('CONFIG_FILE_PATH:%s'%CONFIG_FILE_PATH)
        cf = ConfigParser.ConfigParser()
        cf.read(CONFIG_FILE_PATH)
        db_host = cf.get("redis", "host")
        db_port = cf.getint("redis", "port")
        db_pass = cf.get("redis", "pass")
        if db_pass.strip():
            self.log('pass:%s'%db_pass)
            r = redis.Redis(host=db_host,password=db_pass,port=db_port)
        else:
            self.log('db_port:%s'%db_port)
            r = redis.Redis(host=db_host,port=db_port)

        xls_name = self.name+r"_all.xlsx"
        if not os.path.isfile(xls_name) :
            os.mknod(xls_name)
            self.wb = Workbook()
            self.ws = self.wb.active
            self.ws.append(['工作名称', '联系方式','邮箱'])
            self.log(r.hkeys(self.name))
            for phone in r.hkeys(self.name):
                all=r.hget(self.name,phone).split("@@@@")
                if all != None :
                    if len(all)==2:       
                        line = [all[0],phone,all[1]]
                    else :
                        line = [all[0],phone,'None']
                    self.ws.append(line)
            self.wb.save(xls_name)

        new_element_xls_name = self.name+self.new_element_name+r".xlsx"
        if not os.path.isfile(new_element_xls_name) :
            os.mknod(new_element_xls_name)
            self.wb = Workbook()
            self.ws = self.wb.active
            self.ws.append(['工作名称', '联系方式','邮箱'])
            hname =self.name+self.new_element_name
            self.log(r.hkeys(hname))
            for phone in r.hkeys(hname):
                all=r.hget(hname,phone).split("@@@@")
                if all != None :
                    logging.warning('all[0]:%s,a[1]:%s'%(all[0],all[1]))
                    if len(all)==2 :    
                        line = [all[0],phone,all[1]]
                    else :
                        line = [all[0],phone,'None']
                    self.ws.append(line)
            self.wb.save(new_element_xls_name)

