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
import datetime
def swarm_independent(year,type_name):
	headers = {}
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
	headers["Accept-Encoding"] = "gzip, deflate"
	headers["Upgrade-Insecure-Requests"] = "1"
	file_name='independent_page_'+type_name+'_'+str(year)+".txt"
	count=1
	dic={}
	dic['status']=1
	dic['msg']="download success"
	fw=open("download/"+file_name,'w')
	start = year+'-01-01'
	end = year+'-12-31'

	datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
	dateend = datetime.datetime.strptime(end, '%Y-%m-%d')

	while datestart < dateend:
		datestart += datetime.timedelta(days=1)
		date_str=datestart.strftime('%Y-%m-%d')
		# time.sleep(1)
		try:
			# url = 'https://www.independent.com/commentisfree?page='+str(i)
			url = 'https://www.independent.co.uk/archive/'+date_str
			# print url
			req = requests.get(url, headers=headers, timeout=60)
			# req.encoding="utf-8"
			# print (req.text).encode('utf-8')
			soup = BeautifulSoup((req.text).encode('utf-8'), 'html.parser')
			body=soup.find('body')
			ol=body.find('ol',attrs={"class":"archive"})
			# print ol
			content_list=ol.find_all('li')
			for item in content_list:
				
				a=item.find('a',attrs={})
				href=a['href']
				
				# print href
				if href[1:7]==type_name:
					s="count: "+str(count)+" title: "+a.text.encode('utf-8').strip()+' ,'+date_str
					count+=1
					print s
					s1=a.text.encode('utf-8').strip()+' ,'+date_str
					fw.write(s1+"\n")
				#print(a['href'])
				#print(a.string)
		except Exception as e:
			print "parser error:",e
			dic['msg']="request error: "+str(e)
			dic['status']=0
	fw.close()
	dic['file_name']=file_name
	return dic
if __name__ == '__main__':
	if sys.argv[1]=="help":
		print "voices"
		print "lifeandstyle"
		print "environment"
		print "business"
		print "technology"
		print "science"
		print "culture"
		print "sport"
		print "uk-news"
	else:
		swarm_independent(sys.argv[1],sys.argv[2])