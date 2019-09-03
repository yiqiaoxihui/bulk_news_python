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
 

def swarm_theconversation(begin_news,end_news,typ):
	current=0
	file_name='theconversation_'+typ+'-'+str(begin_news)+'_'+str(end_news)+'.txt'
	fw=open(file_name,'w')
	for i in range(begin_news,end_news):
		# print current
		try:
			url = 'https://theconversation.com/us/'+typ+'/articles?page='+str(i)
			req = requests.get(url, headers=headers, timeout=60)
			req.encoding="utf-8"
			soup = BeautifulSoup(req.text, 'html.parser')
			list = []
			for article in soup.find_all(name='article',attrs={"class":"clearfix placed analysis published"}):
				div_title=article.find(name='div',attrs={"class":"article--header"})
				a=div_title.find(name='a',attrs={})
				# date_dom=article.find(name='time',attrs={})
				# date=date_dom['datetime']
				s= str(current)+" : "+a.text.encode("utf-8")#+","+date.encode("utf-8")
				print i,s
				fw.write(s+'\n')
				current+=1
				# print s
				#print(a['href'])
				#print(a.string)
		except Exception as e:
			print "error:",
			print e

if __name__ == "__main__":
	typ="business"
	typ="national"
	typ="health"
	typ="technology"
	swarm_theconversation(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
