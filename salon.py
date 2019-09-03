import sys
from bs4 import BeautifulSoup
import requests
import re
# import pymysql
import time
def swarm_salon(begin_page,end_page,typ):
	headers = {}
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
	headers["Accept-Encoding"] = "gzip, deflate"
	headers["Upgrade-Insecure-Requests"] = "1"
	file_name='salon_page_'+str(begin_page)+"_to_"+str(end_page)+"_"+str(int(time.time()))+".txt"
	count=1
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
			#the_conversation,science-and-health
			url = 'https://www.salon.com/topic/'+typ+'?sort=new&pagenum='+str(i)
			# print url
			req = requests.get(url, headers=headers, timeout=60)
			# req.encoding="utf-8"
			soup = BeautifulSoup((req.text).encode('utf-8'), 'html.parser')
			list = []
			# print req.text
			for item in soup.find_all('div',attrs={"class":"card-article"}):
				pub_time=""
				try:
					h2=item.find('h2',attrs={})

					a=item.find('a',attrs={})
					if a:
						href_list=a['href'].encode('utf-8').split('/')
						pub_time=href_list[1]+'/'+href_list[2]+'/'+href_list[3]
					s="page:"+str(i)+" count: "+str(count)+" title: "+h2.text.encode('utf-8').strip()+" ,"+pub_time
					print s
					fw.write(s+"\n")
					count+=1
				except Exception as e:
					print "find title error:", e,h2
					continue

				# if (not h2) or (not a):
				# 	print "not h2 or a"
				# 	continue
		except Exception as e:
			print "parser error:",e
			dic['msg']="request error: "+str(e)
			dic['status']=0
	fw.close()
	dic['file_name']=file_name
	return dic
#latest-news,opinion
swarm_salon(sys.argv[1],sys.argv[2],sys.argv[3])
