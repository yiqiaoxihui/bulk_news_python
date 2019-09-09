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
def swarm_csmonitor(begin_page,end_page):
	headers = {}
	# headers["authority"] = "www.csmonitor.com"
	# headers["scheme"] = "https"
	headers["dnt"] = "1"
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
	headers["Accept-Language"] = "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
	headers["Accept-Encoding"] = "gzip, deflate, br"
	headers["dnt"] = "1"
	
	headers["sec-fetch-mode"] = "navigate"
	headers["sec-fetch-site"] = "same-origin"
	headers["sec-fetch-user"] = "?1"
	headers["upgrade-insecure-requests"] = "1"
	headers['cookie']='_sdsat_aa_user_id=; _ga=GA1.2.1139642498.1564224843; __gads=ID=8906658edbc6081b:T=1564224842:S=ALNI_MZbPo22Y819h0R56CNk0drCGorXOQ; _fbp=fb.1.1564224844777.718198700; __qca=P0-1049037900-1564224844983; __bxtest=xyz; check=true; AMCVS_12F40C0F53DAAEB30A490D45%40AdobeOrg=1; s_dslv_s=More%20than%2030%20days; s_invisit=true; s_vmonthnum=1569859200300%26vn%3D1; s_monthinvisit=true; rvd_s=2; s_ppn=csm%3Acommentary%3Athe%20monitor%27s%20view%3Athe%20monitor%27s%20view; s_cc=true; _gid=GA1.2.1296522007.1568008546; kw.session_ts=1568008546296; _sp_ses.f219=*; AMCV_12F40C0F53DAAEB30A490D45%40AdobeOrg=-330454231%7CMCIDTS%7C18149%7CMCMID%7C01563648913512597572283328570187671947%7CMCAAMLH-1568613434%7C11%7CMCAAMB-1568613434%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C1847208428%7CMCOPTOUT-1568015742s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; mbox=PC#303e1fae45bb4e5182fcb6b4d20c5e85.22_18#1631253344|session#eb27d8dbcfd54bc2a0c1e5806370307d#1568010496; s_depth=3; kw.pv_session=3; _sp_id.f219=1bca6060-355f-45f3-9790-094dabcff05a.1564224845.4.1568008638.1564281746.8805d314-6240-4b24-acf5-f71de48aad7b; xdibx=N4Ig-mBGAeDGCuAnRIBcoAOGAuBnNAjAKwBsAHAAwVkkDMZAnAEwAsANCBgG6wB22aWh1z5UxclTKkWTAOwkO3XHwGomHREgA2aECA5btugPQBhAPYBbSwFN-AQ0QBPY9gAWNgLSXzvAJbY5oi4nlx-NgDuxgAU5gBmcbg22ACUxhQxYZFp9lo6BniE0kysZCzyBLQAvhwQMBiINlxooAAm9k6iANriMqXldARs4pTUxQyyALo14FDQTXaF6DN1cH6turS0JO3Msp5MkPZEnjIM9p5kcZBeNqwMDESyNrJSJJ69JSxlRAwEsiAqkA___; s_ppvl=csm%253Acommentary%253Athe%2520monitor%2527s%2520view%253Athe%2520monitor%2527s%2520view%2C7%2C7%2C468%2C1920%2C468%2C1920%2C1080%2C1%2CP; s_ppv=csm%253Acommentary%253Athe%2520monitor%2527s%2520view%253Athe%2520monitor%2527s%2520view%2C100%2C4%2C7680%2C1920%2C293%2C1920%2C1080%2C1%2CP; s_dslv=1568008744708; s_vnum=1571896744712%26vn%3D2; rvd=1568008744715%3E0%3A1-44%3A1; s_nr=1568008744717-Repeat; s_sq=fcocscsm%3D%2526c.%2526a.%2526activitymap.%2526page%253Dcsm%25253Acommentary%25253Athe%252520monitor%252527s%252520view%25253Athe%252520monitor%252527s%252520view%2526link%253D4%2526region%253Dmain-column%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dcsm%25253Acommentary%25253Athe%252520monitor%252527s%252520view%25253Athe%252520monitor%252527s%252520view%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.csmonitor.com%25252FCommentary%25252Fthe-monitors-view%25252F%252528offset%252529%25252F60%25252F%252528view%252529%25252Fall%2526ot%253DA; s_csmTracking=%7B%22id%22%3A%22368%22%2C%22type%22%3A%22csm_subcategory%22%2C%22byline%22%3A%22%22%2C%22title%22%3A%22-%22%7D'
	file_name='csmonitor_page_'+str(begin_page)+"_to_"+str(end_page)+"_"+str(int(time.time()))+".txt"
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
	if begin_page <= 1:
		begin_page=1
	if end_page <=1:
		end_page=1
	url= 'https://www.csmonitor.com/Commentary/the-monitors-view/(offset)/0/(view)/all'
	fw=open("download/"+file_name,'w')
	for i in range(begin_page,end_page+1):
		# time.sleep(1)
		offset=(i-1)*20
		try:
			temp_url=url
			url = 'https://www.csmonitor.com/Commentary/the-monitors-view/(offset)/'+str(offset)+'/(view)/all'
			# print url
			print url[25:]
			# headers["path"] = url[25:]
			headers["referer"] = temp_url
			req = requests.get(url, headers=headers, timeout=60)
			# req.encoding="utf-8"
			soup = BeautifulSoup((req.text).encode('utf-8'), 'html.parser')
			list = []
			# print req.text
			for item in soup.find_all(name='div',attrs={"class":"ezv-listing ezc-csm-story row with-thumbnail"}):
				# print item
				try:
					h3=item.find('h3',attrs={"class":"story-headline"})
					# print a
				except Exception as e:
					print "find a error:", e
					continue
				if (not h3):
					print "not h3"
					continue
				count+=1
				try:
					a=item.find('a',attrs={})
					a_list=a['href'].encode('utf-8').split('/')
					date=a_list[-3]+'/'+a_list[-2]
				except Exception as e:
					print e
				s="page:"+str(i)+" count: "+str(count)+" title: "+h3.text.encode('utf-8').strip()+","+date
				print s
				fw.write(s+"\n")
		except Exception as e:
			print "parser error:",e
			dic['msg']="request error: "+str(e)
			dic['status']=0
	fw.close()
	dic['file_name']=file_name
	return dic
swarm_csmonitor(sys.argv[1],sys.argv[2])