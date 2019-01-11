# -*- coding: utf-8 -*-
import scrapy
import re
import time
import sys
import random
from scrapy.spiders import Spider
from zhaoPinSpider.items import ZhaopinspiderItem



class ZhaopinSpider(scrapy.Spider):
    name = "zhaopin"
    allowed_domains = ["sou.zhaopin.com","jobs.zhaopin.com"]
    #start_urls = ['https://sou.zhaopin.com/?jl=702']

    start_urls = map(lambda i: r"https://sou.zhaopin.com/?p="+str(i)+r"&jl=702", range(1,13))
    '''
    def start_requests(self):
    	#for i in range(2,8): 
        #	self.start_urls.append("https://sou.zhaopin.com/?p="+str(i)+"&jl=702")
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True,callback=self.parse)
            time.sleep(10)
    '''
    def parse(self, response):
        content_urls = response.xpath("//div[@class='contentpile__content__wrapper__item clearfix']/a/@href").extract()
        for url in content_urls:
            #time.sleep(random.random())
            yield scrapy.Request(url, callback=self.deal_content)
        pass

    def deal_content(self,response): 
        reload(sys)
        sys.setdefaultencoding("utf-8")
        #self.log('User-Agent:%s'% response.request.headers['User-Agent'])
        introContents = re.findall('<div class="intro-content">(.*?)</div>',response.body,re.S)
        for introContent in introContents:
			#print introContent.replace(u'\xa0', u' ')
			#unicode中的‘\xa0’字符在转换成gbk编码时会出现问题，gbk无法转换'\xa0'字符,将'\xa0‘替换成u' '空格。
			#phoneNums = re.findall(u'\u7535\u8bdd(.*?)',gbkContent,re.S)
            phoneNums = re.findall(r'\(?[01]\d{2,3}[)-]?\d{7,8}',introContent)
            if phoneNums :
            	phoneNums = list(set(phoneNums))
                self.log('----------------phoneNums: %s' % phoneNums)
                titles = re.findall('<title>(.*?)</title>',response.body,re.S)
                if titles :
                    item = ZhaopinspiderItem()
                    for phoneNum in phoneNums :
                        phoneNum = phoneNum.decode('utf-8').encode('utf-8')
                    item['title'] = titles[0]
                    self.log('---------------titles :%s'% item['title'])
                    item['phone'] = ','.join(phoneNums) #phoneNums[0].decode('utf-8').encode('utf-8')
                    yield item
                else:
                    self.log('---------------titles not matched--------------')
            else: 
                self.log('---------------phoneNums not matched--------------')

