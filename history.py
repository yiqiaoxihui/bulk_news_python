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
import json

#根据首页的moreResultsToken来获取下一页内容，以此类推

def swarm_history(begin_page,end_page):
	headers = {}
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
	headers["Accept-Encoding"] = "gzip, deflate"
	headers["Upgrade-Insecure-Requests"] = "1"
	file_name='history_page_'+str(begin_page)+"_to_"+str(end_page)+"_"+str(int(time.time()))+".txt"
	count=0
	i=1
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
	url='https://www.history.com/news'
	req = requests.get(url, headers=headers, timeout=3600)
	# req.encoding="utf-8"
	soup = BeautifulSoup((req.text).encode('utf-8'), 'html.parser')
	query_token=soup.find(name='div',attrs={"class":"m-component-footer--container m-component-stack--footer"})
	if not query_token:
		print("history:get query_token fail")
		dic['msg']="request error: history:get query_token fail"
		dic['status']=0
		return dic
	moreResultsToken= query_token['stream-more-items']
	initialSlots= query_token['initial-slots']
	if begin_page<=1:
		begin_page=1
		
		for item in soup.find_all(name='div',attrs={"class":"m-card--content"}):
			count+=1
			h2=item.find('h2',attrs={"class":"m-ellipsis--text m-card--header-text"})
			li=item.find('li',attrs={"class":"m-card--metadata-a"})
			if not li:
				pub_time="头条"
			else:
				pub_time=li.text.encode('utf-8')
			s="page:"+str(i)+" count: "+str(count)+" title: "+h2.text.encode('utf-8').strip()+' ,'+pub_time
			print s
			fw.write(s+"\n")
	i=2	#首页算是第一页，有内容
	while i<=end_page:
		# time.sleep(1)
		try:
			url = 'https://www.history.com/.api/stream-html/news?moreResultsToken='+moreResultsToken+'&initialSlots='+initialSlots
			# print url
			req = requests.get(url, headers=headers, timeout=60)
			# req.encoding="utf-8"
			# print req.text.encode('utf-8')
			html_str=json.loads(req.text.encode('utf-8'))['html']
			soup = BeautifulSoup(html_str.encode('utf-8'), 'html.parser')#html.parser
			query_token=soup.find(name='div',attrs={"class":"m-component-footer--container m-component-stack--footer"})
			if not query_token:
				print moreResultsToken
				print initialSlots
				print url
				print "history:get query_token fail",i
				continue
			else:
				# print "begin to get token"
				moreResultsToken= query_token['stream-more-items']
				initialSlots= query_token['initial-slots']
				list = []
				#
				if i<begin_page:
					i+=1
					continue
				else:
					for item in soup.find_all(name='div',attrs={"class":"m-card--content"}):
						count+=1
						h2=item.find('h2',attrs={"class":"m-ellipsis--text m-card--header-text"})
						li=item.find('li',attrs={"class":"m-card--metadata-a"})
						if not li:
							pub_time="头条"
						else:
							pub_time=li.text.encode('utf-8')
						s="page:"+str(i)+" count: "+str(count)+" title: "+h2.text.encode('utf-8').strip()+' ,'+pub_time
						print s
						fw.write(s+"\n")
				i+=1#继续下一页
						#print(a['href'])
						#print(a.string)
		except Exception as e:
			print "parser error:",e
			dic['msg']="request error: "+str(e)
			dic['status']=0
	fw.close()
	dic['file_name']=file_name
	return dic

swarm_history(sys.argv[1],sys.argv[2])