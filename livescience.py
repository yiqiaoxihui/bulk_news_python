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
 

def swarm_rd(begin_page,end_page,type1):
	current=0
	while begin_page<=end_page:
		# print current
		try:
			url = 'https://www.livescience.com/'+type1+'/'+str(begin_page)
			req = requests.get(url, headers=headers, timeout=60)
			req.encoding="utf-8"
			soup = BeautifulSoup(req.text, 'html.parser')
			# print req.text
			list = []
			for article in soup.find_all(name='li',attrs={"class":"search-item line pure-g"}):
				# print article
				# h3=article.find_all('h3')[0]
				try:
					date_div=article.find('div',attrs={"class":"date-posted"})
					date=date_div.string.encode('utf-8').strip()
					h2=article.find('h2',attrs={})
					a=h2.find('a',attrs={})
					# print h3
					# print  "h3.find"
					# a=h3.find('a')
					# print a
					print "page:",begin_page,"count:",current,"title: ",a.string.encode("utf-8").strip(),",",date
					current+=1
					if current % 20 == 0:
						time.sleep(30)
				except Exception as e:
					print "get article",e
					pass
				#print(a['href'])
				#print(a.string)
		except Exception as e:
			print "error:",
			print(e)
		begin_page+=1
if __name__ == "__main__":
	swarm_rd(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])