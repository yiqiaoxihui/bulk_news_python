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

def swarm_huffpost(begin_page,end_page,type_name):
	headers = {}
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
	headers["Accept-Encoding"] = "gzip, deflate"
	headers["Upgrade-Insecure-Requests"] = "1"
	file_name='huffpost_'+type_name.split('/')[-1]+'_'+str(begin_page)+"_to_"+str(end_page)+".txt"
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
		if page % 2==0:
			time.sleep(3)
		try:
			req=''
			# url='https://www.huffpost.com/markets2/api/search?query=opinion&page='+str(page)
			url='https://www.huffpost.com/api/'+type_name+'/cards?page='+str(page)+'&limit=undefined'
			# url='https://www.huffpost.com/api/section/opinion/cards?page=1&limit=undefined'
			url='https://www.huffpost.com/api/section/opinion/cards?page=1&limit=undefined'
			req = requests.get(url, headers=headers, timeout=60)
			req.encoding="utf-8"
			json_text=json.loads(req.text.encode('utf-8'))
			if json_text.get('cards'):
				cards=json_text['cards']
				for item in cards:#li,article-list__item
					# print item
					# print("*************************")
					# print item.string.encode('utf-8')
					
					headlines_list=item.get('headlines')
					for headline in headlines_list:
						time_lable=''
						title=''
						title=headline['text'].encode('utf-8').strip()
						if headline.get('published_date'):
							time_lable=headline.get('published_date').encode('utf-8').strip().split('T')[0]
					# date=time_lable.find(attrs={"class":"time-container"})
					# print a.string.encode('utf-8')
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
			print "parser error:",e,req.text.encode('utf-8').strip()
			dic['msg']="request error: "+str(e)
			dic['status']=0
	fw.close()
	dic['file_name']=file_name
	return dic
if __name__ == '__main__':

	swarm_huffpost(sys.argv[1],sys.argv[2],sys.argv[3])

