# -*- coding: utf-8 -*-
import time
import os
if __name__ == '__main__':
	try:
		import psyco
		psyco.profile()
	except ImportError:
		pass
	tasks = ["zhaopin_nanjing","zhaopin_shijiazhuang","zhaopin_zhengzhou","zhaoping_hangzhou", \
	"qiancheng_nanjing","qiancheng_shijiazhuang","qiancheng_zhengzhou","qiancheng_hangzhou"]
	for task in tasks:
		print('---------------spider_starting:%s-------------'%task)
		command = r'scrapy crawl '+task
		os.system(command)
		time.sleep(5)
