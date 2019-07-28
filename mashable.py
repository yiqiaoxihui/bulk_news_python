#coding=utf8
#author		 heaven
#date		 2019/2/1
#脚本描述	 将cnvd漏洞信息导入到数据库中
#脚本使用说明 python swarm_cve.py

import sys
from bs4 import BeautifulSoup
import requests
import re
import json
# import pymysql
import time

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
headers["Accept-Encoding"] = "gzip, deflate"
headers["Upgrade-Insecure-Requests"] = "1"
 

def swarm_mashable(begin_page,end_page,type1):
	current=0
	while begin_page<=end_page:
		# print current
		try:
			url = 'https://mashable.com/channeldatafeed/Tech/new/page/'+str(begin_page)
			req = requests.get(url, headers=headers, timeout=60)
			req.encoding="utf-8"
			# print req.text
			try:
				json_text=json.loads(req.text)
				if json_text.get('dataFeed'):
					for item in json_text['dataFeed']:
						try:
							date_list=item['itemUrl'].split('/')
							print item['itemUrl'],date_list[-2]
							date=""
							if date_list[-2].isdigit()==True and len(date_list)>=4:
								date=date_list[-4]+"/"+date_list[-3]+"/"+date_list[-2]
							s="page:"+str(begin_page)+" start: "+str(current)+" title: "+item['display_title'].encode("utf-8")+","+date
							print s
							# fw.write(s+"\n")
							current+=1
						except Exception as e:
							print "line error:" ,e
						# print item,"******"
				else:
					print "no dataFeed"
			except Exception as e:
				print "loads error:", e
				#print req.text
				break
		except Exception as e:
			print "error:",e
			# print(e)
		begin_page+=1
if __name__ == "__main__":
	swarm_mashable(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])