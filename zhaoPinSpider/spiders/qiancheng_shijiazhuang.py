# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import Spider
from zhaoPinSpider.items import ZhaopinspiderItem
from zhaoPinSpider.spiders.qiancheng import ZhaopinSpider


class SubSpider(ZhaopinSpider):
    name = "qiancheng_shijiazhuang"
    start_urls = map(lambda i: r"https://search.51job.com/list/160200,000000,0000,00,9,99,%2B,2," \
    	+str(i)+r".html?        lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=" \
    	, range(1,500))
