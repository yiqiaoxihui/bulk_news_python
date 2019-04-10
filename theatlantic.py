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
 

def theatlantic(begin_page,end_page):
	count=0
	for i in range(begin_page,end_page+1):
		# time.sleep(1)
		
		try:
			url = 'https://www.theatlantic.com/latest/?page='+str(i)
			req = requests.get(url, headers=headers, timeout=60)
			# req.encoding="utf-8"
			soup = BeautifulSoup((req.text).encode('utf-8'), 'html.parser')
			list = []
			for h2 in soup.find_all(name='h2',attrs={"class":"hed"}):
				# a=h2.find_all('a')[0]
				title=""
				# for em in h2.find_all("em"):
				# 	em_str=str(em.string).encode('utf-8').strip()

				# 	title=title+" " +em_str
				count+=1
				print "count:",count," page:",i,"title: ",title+" "+h2.text.encode('utf-8').strip()
				
				#print(a['href'])
				#print(a.string)
		except Exception as e:
			print "error:",
			print(e)

if __name__ == "__main__":
	theatlantic(int(sys.argv[1]),int(sys.argv[2]))

