# -*- coding: utf-8 -*-
import time
import os
import ConfigParser
if __name__ == '__main__':
	try:
		import psyco
		psyco.profile()
	except ImportError:
		pass
    cf = ConfigParser.ConfigParser()
    cf.read("scrapy.cfg")
    db_host = cf.get("redis", "host")
    db_port = cf.getint("redis", "port")
    db_pass = cf.get("redis", "pass")
    if db_pass.strip():
        r = redis.Redis(host=db_host,password=db_pass,port=db_port)
    else:
        r = redis.Redis(host=db_host,port=db_port)
	#tasks = ["zhaopin_nanjing","zhaopin_shijiazhuang","zhaopin_zhengzhou","zhaoping_hangzhou", \
	#"qiancheng_nanjing","qiancheng_shijiazhuang","qiancheng_zhengzhou","qiancheng_hangzhou"]
	tasks = {"qiancheng_hangzhou":"qiancheng_shaoxing",
		"qiancheng_shijiazhuang":"qiancheng_hengshui",
		"qiancheng_nanjing":"qiancheng_zhenjiang",
		"qiancheng_zhengzhou":"qiancheng_kaifeng"
	}
	for task,task2 in tasks.items() : 
		xls_name = task+r"_all_merged.xlsx"
		if not os.path.isfile(xls_name) :
            os.mknod(xls_name)
            wb = Workbook()
            ws = self.wb.active
            ws.append(['工作名称', '联系方式'])
            print(r.hkeys(task))
            for phone in r.hkeys(task):
                line = [r.hget(task,phone),phone]
                ws.append(line)
            print(r.hkeys(task2))
            for phone in r.hkeys(task2):
                line = [r.hget(task2,phone),phone]
                ws.append(line)
            self.wb.save(xls_name)

