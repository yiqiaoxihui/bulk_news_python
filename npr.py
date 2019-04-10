#coding=utf8
#author		 heaven
#date		 2019/2/1
#脚本描述	 将cnvd漏洞信息导入到数据库中
#脚本使用说明 python swarm_cve.py

import sys
from bs4 import BeautifulSoup
import requests
import re
# import pymysql
import time

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
headers["Accept-Encoding"] = "gzip, deflate"
headers["Upgrade-Insecure-Requests"] = "1"
 

def swarm_npr(begin_news,count):
	current=0
	while current<count:
		# print current
		try:
			url = 'https://www.npr.org/sections/health/archive?start='+str(begin_news+current)
			req = requests.get(url, headers=headers, timeout=60)
			req.encoding="utf-8"
			soup = BeautifulSoup(req.text, 'html.parser')
			list = []
			for h2 in soup.find_all(name='h2',attrs={"class":"title"}):
				a=h2.find_all('a')[0]
				print "start:",begin_news+current,"title: ",a.string.encode("utf-8")
				current+=1
				#print(a['href'])
				#print(a.string)
		except Exception as e:
			print "error:",
			print(e)

if __name__ == "__main__":
	swarm_npr(int(sys.argv[1]),int(sys.argv[2]))


