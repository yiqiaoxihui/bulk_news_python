# -*- coding: utf-8 -*-
import json
import time
import sys
import requests
import os
import chardet
from bs4.diagnose import diagnose
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
def telegraph_opinion(begin_page,end_page,type_name):
	headers = {}
	headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
	headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
	headers["accept-language"] = "zh-CN,zh;q=0.9"
	headers["accept-encoding"] = "gzip, deflate, br"
	headers["upgrade-insecure-requests"] = "1"
	headers['dnt']="1"
	file_name='telegraph_'+type_name+".txt"
	count=0
	dic={}
	dic['status']=1
	dic['msg']="download success"
	if str(begin_page).isdigit() == False or str(end_page).isdigit() ==False:
		print("input error: illege input")
		dic['msg']="input error: illege input"
		dic['status']=0
		return dic
	begin_page=int(begin_page)
	end_page=int(end_page)
	fw=open("download/"+file_name,'w')
	# fw=open("q_format.html",'r')
	for i in range(begin_page,end_page+1):
		try:
			url='https://www.telegraph.co.uk/opinion/telegraph-view/page-'+str(i)
			# print url
			req = requests.get(url, headers=headers, timeout=60)
			soup = BeautifulSoup(req.text.encode('utf-8'), 'html.parser')	#html5lib:最好的容错性;以浏览器的方式解析文档;生成HTML5格式的文档
			# print soup
			# soup=soup.find('body')
			# print soup
			try:
				for item in soup.find_all(name='div',attrs={"class":"card__content"}):#li,article-list__item
					# print item
					# print("*************************")
					# print item.string.encode('utf-8')
					span=item.find('span',attrs={"class":"list-headline__text"})
					time_lable=item.find('time',attrs={"class":"card__date"})
					# date=time_lable.find(attrs={"class":"time-container"})
					# print span.string.encode('utf-8')
					
					count+=1
					s="page:"+str(i)+" count: "+str(count)+" title: "+span.string.encode('utf-8').strip()+", "+time_lable.text.encode('utf-8').strip().split(',')[0]
					s1="title: "+span.string.encode('utf-8').strip()+", "+time_lable.text.encode('utf-8').strip().split(',')[0]
					print s
					fw.write(s1+"\n")
					#print(a['href'])
					#print(a.string)
			except Exception as e:
				print "find error:",e
				dic['msg']="line error: "+str(e)
				dic['status']=0
		except Exception as e:
			print "request error:",e
			dic['msg']="request error: "+str(e)
			dic['status']=0
	dic['file_name']=file_name
	return dic

s='review-outlook-u-s'
s='commentary-u-s'
telegraph_opinion(sys.argv[1],sys.argv[2],sys.argv[3])
