# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
from openpyxl import Workbook
import ConfigParser
import os
import logging


class ZhaopinspiderPipeline(object):
    def __init__(self):
        #self.wb = Workbook()
        #self.ws = self.wb.active
        #self.ws.append(['工作名称', '联系方式'])

        #self.log('+++++++++++++++++++++++++++++++++init+++++++++++++++++++++++++++++++++++++++++++++++++')
        CONFIG_FILE_PATH = os.path.abspath('.')+r"/scrapy.cfg"
        cf = ConfigParser.ConfigParser()
        logging.warning('CONFIG_FILE_PATH:%s'%CONFIG_FILE_PATH)
        cf.read(CONFIG_FILE_PATH)
        db_host = cf.get("redis", "host")
        db_port = cf.getint("redis", "port")
        db_pass = cf.get("redis", "pass")
        if db_pass.strip():
            self.r = redis.Redis(host=db_host,password=db_pass,port=db_port)
        else:
            self.r = redis.Redis(host=db_host,port=db_port)

    def process_item(self, item, spider):
        line = [item['title'], item['phone']]
        #self.ws.append(line)
        if (self.r.hexists(spider.name,item['phone']) == 0) :
            self.r.hset(spider.name+spider.new_element_name,item['phone'],item['title'].decode('utf-8'))
        self.r.hset(spider.name,item['phone'],item['title'].decode('utf-8'))

        #if (spider.name.startswith("qiancheng")):
            #self.r.hset('qiancheng_zhengzhou',item['phone'],item['title'].decode('utf-8'))
            #self.r.hset('qiancheng_zhengzhou_500_1879',item['phone'],item['title'].decode('utf-8'))
            #self.wb.save('/home/chris/scrapy/zhaoPinSpider/qiancheng-zhengzhou.xlsx')
            
            #self.r.hset('qiancheng',item['phone'],item['title'].decode('utf-8'))
            #self.r.hset('qiancheng_nanjing_1_500',item['phone'],item['title'].decode('utf-8'))
            #self.r.hset('qiancheng_nanjing_500_2000',item['phone'],item['title'].decode('utf-8'))
        #elif (spider.name == "zhaopin"):
            #self.r.hset('zhaopin_shijiazhuang',item['phone'],item['title'].decode('utf-8'))
            #self.wb.save('/home/chris/scrapy/zhaoPinSpider/zhaopin-zhengzhou.xlsx')
        return item
