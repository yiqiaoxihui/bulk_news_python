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
 

def swarm_npr(begin_news,count,typ):
	file_name='npr_'+typ+".txt"
	dic={}
	dic['status']=1
	dic['msg']="download success"
	fw=open("download/"+file_name,'w')
	current=1
	req = requests.get('https://www.npr.org/sections/news', headers=headers, timeout=60)
	req.encoding="utf-8"
	# print req.text
	soup = BeautifulSoup(req.text, 'html.parser')
	list = []
	for article in soup.find_all(name='article',attrs={"class":"item"}):
		h2=article.find(name='h2',attrs={"class":"title"})
		a=h2.find(name='a',attrs={})
		date_dom=article.find(name='time',attrs={})
		date=date_dom['datetime']
		s= "start:"+str(begin_news+current)+" title: "+a.string.encode("utf-8")+","+date.encode("utf-8")
		current+=1
		print s
		s1=a.string.encode("utf-8")+","+date.encode("utf-8")
		fw.write(s1+'\n')

	while current<count:
		# print current
		try:
			if typ=='news':
				url='https://www.npr.org/get/1001/render/partial/next?start='+str(begin_news+current)
			else:
				url = 'https://www.npr.org/sections/'+typ+'/archive?start='+str(begin_news+current)
			print url,'\n'
			req = requests.get(url, headers=headers, timeout=60)
			req.encoding="utf-8"
			# print req.text
			soup = BeautifulSoup(req.text, 'html.parser')
			list = []
			for article in soup.find_all(name='article',attrs={"class":"item"}):
				h2=article.find(name='h2',attrs={"class":"title"})
				a=h2.find(name='a',attrs={})
				date_dom=article.find(name='time',attrs={})
				date=date_dom['datetime']
				s= "start:"+str(begin_news+current)+" title: "+a.string.encode("utf-8")+","+date.encode("utf-8")
				current+=1
				print s
				s1=a.string.encode("utf-8")+","+date.encode("utf-8")
				fw.write(s1+'\n')
				#print(a['href'])
				#print(a.string)
		except Exception as e:
			print "error:",
			print e,h2
			dic['msg']="request error: "+str(e)
			dic['status']=0
	fw.close()
	dic['file_name']=file_name
	return dic
if __name__ == "__main__":
	typ="business"
	typ="national"
	typ="health"
	typ="technology"
	swarm_npr(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])


