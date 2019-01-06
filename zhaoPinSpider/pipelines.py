# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook

class ZhaopinspiderPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['工作名称', '联系方式'])
        #self.log('+++++++++++++++++++++++++++++++++init+++++++++++++++++++++++++++++++++++++++++++++++++')
 
    def process_item(self, item, spider):
        line = [item['title'], item['phone']]
        self.ws.append(line)
        self.wb.save('/home/chris/scrapy/zhaoPinSpider/zhaopin.xlsx')
        return item
