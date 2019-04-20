# -*- coding: utf-8 -*-
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
import random

class ZhaopinMiddleware(object):
    def __init__(self):
        self.user_agent_list = [
            'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
            'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
            'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
            'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
            'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
            'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
            'Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)'
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0'
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
            'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
            'Mozilla/5.0 (Microsoft Windows NT 6.2.9200.0); rv:22.0) Gecko/20130405 Firefox/22.0'
            'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'
        ]

    def process_request(self, request, spider):
        request.headers['User-Agent']=random.choice(self.user_agent_list)
        if (spider.name.startswith("zhaopin") and request.url.startswith("https://sou.zhaopin.com")) \
            or(spider.name.startswith("qiancheng") and request.url.startswith("https://search.51job.com")):
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

