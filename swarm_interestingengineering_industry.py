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

def swarm_interestingengineering_industry(begin_page,end_page):
	# fw=open('2','w')
	time.sleep(1)
	count=1
	for i in range(begin_page,end_page+1):
		try:
			url = 'https://interestingengineering.com/industry?page='+str(i)
			res = requests.get(url, headers=headers, timeout=60)
			# CVEList_html = getMiddleStr(res.text, 'New entries:', 'Graduations')
			soup = BeautifulSoup((res.text).encode('utf-8'), 'html.parser')
			list = []
			for article in soup.find_all(name='article',attrs={"class":"sub-featured-v ias-item"}):
				h2=article.find(name='h2',attrs={"class":"clearfix"})
				a=h2.find_all('a')[0]
				date_dom=article.find(name='time',attrs={})
				date=date_dom['datetime'].encode('utf-8').split('T')[0]
				s= "page:"+str(i)+" count:"+str(count)+" title: "+a.string.encode("utf-8")+","+date	#
				count=count+1
				print s
		except Exception as e:
			print "error:",
			print(e)
 
if __name__ == "__main__":
	swarm_interestingengineering_industry(int(sys.argv[1]),int(sys.argv[2]))