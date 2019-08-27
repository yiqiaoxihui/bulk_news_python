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

def swarm_bigthink(begin_page,end_page,type_name):
	headers = {}
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
	headers["Accept-Encoding"] = "gzip, deflate"
	headers["Upgrade-Insecure-Requests"] = "1"
	file_name='bigthink_page_'+type_name+'_'+str(begin_page)+"_to_"+str(end_page)+"_"+str(int(time.time()))+".txt"
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
	exclude_post_ids='2639797909%2C2637251705%2C2604321755%2C2639613864%2C2639820517%2C2639779672%2C2639820281%2C2631325574%2C2639782794%2C2621597311%2C2639798340%2C2608855035'
	exclude_post_ids_set=set()
	for page in range(begin_page,end_page+1):
		# time.sleep(1)
		try:
			# url = 'https://www.bigthink.com/commentisfree?page='+str(i)
			exclude_post_ids_set_str=''
			for item in exclude_post_ids_set:
				exclude_post_ids_set_str+="%2C"+item
			exclude_post_ids_all=exclude_post_ids+exclude_post_ids_set_str
			url='https://bigthink.com/res/load_more_posts/data.js?site_id=18943713&rm_lazy_load=1&pn='+str(page)+'&exclude_post_ids='+exclude_post_ids_all+'&node_id=%2Froot%2Fblocks%2Fblock%5Btag%5D%2Fabtests%2Fabtest%2Felement_wrapper%2Frow%2Fcolumn%5B1%5D%2Fposts%5B2%5D-&resource_id='+type_name+'&site_id=18943713&path_params=%7B%7D'
			req = requests.get(url, headers=headers, timeout=60)
			# req.encoding="utf-8"
			# print req.text
			# soup = BeautifulSoup((req.text).encode('utf-8'), 'html.parser')
			# list = []
			json_text=json.loads(req.text.encode('utf-8'))
			if json_text.get('posts_by_source'):
				posts_by_source=json_text['posts_by_source']
				# print posts_by_source
				if posts_by_source.get('current_page'):
					current_page=posts_by_source['current_page']
					times=0
					for item in current_page:
						count+=1
						# a=item.find('a',attrs={"class":"u-faux-block-link__overlay js-headline-text"})
						# pub_time=item.find('time',attrs={"class":"fc-item__timestamp"})
						s="page:"+str(page)+" count: "+str(count)+" title: "+item['headline'].encode('utf-8').strip()+' ,'+item['created_date'].encode('utf-8')
						print s
						fw.write(s+"\n")
						exclude_post_ids_set.add(str(item['id']))
						times+=1
						# if times>=3:
						# 	break
				else:
					print "current_page no"
				if posts_by_source.get('popular_24h'):
					popular_24h=posts_by_source['popular_24h']
					times=0
					for item in popular_24h:
						count+=1
						# a=item.find('a',attrs={"class":"u-faux-block-link__overlay js-headline-text"})
						# pub_time=item.find('time',attrs={"class":"fc-item__timestamp"})
						s="popular_24h,page:"+str(page)+" count: "+str(count)+" title: "+item['headline'].encode('utf-8').strip()+' ,'+item['created_date'].encode('utf-8')
						print s
						fw.write(s+"\n")
						exclude_post_ids_set.add(str(item['id']))
						times+=1
						# if times>=3:
						# 	break
				else:
					pass
					# print "popular_24h no"
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
		print "tp_education"
		print "tp_speech"
		print "tp_environment"
		print "tp_business"
		print "tp_technology"
		print "tp_science"
		print "tp_culture"

	else:
		swarm_bigthink(sys.argv[1],sys.argv[2],sys.argv[3])
