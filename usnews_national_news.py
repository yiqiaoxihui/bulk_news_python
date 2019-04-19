# -*- coding: UTF-8 -*-
import json
import time
import sys
import requests
import os


def download_usnews_national_news(offset,count):
	headers = {}
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
	headers["Accept-Encoding"] = "gzip, deflate, br"
	headers["Upgrade-Insecure-Requests"] = "1"
	headers['dnt']="1"
	headers['host']="www.usnews.com"
	#网站检查cookie,防止非浏览器访问
	headers['cookie']='akacd_www=2177452799~rv=27~id=b90d566f2e7ef60c84d7afe2c32fda4d; ak_bmsc=1E2BFD5AEEE3C9149DCDF134A206ACAC686D342D7F0C00000C7DB85C1480245A~plCikRpGmRDKH1ozmsZeuUCYSnFi8wVCEhIDo4rYvLZpZY1w9PAYpizSLA8om27TRfm6iEGAxB72sIfopMiXBWLBkOhcLMMXa/Hp6gBLO0mx2OlfGyUVoKmNX/prl0fuS7A1haCk5ztR5+j3IHeJIO96B2gaAyp+YTDyziGbtjlmXXloYOqTtxuG9Iis4u4Ssn/KCvpXvvNw18qJN+abQn3FyDhqV31Pvc5Y+PQqB65+g=; usn_session_id=5559450840561891; usn_visitor_id=55594508406661476; s_cc=true; s_fid=53CCD88B114578CF-200090CE5C0032A9; _ga=GA1.2.172632290.1555594541; _gid=GA1.2.1541948908.1555594541; __gads=ID=da114bdcf42f75c7:T=1555594553:S=ALNI_MbL49gbkLN_pY4bKleHPrz0PfSDqA; s_sq=%5B%5BB%5D%5D; _parsely_session={%22sid%22:2%2C%22surl%22:%22https://www.usnews.com/news/healthiest-communities/articles/2019-04-18/trump-plan-to-fight-hiv-aids-meets-skepticism-in-atlanta%22%2C%22sref%22:%22https://www.usnews.com/news/national-news%22%2C%22sts%22:1555601489555%2C%22slts%22:1555598003078}; _parsely_visitor={%22id%22:%22d7a0efb0-5ebb-45c7-8e08-77aabc11db9d%22%2C%22session_count%22:2%2C%22last_session_ts%22:1555601489555}; JSESSIONID=F364AFAB60B3A841AA0F95A9733664BB; _gat_tealium_0=1; sailthru_pageviews=4; sailthru_content=c16a6b9b4b4bbe14ad0ef03c8e01ede4bcbf4479891123bf36c55e9aa65e803d; sailthru_visitor=1b034867-4a84-4899-b61a-9ba6ba414784; RT="sl=1&ss=1555597972950&tt=11224&obo=0&bcn=%2F%2F173e2514.akstat.io%2F&sh=1555601505894%3D1%3A0%3A11224%2C1555600335720%3D1%3A0%3A23720&dm=usnews.com&si=193a2b6f-edb4-4980-9398-13f91a1b5a17&ld=1555601505895"; utag_main=v_id:016a30a8852f005003d15b03d48003073002906b00ac2$_sn:3$_ss:0$_st:1555603306014$_prevpage:www.usnews.com%2Fnews%2Fnational-news%3Bexp-1555605106005$_pn:3%3Bexp-session$ses_id:1555600306881%3Bexp-session; bm_sv=21AED741DF7DF3D6BA61E9774F199B2A~/hhbceHPENisDdNFWytQ/0pRJrcwuxQieE7D7bxMI+4D3hAfwVSE2WagUYkVI622I65S2jlrarC8eC87jLLLe15KyWIw/+ozKHM2fJ5Q1r+HIUGK0iRefGkwhVGyu74A+owNM+WTIEvycXq9a+elhl0idDVFVEAokHO+IoaaiIU='
	# headers['cookie']='akacd_www=2177452799~rv=27~id=b90d566f2e7ef60c84d7afe2c32fda4d; ak_bmsc=1E2BFD5AEEE3C9149DCDF134A206ACAC686D342D7F0C00000C7DB85C1480245A~plCikRpGmRDKH1ozmsZeuUCYSnFi8wVCEhIDo4rYvLZpZY1w9PAYpizSLA8om27TRfm6iEGAxB72sIfopMiXBWLBkOhcLMMXa/Hp6gBLO0mx2OlfGyUVoKmNX/prl0fuS7A1haCk5ztR5+j3IHeJIO96B2gaAyp+YTDyziGbtjlmXXloYOqTtxuG9Iis4u4Ssn/KCvpXvvNw18qJN+abQn3FyDhqV31Pvc5Y+PQqB65+g=; usn_session_id=5559450840561891; usn_visitor_id=55594508406661476; s_cc=true; s_fid=53CCD88B114578CF-200090CE5C0032A9; _ga=GA1.2.172632290.1555594541; _gid=GA1.2.1541948908.1555594541; __gads=ID=da114bdcf42f75c7:T=1555594553:S=ALNI_MbL49gbkLN_pY4bKleHPrz0PfSDqA; s_sq=%5B%5BB%5D%5D; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.usnews.com/news/healthiest-communities/articles/2019-04-18/trump-plan-to-fight-hiv-aids-meets-skepticism-in-atlanta%22%2C%22sref%22:%22https://www.usnews.com/news/national-news%22%2C%22sts%22:1555598003078%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22d7a0efb0-5ebb-45c7-8e08-77aabc11db9d%22%2C%22session_count%22:1%2C%22last_session_ts%22:1555598003078}; utag_main=v_id:016a30a8852f005003d15b03d48003073002906b00ac2$_sn:2$_ss:0$_st:1555599998039$_prevpage:www.usnews.com%2Fnews%2Fnational-news%3Bexp-1555601798413$_pn:4%3Bexp-session$ses_id:1555597960952%3Bexp-session; sailthru_pageviews=8; sailthru_content=c16a6b9b4b4bbe14ad0ef03c8e01ede4bcbf4479891123bf36c55e9aa65e803d; sailthru_visitor=1b034867-4a84-4899-b61a-9ba6ba414784; RT="sl=3&ss=1555597956403&tt=71532&obo=1&bcn=%2F%2F173e2513.akstat.io%2F&sh=1555598211875%3D3%3A1%3A71532%2C1555598196063%3D2%3A1%3A55773%2C1555598012183%3D1%3A0%3A55773&dm=usnews.com&si=193a2b6f-edb4-4980-9398-13f91a1b5a17&ld=1555598211875"; JSESSIONID=369BC083F3B1E9B851A50B26953A8026; bm_sv=21AED741DF7DF3D6BA61E9774F199B2A~/hhbceHPENisDdNFWytQ/0pRJrcwuxQieE7D7bxMI+4D3hAfwVSE2WagUYkVI622I65S2jlrarC8eC87jLLLe15KyWIw/+ozKHM2fJ5Q1r+FpFQumH4Twrjebwmof8e6k5SNSXyZOoNvBLuAf2VqlzMQHLtpZAKCbXVZThCKt+Q='
	dic={}
	dic['status']=1
	if str(offset).isdigit() == False or str(count).isdigit() ==False:
		print "input error: illege input"
		dic['status']=1
		return dic
	offset=int(offset)
	count=int(count)
	current=0
	file_name='usnews_national_new_offset_'+str(offset)+"_count_"+str(count)+"_"+str(int(time.time()))+".txt"
	fw=open("download/"+file_name,'w')
	
	while current<count:
		# print current
		try:
			url = 'https://www.usnews.com/news/business?offset='+str(offset+current)+'&renderer=json'
			# print url
			req = requests.get(url, headers=headers, timeout=60)
			req.encoding="utf-8"
			# print req.text
			try:
				json_text=json.loads(req.text)
				if json_text.get('stories'):
					for item in json_text['stories']:
						try:
							s="start: "+str(offset+current)+" title: "+item['short_headline'].encode("utf-8")+" ,"+item['pubdate'].encode("utf-8")
							print s
							fw.write(s+"\n")
							current+=1
						except Exception as e:
							print "line error:" ,e

			except Exception as e:
				print "loads error:", e
				print req.text
				break
		except Exception as e:
			print "request error:", e
			dic['status']=0
			break
	fw.close()
	dic['file_name']=file_name
	return dic

download_usnews_national_news(sys.argv[1],sys.argv[2])