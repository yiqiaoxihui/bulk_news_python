# -*- coding: utf-8 -*-

#author		 heaven
#date		 2019/2/1
#脚本描述	 
#脚本使用说明 获取insidehighered的标题

import json
import time
import sys
import requests
import os
import chardet
from bs4.diagnose import diagnose
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
def insidehighered(begin_page,end_page,type_name):
	headers = {}
	headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
	headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
	headers["accept-language"] = "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
	headers["accept-encoding"] = "gzip, deflate, br"
	headers["upgrade-insecure-requests"] = "1"
	headers['dnt']="1"
	headers['cookie']='__cfduid=dee21939353735c574a21e7103e1910601570180009; has_js=1; _ga=GA1.2.289070388.1570180018; _gid=GA1.2.1694234530.1570180018; __gads=ID=2af65175ba65ee09:T=1570180012:S=ALNI_Mav3OSV3x4EnNdaP3eGnyST3fr2CQ; __smVID=c83d441a27962474938c62f84c3cc1f0c3e2cc3876068bf38461c463e3e17623; _fbp=fb.1.1570180021490.554328842; __smToken=ZFbGIOg4KuEyY5eSJwJlBWOk; __atssc=google%3B3; __smListBuilderShown=Fri%20Oct%2004%202019%2017:09:17%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4); __atuvc=21%7C40; __atuvs=5d970bb15f5099a6014'
	headers['sec-fetch-mode']='navigate'
	headers['upgrade-insecure-requests']='1'
	headers['sec-fetch-site']='none'
	headers['sec-fetch-user']='?1'
	file_name='insidehighered_'+type_name+'_page_'+str(begin_page)+"_to_"+str(end_page)+".txt"
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
	html_file='insidehighered.html'
	# fw=open("q_format.html",'r')
	for i in range(begin_page,end_page+1):
		try:
			url = 'https://www.insidehighered.com/'+type_name+'?page='+str(i)
			# url='https://www.insidehighered.com/news/2011/08/31/qt/syrians_attack_facebook_page?page=7'
			cmd='wget '+url+' -O '+html_file
			status=os.system(cmd)
			if status==0:
				soup = BeautifulSoup(open(html_file))
				pane=soup.find('div',attrs={'class':'panel-pane'})
				if pane:
					pane_content=pane.find('div',attrs={'class':'pane-content'}).find('div',attrs={'class':'view'}).find('div',attrs={'class':'view-content'})
					if pane_content:
						try:
							for item in soup.find_all(name='div',attrs={"class":"views-row"}):
								# print("*************************")
								# print item.string.encode('utf-8')
								title=''
								title_div=item.find('div',attrs={'class':'field-content'})
								if title_div:
									a=title_div.find('a',attrs={})
									if a:
										title=a.text.encode('utf-8')
									else:
										'no find title a',i
								else:
									'no find title div',i
								time_lable=item.find('em',attrs={"class":"views-field"})
								if time_lable:
									time_span=time_lable.find('span',attrs={'class':'field-content'})
									if time_span:
										date=time_span.text.encode('utf-8').strip()
								else:
									print 'no find time div',i
								# date=time_lable.find(attrs={"class":"time-container"})
								# print h3.string.encode('utf-8')
								count+=1
								s="page:"+str(i)+" count: "+str(count)+" title: "+title+", "+date
								print s
								s1="title: "+title+", "+date
								fw.write(s1+"\n")
								#print(a['href'])
								#print(a.string)
						except Exception as e:
							print "find error:",e
							dic['msg']="line error: "+str(e)
							dic['status']=0
					else:
						print "no find pane_content"
				else:
					print 'no find panel-pane'
			else:
				print "os.system error",status
		except Exception as e:
			print "request error:",e
			dic['msg']="request error: "+str(e)
			dic['status']=0
	dic['file_name']=file_name
	fw.close()
	return dic

insidehighered(sys.argv[1],sys.argv[2],sys.argv[3])
