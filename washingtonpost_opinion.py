# -*- coding: UTF-8 -*-
import json
import time
import sys
import requests
import os
from bs4.diagnose import diagnose
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit

def download_washingtonpost_opinion(page_begin,page_end,type_name):
	headers = {}
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
	headers["Accept-Encoding"] = "gzip, deflate, br"
	headers["Upgrade-Insecure-Requests"] = "1"
	headers['dnt']="1"
	#网站检查cookie,防止非浏览器访问
	# headers['cookie']='akacd_www=2177452799~rv=27~id=b90d566f2e7ef60c84d7afe2c32fda4d; ak_bmsc=1E2BFD5AEEE3C9149DCDF134A206ACAC686D342D7F0C00000C7DB85C1480245A~plCikRpGmRDKH1ozmsZeuUCYSnFi8wVCEhIDo4rYvLZpZY1w9PAYpizSLA8om27TRfm6iEGAxB72sIfopMiXBWLBkOhcLMMXa/Hp6gBLO0mx2OlfGyUVoKmNX/prl0fuS7A1haCk5ztR5+j3IHeJIO96B2gaAyp+YTDyziGbtjlmXXloYOqTtxuG9Iis4u4Ssn/KCvpXvvNw18qJN+abQn3FyDhqV31Pvc5Y+PQqB65+g=; usn_session_id=5559450840561891; usn_visitor_id=55594508406661476; s_cc=true; s_fid=53CCD88B114578CF-200090CE5C0032A9; _ga=GA1.2.172632290.1555594541; _gid=GA1.2.1541948908.1555594541; __gads=ID=da114bdcf42f75c7:T=1555594553:S=ALNI_MbL49gbkLN_pY4bKleHPrz0PfSDqA; s_sq=%5B%5BB%5D%5D; _parsely_session={%22sid%22:2%2C%22surl%22:%22https://www.usnews.com/news/healthiest-communities/articles/2019-04-18/trump-plan-to-fight-hiv-aids-meets-skepticism-in-atlanta%22%2C%22sref%22:%22https://www.usnews.com/news/national-news%22%2C%22sts%22:1555601489555%2C%22slts%22:1555598003078}; _parsely_visitor={%22id%22:%22d7a0efb0-5ebb-45c7-8e08-77aabc11db9d%22%2C%22session_count%22:2%2C%22last_session_ts%22:1555601489555}; JSESSIONID=F364AFAB60B3A841AA0F95A9733664BB; _gat_tealium_0=1; sailthru_pageviews=4; sailthru_content=c16a6b9b4b4bbe14ad0ef03c8e01ede4bcbf4479891123bf36c55e9aa65e803d; sailthru_visitor=1b034867-4a84-4899-b61a-9ba6ba414784; RT="sl=1&ss=1555597972950&tt=11224&obo=0&bcn=%2F%2F173e2514.akstat.io%2F&sh=1555601505894%3D1%3A0%3A11224%2C1555600335720%3D1%3A0%3A23720&dm=usnews.com&si=193a2b6f-edb4-4980-9398-13f91a1b5a17&ld=1555601505895"; utag_main=v_id:016a30a8852f005003d15b03d48003073002906b00ac2$_sn:3$_ss:0$_st:1555603306014$_prevpage:www.usnews.com%2Fnews%2Fnational-news%3Bexp-1555605106005$_pn:3%3Bexp-session$ses_id:1555600306881%3Bexp-session; bm_sv=21AED741DF7DF3D6BA61E9774F199B2A~/hhbceHPENisDdNFWytQ/0pRJrcwuxQieE7D7bxMI+4D3hAfwVSE2WagUYkVI622I65S2jlrarC8eC87jLLLe15KyWIw/+ozKHM2fJ5Q1r+HIUGK0iRefGkwhVGyu74A+owNM+WTIEvycXq9a+elhl0idDVFVEAokHO+IoaaiIU='
	# headers['cookie']='akacd_www=2177452799~rv=27~id=b90d566f2e7ef60c84d7afe2c32fda4d; ak_bmsc=1E2BFD5AEEE3C9149DCDF134A206ACAC686D342D7F0C00000C7DB85C1480245A~plCikRpGmRDKH1ozmsZeuUCYSnFi8wVCEhIDo4rYvLZpZY1w9PAYpizSLA8om27TRfm6iEGAxB72sIfopMiXBWLBkOhcLMMXa/Hp6gBLO0mx2OlfGyUVoKmNX/prl0fuS7A1haCk5ztR5+j3IHeJIO96B2gaAyp+YTDyziGbtjlmXXloYOqTtxuG9Iis4u4Ssn/KCvpXvvNw18qJN+abQn3FyDhqV31Pvc5Y+PQqB65+g=; usn_session_id=5559450840561891; usn_visitor_id=55594508406661476; s_cc=true; s_fid=53CCD88B114578CF-200090CE5C0032A9; _ga=GA1.2.172632290.1555594541; _gid=GA1.2.1541948908.1555594541; __gads=ID=da114bdcf42f75c7:T=1555594553:S=ALNI_MbL49gbkLN_pY4bKleHPrz0PfSDqA; s_sq=%5B%5BB%5D%5D; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.usnews.com/news/healthiest-communities/articles/2019-04-18/trump-plan-to-fight-hiv-aids-meets-skepticism-in-atlanta%22%2C%22sref%22:%22https://www.usnews.com/news/national-news%22%2C%22sts%22:1555598003078%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22d7a0efb0-5ebb-45c7-8e08-77aabc11db9d%22%2C%22session_count%22:1%2C%22last_session_ts%22:1555598003078}; utag_main=v_id:016a30a8852f005003d15b03d48003073002906b00ac2$_sn:2$_ss:0$_st:1555599998039$_prevpage:www.usnews.com%2Fnews%2Fnational-news%3Bexp-1555601798413$_pn:4%3Bexp-session$ses_id:1555597960952%3Bexp-session; sailthru_pageviews=8; sailthru_content=c16a6b9b4b4bbe14ad0ef03c8e01ede4bcbf4479891123bf36c55e9aa65e803d; sailthru_visitor=1b034867-4a84-4899-b61a-9ba6ba414784; RT="sl=3&ss=1555597956403&tt=71532&obo=1&bcn=%2F%2F173e2513.akstat.io%2F&sh=1555598211875%3D3%3A1%3A71532%2C1555598196063%3D2%3A1%3A55773%2C1555598012183%3D1%3A0%3A55773&dm=usnews.com&si=193a2b6f-edb4-4980-9398-13f91a1b5a17&ld=1555598211875"; JSESSIONID=369BC083F3B1E9B851A50B26953A8026; bm_sv=21AED741DF7DF3D6BA61E9774F199B2A~/hhbceHPENisDdNFWytQ/0pRJrcwuxQieE7D7bxMI+4D3hAfwVSE2WagUYkVI622I65S2jlrarC8eC87jLLLe15KyWIw/+ozKHM2fJ5Q1r+FpFQumH4Twrjebwmof8e6k5SNSXyZOoNvBLuAf2VqlzMQHLtpZAKCbXVZThCKt+Q='
	type_name_dic={}
	type_name_dic['outlook']='outlook'
	type_name_dic['the-posts-view']='opinions/the-posts-view'
	type_name_dic['letters-to-the-editor']='opinions/letters-to-the-editor'
	dic={}
	dic['status']=1
	if str(page_begin).isdigit() == False or str(page_end).isdigit() ==False:
		print "input error: illege input"
		dic['status']=1
		return dic
	page_begin=int(page_begin)
	page_end=int(page_end)
	if page_begin<=0:
		page_begin=1
	if page_end<=0:
		page_end=1
	file_name='washingtonpost_opinion_page_from_'+str(page_begin)+"_to_"+str(page_end)+"_"+str(int(time.time()))+".txt"
	fw=open("download/"+file_name,'w')
	limit=10
	count=0
	for i in range(page_begin,page_end+1):
		offset=(i-1)*limit
		try:
			if type_name=="local-opinions":
				url='https://www.washingtonpost.com/pb/api/v2/render/feature/?service=prism-query&contentConfig={%22url%22:%22prism://prism.query/site,/opinions/local-opinions%22,%22offset%22:'+str(offset)+',%22limit%22:'+str(limit)+'}&customFields={%22isLoadMore%22:true,%22offset%22:0,%22maxToShow%22:10,%22dedup%22:false}&id=f0OLVMlE4mWKvr&rid=&uri=/opinions/local-opinions/'
				# url='https://www.washingtonpost.com/pb/api/v2/render/feature/?service=prism-query&contentConfig={%22url%22:%22prism://prism.query/site,/opinions/local-opinions%22,%22offset%22:5,%22limit%22:10}&customFields={%22isLoadMore%22:true,%22offset%22:0,%22maxToShow%22:10,%22dedup%22:false}&id=f0OLVMlE4mWKvr&rid=&uri=/opinions/local-opinions/'
			elif type_name =='global-opinions':
				url='https://www.washingtonpost.com/pb/api/v2/render/feature/?contentConfig={%22path%22:%22http://www.washingtonpost.com/opinions/?offset='+str(offset)+'%26limit='+str(limit)+'%26query=%2fWashingtonPost%2fProduction%2fDigital%2fQueries%2fsite-service%2fopinions%2fglobal-opinions-front%22}&customFields={%22isLoadMore%22:true,%22showLoadMore%22:true,%22offset%22:0,%22offsetTotal%22:10,%22maxToShow%22:10,%22dedup%22:false}&id=f4Dqas1OzIUKvr&rid=&uri=/global-opinions/'
				# url='https://www.washingtonpost.com/pb/api/v2/render/feature?id=f0Aac2b2PCZvhr&contentConfig=%7B%22path%22%3A%22%2Fopinions%2F%3Fquery%3D%2FWashingtonPost%2FProduction%2FDigital%2FPages-Web%2Fopinions%2F_module-content%2Fglobal-opinions%26limit%3D'+str(limit)+'%26offset%3D'+str(offset)+'%22%7D&uri=/pb/global-opinions/&service=com.washingtonpost.webapps.pagebuilder.services.StoryAdapterService'
			elif type_name=='the-posts-view':
				url='https://www.washingtonpost.com/pb/api/v2/render/feature/section/story-list?content_origin=prism-query&url=prism://prism.query/author,the-posts-view&offset='+str(offset)+'&limit='+str(limit)
			else:
				# url='https://www.washingtonpost.com/pb/api/v2/render/feature?id=fzUfk61n8wBqur&contentConfig=%7B%22path%22%3A%22%2Foutlook%2F%3Flimit%3D15%26offset%3D23%22%7D&uri=/pb/outlook/&service=com.washingtonpost.webapps.pagebuilder.services.StoryAdapterService'
				url='https://www.washingtonpost.com/pb/api/v2/render/feature?id=fzUfk61n8wBqur&contentConfig=%7B%22path%22%3A%22%2F'+type_name_dic[type_name]+'%2F%3Flimit%3D'+str(limit)+'%26offset%3D'+str(offset)+'%22%7D&uri=/pb/'+type_name_dic[type_name]+'/&service=com.washingtonpost.webapps.pagebuilder.services.StoryAdapterService'
			# print url
			req = requests.get(url, headers=headers, timeout=60)
			req.encoding="utf-8"
			# print req.text
			try:
				json_text=json.loads(req.text)
				if json_text.get('rendering'):
					# print json_text['rendering']
					soup = BeautifulSoup(json_text['rendering'].encode('utf-8'), 'lxml')
					try:
						a_list=soup.find_all(name='a',attrs={"data-pb-url-field":"canonical_url"})
						if len(a_list)>0:
							pass
						else:
							# print "web_headline^^^^^^^^^^^^^^^^"
							a_list=soup.find_all(name='a',attrs={"data-pb-local-content-field":"web_headline"})
						for a in a_list:
							count+=1
							href_split=a['href'].split('/')
							date=""
							if len(href_split)>=4:
								date=href_split[-4]+'/'+href_split[-3]+'/'+href_split[-2]
								# print date
							s="page:"+str(i)+" count: "+str(count)+" title: "+a.text.encode('utf-8').strip()+" "+date
							print s
							# print a['href']

							fw.write(s+"\n")
					except Exception as e:
						print "find error:",e
						dic['msg']="line error: "+str(e)
						dic['status']=0

			except Exception as e:
				print "loads error:", e
				# print req.text
				break
		except Exception as e:
			print "request error:", e
			dic['status']=0
			break
	fw.close()
	dic['file_name']=file_name
	return dic



s='letters-to-the-editor'
# s='global-opinions'
# s='local-opinions'
s='the-posts-view'
# s='outlook'
download_washingtonpost_opinion(sys.argv[1],sys.argv[2],s)