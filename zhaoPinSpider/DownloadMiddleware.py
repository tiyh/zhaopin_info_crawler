# -*- coding: utf-8 -*-
from selenium import webdriver
from scrapy.http import HtmlResponse
import time

class ZhaopinMiddleware(object):

    def process_request(self, request, spider):
        if (spider.name == "zhaopin" and request.url.startswith("https://sou.zhaopin.com")) \
            or(spider.name == "qiancheng" and request.url.startswith("https://search.51job.com")):
            driver = webdriver.PhantomJS() 
            #driver = webdriver.Firefox()
            driver.get(request.url)
            #time.sleep(1)
            #js = "var q=document.documentElement.scrollTop=10000" 
            #driver.execute_script(js) #可执行js，模仿用户操作。此处为将页面拉至最底端。 
            body = driver.page_source
            print ("------------访问"+request.url)
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return

