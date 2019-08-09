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
 

def swarm_psychologytoday(begin_page,end_page):
	current=1
	while begin_page<=end_page:
		# print current
		try:
			url = 'https://www.psychologytoday.com/intl/blog-posts?page='+str(begin_page)
			req = requests.get(url, headers=headers, timeout=60)
			req.encoding="utf-8"
			# print req.text.encode('utf-8')
			try:
				soup = BeautifulSoup(req.text, 'html.parser')
				# print req.text
				list = []
				for article in soup.find_all(name='div',attrs={"class":"blog-entry teaser-listing--item col-lg-12 col-sm-10"}):
					try:
						time_dom=article.find('p',attrs={"class":"blog_entry__publish_info text-teaser-byline d-none d-sm-block"})
						# date=time_dom['datetime']
						date_string=time_dom.text.encode("utf-8").strip()
						date_string=date_string[date_string.find(' on '):date_string.find(' in ')]
						h2=article.find('h2',attrs={"class":"blog_entry__title"})
						s= "page:"+str(begin_page)+" count:"+str(current)+" title: "+h2.string.encode("utf-8").strip()+","+date_string
						# fw.write(s+"\n")
						print s
						current+=1
					except Exception as e:
						print "h2",e
						pass
			except Exception as e:
				print "line error:" ,e
			# print item,"******"
		except Exception as e:
			print "error1:",e
			# print(e)
		begin_page+=1
if __name__ == "__main__":
	swarm_psychologytoday(int(sys.argv[1]),int(sys.argv[2]))