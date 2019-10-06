# -*- coding: utf-8 -*-

#author		 heaven
#date		 2019/2/1
#脚本描述	 
#脚本使用说明 获取latimes的标题

import json
import time
import sys
import requests
import os
import chardet
from bs4.diagnose import diagnose
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
def latimes(begin_page,end_page,type_name):
	headers = {}
	headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
	headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
	headers["accept-language"] = "zh-CN,zh;q=0.9"
	headers["accept-encoding"] = "gzip, deflate, br"
	headers["upgrade-insecure-requests"] = "1"
	headers['dnt']="1"
	# headers['cookie']='MicrosoftApplicationsTelemetryDeviceId=f368b9cc-f957-c4b6-8eed-f4cf78b9be47; MicrosoftApplicationsTelemetryFirstLaunchTime=1555646377649; _scid=c56e45c5-8aa8-4dea-a5e8-967ccb9b7e50; wsjregion=na%2Cus; usr_bkt=2qgQ1WCa3A; ab_uuid=aea8240b-0366-4126-954b-b682b3e3518e; test_key=0.7220783668882076; optimizelyEndUserId=oeu1555646101426r0.1287645573626417; AMCVS_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=1; s_cc=true; __gads=ID=8b5722181bfee765:T=1555646107:S=ALNI_MbMFEM4gdOTaEUOp9v2CgxLrFeRkA; _ncg_sp_ses.5378=*; _ncg_id_=760f8154-5e60-4ba4-b583-fbb8dc19c673; NaN_hash=af3f02e7HKEKCGNE1555646111871; _mibhv=anon-1555646113976-3777492670_4171; _fbp=fb.1.1555646118325.1982338707; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.wsj.com/news/opinion%22%2C%22sref%22:%22%22%2C%22sts%22:1555646119786%2C%22slts%22:0}; _parsely_visitor={%22id%22:%220285a2cc-91ea-4a41-a628-344c1065181c%22%2C%22session_count%22:1%2C%22last_session_ts%22:1555646119786}; cX_P=jqk9lj5bxylsgx94; cX_S=junjjf1oqs102wdu; _sctr=1|1555603200000; cX_G=cx%3A4gp59eg9a2vx3uo93ast7s9j5%3Afocaobt6urb2; usr_prof_v2=eyJpYyI6Mn0%3D; hok_seg=8m5oogcu3a7n; __qca=P0-603558645-1555646218054; vidoraUserId=eb0rcr800c4gdhd4tib17ksb9lqp6g; AMCV_CB68E4BA55144CAA0A4C98A5%40AdobeOrg=-1891778711%7CMCIDTS%7C18006%7CMCMID%7C91866129217042738901410584778414687528%7CMCAAMLH-1556253665%7C9%7CMCAAMB-1556261647%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1555664047s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.4.0; s_vnum=1558251406684%26vn%3D1; s_invisit=true; gpv_pn=WSJ_infogrfx_interactive_virtual-reality_How%20to%20Watch%20WSJ%20Virtual%20Reality%20%7C%20360%26deg%3B%20Video; s_sq=%5B%5BB%5D%5D; utag_main=v_id:016a33bbb1fc0017d7f6be0b6e7e03073002006b00ac2$_sn:1$_ss:0$_st:1555662280023$ses_id:1555646099966%3Bexp-session$_pn:48%3Bexp-session$_prevpage:WSJ_Summaries_Opinion%3Bexp-1555664080033$vapi_domain:wsj.com; _ncg_sp_id.5378=760f8154-5e60-4ba4-b583-fbb8dc19c673.1555646111.1.1555660532.1555646111.7c5f234d-2c83-48ed-90a0-70e96bb4d7da; GED_PLAYLIST_ACTIVITY=W3sidSI6IlVlV28iLCJ0c2wiOjE1NTU2NjA5OTEsIm52IjowLCJ1cHQiOjE1NTU2NjA0NzQsImx0IjoxNTU1NjYwNTYwfV0'

	file_name='latimes_'+type_name+'_page_'+str(begin_page)+"_to_"+str(end_page)+".txt"
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
	# fw=open("q_format.html",'r')
	for i in range(begin_page,end_page+1):
		try:
			url = 'https://www.latimes.com/topic/'+type_name+'?0000016b-7100-d3a1-a17b-f75ac8440001-p='+str(i)
			req = requests.get(url, headers=headers, timeout=60)
			#problem:使用html.parser解析文档时，遇到日语等字符，无法解析
													#lxml:速度快文档容错能力强
													#html.parser :Python的内置标准库执行速度适中文档容错能力强
			soup = BeautifulSoup(req.text.encode('utf-8'), 'html.parser')	#html5lib:最好的容错性;以浏览器的方式解析文档;生成HTML5格式的文档
			# print soup
			list = []
			# print req.text.encode('utf-8')
			soup=soup.find('body')
			# print soup
			try:
				for item in soup.find_all(name='li',attrs={"class":"ListI-items-item"}):
					# print("*************************")
					# print item.string.encode('utf-8')
					title_div=item.find('div',attrs={'class':'PromoMedium-title'})
					if title_div:
						a=title_div.find('a',attrs={"class":"Link"})
						title=''
						if a:
							title=a.text.encode('utf-8')
						else:
							'no find title a'
					else:
						'no find title div'
					time_lable=item.find('div',attrs={"class":"PromoMedium-timestamp"})
					if time_lable:
						date=time_lable['data-date'].encode('utf-8').strip()
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
		except Exception as e:
			print "request error:",e
			dic['msg']="request error: "+str(e)
			dic['status']=0
	dic['file_name']=file_name
	return dic



latimes(sys.argv[1],sys.argv[2],sys.argv[3])
