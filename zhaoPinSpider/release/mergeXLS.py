# -*- coding: utf-8 -*-
import time
import os
if __name__ == '__main__':
	try:
		import psyco
		psyco.profile()
	except ImportError:
		pass
	r = redis.Redis(host='127.0.0.1',password='3664',port=6379)
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

