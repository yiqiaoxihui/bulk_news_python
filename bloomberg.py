#coding=utf8
#author		 heaven
#date		 2019/2/1
#脚本描述	 
#脚本使用说明 

import sys
from bs4 import BeautifulSoup
import requests
import re
import json
# import pymysql
import time

def swarm_bloomberg(begin_page,end_page,type_name):
	headers = {}
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
	headers["Accept-Encoding"] = "gzip, deflate"
	headers["Upgrade-Insecure-Requests"] = "1"
	file_name='bloomberg_page_'+type_name+'_'+str(begin_page)+"_to_"+str(end_page)+".txt"
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
	fw=open("download/"+file_name,'w')
	for page in range(begin_page,end_page+1):
		# time.sleep(1)
		if page%10==0:
			time.sleep(10)
		try:
			url='https://www.bloomberg.com/markets2/api/search?query=opinion&page='+str(page)
			req = requests.get(url, headers=headers, timeout=60)
			# req.encoding="utf-8"
			# print req.text
			# soup = BeautifulSoup((req.text).encode('utf-8'), 'html.parser')
			# list = []
			json_text=json.loads(req.text.encode('utf-8'))
			if json_text.get('results'):
				results=json_text['results']
				for item in results:
					eyebrow=item['eyebrow']
					headline=item['headline']
					# print headline
					if eyebrow=='opinion':
						count+=1
						# a=item.find('a',attrs={"class":"u-faux-block-link__overlay js-headline-text"})
						# pub_time=item.find('time',attrs={"class":"fc-item__timestamp"})
						s="page:"+str(page)+" count: "+str(count)+" title: "+item['headline'].encode('utf-8').strip()+' ,'+item['publishedAt'].encode('utf-8')
						print s
						s1="title: "+item['headline'].encode('utf-8').strip()+' ,'+item['publishedAt'].encode('utf-8')
						fw.write(s1+"\n")
						# if times>=3:
						# 	break
			else:
				print "no json_text"
				print req.text
				pass
					# print "popular_24h no"
				#print(a['href'])
				#print(a.string)
		except Exception as e:
			print "parser error:",e
			print req.text
			dic['msg']="request error: "+str(e)
			dic['status']=0
	fw.close()
	dic['file_name']=file_name
	return dic
if __name__ == '__main__':

	swarm_bloomberg(sys.argv[1],sys.argv[2],sys.argv[3])

