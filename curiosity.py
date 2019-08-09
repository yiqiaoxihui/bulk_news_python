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
 

def swarm_curiosity(begin_page,end_page):
	current=1
	while begin_page<=end_page:
		# print current
		try:
			url = 'https://curiosity.com/proxy/ajax/subjects/science-technology/topics/'+str(begin_page)
			req = requests.get(url, headers=headers, timeout=60)
			req.encoding="utf-8"
			# print req.text.encode('utf-8')
			try:
				soup = BeautifulSoup(req.text, 'html.parser')
				# print req.text
				list = []
				for article in soup.find_all(name='div',attrs={"class":"content-card series-topic-card js-card"}):
					try:
						# time_dom=article.find('time',attrs={})
						# date=time_dom['datetime']
						h3=article.find('h3',attrs={})
						s= "page:"+str(begin_page)+" count:"+str(current)+" title: "+h3.string.encode("utf-8").strip()#+","+date.encode("utf-8").strip()
						# fw.write(s+"\n")
						print s
						current+=1
					except Exception as e:
						print "h3",e
						pass
			except Exception as e:
				print "line error:" ,e
			# print item,"******"
		except Exception as e:
			print "error1:",e
			# print(e)
		begin_page+=1
if __name__ == "__main__":
	swarm_curiosity(int(sys.argv[1]),int(sys.argv[2]))