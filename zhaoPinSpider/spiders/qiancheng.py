# -*- coding: utf-8 -*-
import scrapy
import re
import time
import sys
import random
from scrapy.spiders import Spider
from zhaoPinSpider.items import ZhaopinspiderItem
from zhaoPinSpider.spiders.base import BaseSpider

class ZhaopinSpider(BaseSpider,scrapy.Spider):
    name = "qiancheng"
    allowed_domains = ["search.51job.com","jobs.51job.com"]

    start_urls = map(lambda i: r"https://search.51job.com/list/120200,000000,0000,00,9,99,%2520,2," \
        +str(i)+r".html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=" \
        , range(1,200))

    def parse(self, response):
        content_urls = response.xpath("//div[@class='el']/p/span/a/@href").extract()
        for url in content_urls:
            #time.sleep(random.random())
            yield scrapy.Request(url, callback=self.deal_content)
        pass

    def deal_content(self,response): 
        reload(sys)
        sys.setdefaultencoding("utf-8")
        introContents = re.findall('<div class="bmsg job_msg inbox">(.*?)</div>',response.body,re.S)
        for introContent in introContents:
            phoneNums = re.findall(r'\(?[01]\d{2,3}[)-]?\d{7,8}',introContent)
            if phoneNums :
            	phoneNums = list(set(phoneNums))
                self.log('----------------phoneNums: %s' % phoneNums)
                titles = re.findall('<title>(.*?)</title>',response.body,re.S)
                if titles :
                    item = ZhaopinspiderItem()
                    #<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
                    item['title'] = titles[0].decode("gb2312").encode('utf-8')
                    item['phone'] = ','.join(phoneNums)
                    yield item
                else:
                    self.log('---------------titles not matched--------------')
            else: 
                self.log('---------------phoneNums not matched--------------')