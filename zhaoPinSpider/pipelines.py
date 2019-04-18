# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
from openpyxl import Workbook


class ZhaopinspiderPipeline(object):
    def __init__(self):
        #self.wb = Workbook()
        #self.ws = self.wb.active
        #self.ws.append(['工作名称', '联系方式'])
        #self.log('+++++++++++++++++++++++++++++++++init+++++++++++++++++++++++++++++++++++++++++++++++++')
        self.r = redis.Redis(host='127.0.0.1',password='3664',port=6379)
    def process_item(self, item, spider):
        line = [item['title'], item['phone']]
        #self.ws.append(line)
        if (spider.name == "qiancheng"):
            #self.r.hset('qiancheng_zhengzhou',item['phone'],item['title'].decode('utf-8'))
            #self.r.hset('qiancheng_zhengzhou_500_1879',item['phone'],item['title'].decode('utf-8'))
            #self.wb.save('/home/chris/scrapy/zhaoPinSpider/qiancheng-zhengzhou.xlsx')
            
            self.r.hset('qiancheng_nanjing',item['phone'],item['title'].decode('utf-8'))
            #self.r.hset('qiancheng_nanjing_1_500',item['phone'],item['title'].decode('utf-8'))
            self.r.hset('qiancheng_nanjing_500_2000',item['phone'],item['title'].decode('utf-8'))
        elif (spider.name == "zhaopin"):
            self.r.hset('zhaopin_shijiazhuang',item['phone'],item['title'].decode('utf-8'))
            #self.wb.save('/home/chris/scrapy/zhaoPinSpider/zhaopin-zhengzhou.xlsx')
        return item
