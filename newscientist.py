#coding=utf8
#author		 heaven
#date		 2019/2/1
#脚本描述	 
#脚本使用说明 

import sys
from bs4 import BeautifulSoup
import requests
import re
# import pymysql
import time
def swarm_newscientist(begin_page,end_page):
	headers = {}
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
	headers["Accept-Encoding"] = "gzip, deflate"
	headers["Upgrade-Insecure-Requests"] = "1"
	file_name='newscientist'+".txt"
	count=0
	dic={}
	dic['status']=1
	dic['msg']="download success"
	if str(begin_page).isdigit() == False or str(end_page).isdigit() ==False:
		print "input error: illege input"
		dic['msg']="input error: illege input"
		dic['status']=0
		return dic
	begin_page=int(begin_page)
	end_page=int(end_page)
	if begin_page <= 1:
		begin_page=1
	if end_page <=1:
		end_page=1
	fw=open("download/"+file_name,'w')
	for i in range(begin_page,end_page+1):
		try:
			url = 'https://www.newscientist.com/section/news/page/'+str(i)
			# print url
			req = requests.get(url, headers=headers, timeout=60)
			# req.encoding="utf-8"
			soup = BeautifulSoup((req.text).encode('utf-8'), 'html.parser')
			list = []
			# print req.text
			for item in soup.find_all('div',attrs={"class":"card__content card__content--linked"}):
				try:
					h2=item.find('h2',attrs={"class":"card__heading"})
					# print a
				except Exception as e:
					print "find a error:", e
					continue
				if (not h2):
					continue
				count+=1
				s="page:"+str(i)+" count: "+str(count)+" title: "+h2.text.encode('utf-8').strip()
				print s
				fw.write(s+"\n")
		except Exception as e:
			print "parser error:",e
			dic['msg']="request error: "+str(e)
			dic['status']=0
	fw.close()
	dic['file_name']=file_name
	return dic
swarm_newscientist(sys.argv[1],sys.argv[2])