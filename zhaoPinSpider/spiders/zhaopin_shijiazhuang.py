# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from zhaoPinSpider.items import ZhaopinspiderItem
from zhaoPinSpider.spiders.zhaopin import ZhaopinSpider

class SubSpider(ZhaopinSpider):
    name = "zhaopin_shijiazhuang"
    start_urls = map(lambda i: r"https://sou.zhaopin.com/?p="+str(i)+r"&jl=565", range(1,13))

