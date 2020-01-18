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
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
headers["Accept"] = "text/html, */*; q=0.01"
headers["Accept-Language"] = "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
headers["Accept-Encoding"] = "gzip, deflate, br"
headers["Upgrade-Insecure-Requests"] = "1"
headers['x-requested-with']='XMLHttpRequest'
def swarm_interestingengineering_industry(begin_page,end_page):
	# fw=open('2','w')
	file_name='interestingengineering_industry'+".txt"
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
	current=1
	time.sleep(1)
	count=1
	use_list=['Civil Engineering','Vehicles','Defense & Military','Transportation','Medical Technology','Electronics','Materials','Automotive','Sustainability','Apps & Software','Mobile']
	for i in range(begin_page,end_page+1):
		time.sleep(2)
		try:
			if sys.argv[3]=='all':
				url='https://interestingengineering.com/page/'+str(i)
			else:
				url = 'https://interestingengineering.com/industry?page='+str(i)
			print url
			res = requests.get(url, headers=headers, timeout=60)
			# CVEList_html = getMiddleStr(res.text, 'New entries:', 'Graduations')
			soup = BeautifulSoup((res.text).encode('utf-8'), 'html.parser')
			# print res.text
			for article in soup.find_all(name='article',attrs={"class":"sub-featured-v ias-item"}):
				# print article
				a_typ=article.find(name='a',attrs={"class":'category-title'})
				if a_typ:
					typ=a_typ.string.encode("utf-8")
					# print typ
					if typ in use_list:					
						h2=article.find(name='h2',attrs={"class":"clearfix"})
						if h2:
							a=h2.find('a')
							if a:
								date=''
								if sys.argv[3]=='all':
									date_dom=article.find_all(name='span',attrs={})[1]
									date=date_dom.string.encode('utf-8')
								else:
									date_dom=article.find(name='time',attrs={})
									if date_dom:
										date=date_dom['datetime'].encode('utf-8').split('T')[0]
									else:
										print 'no find date'
								s= "page:"+str(i)+" count:"+str(count)+" title: "+a.string.encode("utf-8")+","+date	#
								count=count+1
								print s
								s1=a.string.encode("utf-8")+", "+date
								fw.write(s1+"\n")
							else:
								print 'no find h2 a'
						else:
							print 'no find h2'
				else:
					print 'no find typ',a_typ
		except Exception as e:
			print "the error:",e
			dic['msg']="request error: "+str(e)
			dic['status']=0
		begin_page+=1
	fw.close()
	dic['file_name']=file_name
	return dic
if __name__ == "__main__":
	swarm_interestingengineering_industry(int(sys.argv[1]),int(sys.argv[2]))
