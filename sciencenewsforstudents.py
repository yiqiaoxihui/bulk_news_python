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
 

def swarm_sciencenewsforstudents(begin_page,end_page):
	current=0

	while begin_page<=end_page:
		# print current
		post_json={'page':str(begin_page),'view_name':'sns_cron_listing','view_display_id':'panel_pane_5','view_args':'','view_path':'home','view_base_path':'','view_dom_id':'ddb9821877522e21e9508e252db8d71f','pager_element':'0','fbclid':'IwAR1EivGKujRv0fgyctjH3XAn3sG3t60VmW8p7kChp5xufzPvr8Qf13QalFU'}
		try:
			url = 'https://www.sciencenewsforstudents.org/views/ajax'
			req = requests.post(url, data=post_json,headers=headers)
			req.encoding="utf-8"
			# print req.text
			try:
				json_text=json.loads(req.text)
				date_json=json_text[2]
				if date_json.get('data'):
					html_data=date_json['data'].encode('utf-8')
					# print html_data
					soup = BeautifulSoup(html_data, 'html.parser')
					# print req.text
					list = []
					for article in soup.find_all(name='div',attrs={"class":"views-row"}):
						try:
							title_div=article.find('div',attrs={"class":"views-field views-field-title"})
							s= "page:"+str(begin_page)+" count:"+str(current)+" title: "+title_div.string.encode("utf-8").strip()#+","+date.encode("utf-8").strip()
							# fw.write(s+"\n")
							print s
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
if __name__ == "__main__":
	swarm_sciencenewsforstudents(int(sys.argv[1]),int(sys.argv[2]))