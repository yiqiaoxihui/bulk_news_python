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
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
headers["Accept-Encoding"] = "gzip, deflate"
headers["Upgrade-Insecure-Requests"] = "1"

def swarm_day_detail(year,month,link,fw):
	req = requests.get(link, headers=headers, timeout=60)
	req.encoding="utf-8"
	soup = BeautifulSoup(req.text, 'html.parser')
	episode_core=soup.find(name='div',attrs={'class':'episode-core'})
	if not episode_core:
		print('day->no episode-core')
		return
	for article in episode_core.find_all(name='article',attrs={"class":"rundown-segment"}):
		h3_title=article.find(name='h3',attrs={"class":"rundown-segment__title"})
		if not h3_title:
			print("no episode-core -> article -> h3_title")
			continue
		a_title=h3_title.find(name='a')
		if not a_title:
			print('no episode -> section -> article -> h3_title -> a')
			continue
		title_str=a_title.string.encode('utf-8')
		record_during=article.find(name='time',attrs={'class':'audio-module-duration'})
		if not record_during:
			record_during=''
			print('no episode -> section -> article -> time')
		else:
			record_during=record_during.text.encode('utf-8').strip()
		s= title_str+", "+record_during+', '+year+','+month
		print s
		fw.write(s+'\n')
def swarm_month(year,month,link,fw):
	test_month=month
	next_link=link
	#loop loading next until get full this month
	while int(month) == int(test_month):
		req = requests.get(next_link, headers=headers, timeout=60)
		req.encoding="utf-8"
		soup = BeautifulSoup(req.text, 'html.parser')
		#get this month
		episode_list=soup.find(name='div',attrs={'class':'episode-list'})
		for episode in episode_list.find_all(name='article',attrs={"class":"program-show has-segments has-more-link"}):
			program_show__title=episode.find(name='h2',attrs={"class":"program-show__title"})
			if not program_show__title:
				print('no episode -> program_show__title')
				continue
			day_link_a=program_show__title.find(name='a')
			if not day_link_a:
				print('no episode -> program_show__title -> day_link')
				continue
			day_link=day_link_a['href'].encode('utf-8')
			data_episode_id=episode['data-episode-id'].encode('utf-8')
			data_episode_date=episode['data-episode-date'].encode('utf-8')
			test_month=data_episode_date.split('-')[1]
			next_link='https://www.npr.org/programs/morning-edition/archive?date='+data_episode_date+'&eid='+data_episode_id
			if int(month) == int(test_month):
				#enter full day page to get title
				swarm_day_detail(year,month,day_link,fw)
def swarm_npr(begin_year,end_year):
	file_name='npr_morning-edition'+str(end_year)+'-'+str(begin_year)+".txt"
	dic={}
	dic['status']=1
	dic['msg']="download success"
	fw=open("download/"+file_name,'w')
	current=1
	req = requests.get('https://www.npr.org/programs/morning-edition/archive', headers=headers, timeout=60)
	req.encoding="utf-8"
	# print req.text
	soup = BeautifulSoup(req.text, 'html.parser')
	#get archives
	archive_nav=soup.find(name='nav',attrs={"class":"archive-nav"})
	if not archive_nav:
		print('no find archive_nav!')
		return
	#loop nav year
	for year_div in archive_nav.find_all(name='div',attrs={"class":"year"}):
		year=year_div.find(name='button',attrs={"class":"expand-year"}).string.encode("utf-8")
		ul=year_div.find(name='ul',attrs={'class':'months'})
		if not ul:
			print('no archive_nav -> year -> ul')
			continue
		#loop month
		for li in ul.find_all(name='li'):
			month_link_a=li.find(name='a')
			if not month_link_a:
				print('no archive_nav -> year -> ul -> month_link_a')
				continue
			month_link=month_link_a['href'].encode('utf-8')
			month=month_link.split('?')[-1].split('=')[-1]
			year_str=month.split('-')[2]
			month_str=month.split('-')[0]
			day_str=month.split('-')[1]
			year_int=int(year_str)
			if year_int>=begin_year and year_int <=end_year:
				print('begin '+year_str+'...')
				month_link='https://www.npr.org'+month_link
				swarm_month(year_str,month_str,month_link,fw)
	fw.close()
	dic['file_name']=file_name
	return dic
if __name__ == "__main__":
	typ="business"
	typ="national"
	typ="health"
	typ="technology"
	swarm_npr(int(sys.argv[1]),int(sys.argv[2]))


