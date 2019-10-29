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

def swarm_hbr(begin_page,end_page,type_name):
	headers = {}
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
	headers["Accept-Encoding"] = "gzip, deflate"
	headers["Upgrade-Insecure-Requests"] = "1"
	file_name='hbr_'+type_name+'_'+str(begin_page)+"_to_"+str(end_page)+".txt"
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
		time.sleep(2)
		try:
			req=''
			# url='https://www.hbr.com/markets2/api/search?query=opinion&page='+str(page)
			url='https://hbr.org/service/components/external-list/latest/'+str(page)+'/8?format=json&id=page.external-list.the-latest'
			req = requests.get(url, headers=headers, timeout=60)
			# req.encoding="utf-8"
			json_text=json.loads(req.text.encode('utf-8'))
			if json_text.get('entry'):
				entry=json_text['entry']
				for item in entry:#li,article-list__item
					time_lable=''
					title=''
					if item.get('title'):
						title=item['title'].encode('utf-8').strip()
					if item.get('published'):
						time_lable=item.get('published').encode('utf-8').strip()
					count+=1
					s="page:"+str(page)+" count: "+str(count)+" title: "+title+", "+time_lable
					s1=title+", "+time_lable
					print s
					fw.write(s1+"\n")
						# if times>=3:
						# 	break
			else:
				print "no json_text",page
				print req.text
				pass
					# print "popular_24h no"
				#print(a['href'])
				#print(a.string)
		except Exception as e:
			print "parser error:",e,req.text
			dic['msg']="request error: "+str(e)
			dic['status']=0
	fw.close()
	dic['file_name']=file_name
	return dic
if __name__ == '__main__':
	swarm_hbr(sys.argv[1],sys.argv[2],sys.argv[3])

