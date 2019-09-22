#coding:utf-8
import sys
from bs4 import BeautifulSoup
import requests
import re
# import pymysql
import time
def swarm_bloomberg(begin_page,end_page,year):
	headers = {}
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
	headers["Accept-Encoding"] = "gzip, deflate"
	headers["Upgrade-Insecure-Requests"] = "1"
	file_name='bloomberg_page_'+str(begin_page)+"_to_"+str(end_page)+".txt"
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
	for i in range(begin_page-1,end_page+1):
		offset=i*10
		try:
			#the_conversation,science-and-health
			url = 'https://www.google.com/search?q=opinion+site:https://www.bloomberg.com/opinion&lr=&hl=en&tbs=qdr:y&ei=Z4qHXeChO6aXmwWY576wAw&start='+str(offset)+'&sa=N&ved=0ahUKEwig8aP91uTkAhWmy6YKHZizDzY4FBDy0wMIhAE&biw=1920&bih=342'
			# print url
			req = requests.get(url, headers=headers, timeout=60)
			# req.encoding="utf-8"
			soup = BeautifulSoup((req.text).encode('utf-8'), 'html.parser')
			list = []
			# print req.text
			srg=soup.find('div',attrs={'class':'srg'})
			for item in srg.find_all('div',attrs={"class":"g"}):
				pub_time=""
				title=''
				try:
					div=item.find('div',attrs={"class":'r'})
					if div:
						a=div.find('a')
						if a:
							title=a['href'].encode('utf-8').strip().split('/')[-1]
							title=title.replace('-',' ')
						else:
							print 'div->a no find'
					else:
						print "div no find of title",item
					span=item.find('span',attrs={'class':'f'})
					if span:
						pub_time=span.text.encode('utf-8').strip()
					s="page:"+str(i)+" count: "+str(count)+" title: "+title+" ,"+pub_time
					print s
					if year in pub_time:	#写入指定年份的
						s1=title+" ,"+pub_time
						fw.write(s1+"\n")
					count+=1
				except Exception as e:
					print "find title error:", e,div
					continue
				# if (not h2) or (not a):
				# 	print "not h2 or a"
				# 	continue
		except Exception as e:
			print "parser error:",e,
			dic['msg']="request error: "+str(e)
			dic['status']=0
		time.sleep(10)
	fw.close()
	dic['file_name']=file_name
	return dic
#latest-news,opinion
print "begin_page,end_page,year"
swarm_bloomberg(sys.argv[1],sys.argv[2],sys.argv[3])