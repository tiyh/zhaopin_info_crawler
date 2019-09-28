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
    name = "sdjzu"
    allowed_domains = ["sdjzu.bibibi.net"]
    #http://sdjzu.bibibi.net/module/onlines
    start_urls = map(lambda i: r"http://sdjzu.bibibi.net/module/getonlines?start_page=1&k=&recruit_type=&count=15&start="+str(i)+r"&_=1569421659656=", range(1,330))
    #//*[@id="data_html"]/li[1]/div/div[2]/p[1]/a
    #Request URL: http://sdjzu.bibibi.net/module/getonlines?start_page=1&k=&recruit_type=&count=15&start=5&_=1569421659656
    def parse(self, response):
        base = r'http://sdjzu.bibibi.net/detail/online?menu_id=&id='
        recruitment_ids = re.findall(r'"recruitment_id":"(.*?)"',response.body)
        self.log('----------------recruitment_ids: %s' % recruitment_ids)
        for recruitment_id in recruitment_ids:
            yield scrapy.Request(base+recruitment_id, callback=self.deal_content)
        pass
    def deal_content(self,response): 
        reload(sys)
        sys.setdefaultencoding("utf-8")
        #title *[@id="data_details"]/div[1]/div/div[1]/h1
        contents = response.xpath("//div[@id='data_details']/div[1]/div/div[2]").extract()
        for cont in contents:
            phoneNums = re.findall(r'\(?[01]\d{2,3}[)-]?\d{7,8}',cont)
            if phoneNums :
                phoneNums = list(set(phoneNums))
                self.log('----------------phoneNums: %s' % phoneNums)
                titles = re.findall('<h1 class="dh-tit" style="font-weight:normal;line-height: 50px;text-align: center">(.*?)</h1>',response.body,re.S)
                if titles :
                    item = ZhaopinspiderItem()
                    for phoneNum in phoneNums :
                        phoneNum = phoneNum.decode('utf-8').encode('utf-8')
                    item['title'] = titles[0]
                    self.log('---------------titles :%s'% item['title'])
                    item['phone'] = ','.join(phoneNums) 
                    mails = re.findall(r'([\w\.-]+@[\w\.-]+\.[\w\.]+)',cont)
                    if mails:
                        mails = list(set(mails))
                        self.log('----------------mails: %s' % mails)
                        item['mail'] = ','.join(mails)
                    else:
                        item['mail'] = ''
                    yield item
                else:
                    self.log('---------------titles not matched--------------')
            else: 
                self.log('---------------phoneNums not matched--------------')