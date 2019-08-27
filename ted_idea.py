#coding=utf8
#author		 heaven
#date		 2019/2/1
#脚本描述	 将cnvd漏洞信息导入到数据库中
#脚本使用说明 python swarm_cve.py

import sys
from bs4 import BeautifulSoup
import requests
import re
import json
# import pymysql
import time

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
headers["Accept-Encoding"] = "gzip, deflate"
headers["Upgrade-Insecure-Requests"] = "1"
 

def ted_idea(begin_page,end_page):
	current=1
	fn='download/ted_idea_'+str(begin_page)+'_'+str(end_page)+'.txt'
	fw=open(fn,'w')
	while begin_page<=end_page:
		# print current

		post_json={'page':str(begin_page),'action':'infinite_scroll','order':'DESC','scripts':[],'query_args':{}}
		try:
			url = 'https://ideas.ted.com/?infinity=scrolling'
			req = requests.post(url, data=post_json,headers=headers)
			req.encoding="utf-8"
			# print req.text
			try:
				json_text=json.loads(req.text)
				if json_text.get('html'):
					html_data=json_text['html'].encode('utf-8')
					# print html_data
					soup = BeautifulSoup(html_data, 'html.parser')
					# print req.text
					list = []
					for article in soup.find_all(name='h2',attrs={"class":"block-entry-title"}):
						try:
							# title_div=article.find('div',attrs={"class":"views-field views-field-title"})
							s=str(current)+" title: "+article.string.encode("utf-8").strip()#+","+date.encode("utf-8").strip()
							print "page:",begin_page,s
							fw.write(s+"\n")
							current+=1
						except Exception as e:
							print "title_div",e
							pass
				else:
					print "no data in array 3"
			except Exception as e:
				print "loads error:", e
				#print req.text
				break
		except Exception as e:
			print "error:",e
			# print(e)
		begin_page+=1
	fw.close()
if __name__ == "__main__":
	ted_idea(int(sys.argv[1]),int(sys.argv[2]))