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

headers["accept"] = "*/*"
headers["content-type"] = "application/json"
headers["DNT"] = '1'
headers["nyt-app-type"] = "project-vi"
headers["nyt-app-version"] = "0.0.5"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
# headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
# headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
# headers["Accept-Encoding"] = "gzip, deflate"
headers["Upgrade-Insecure-Requests"] = "1"
headers["nyt-token"]='MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs+/oUCTBmD/cLdmcecrnBMHiU/pxQCn2DDyaPKUOXxi4p0uUSZQzsuq1pJ1m5z1i0YGPd1U1OeGHAChWtqoxC7bFMCXcwnE1oyui9G1uobgpm1GdhtwkR7ta7akVTcsF8zxiXx7DNXIPd2nIJFH83rmkZueKrC4JVaNzjvD+Z03piLn5bHWU6+w+rA+kyJtGgZNTXKyPh6EC6o5N+rknNMG5+CdTq35p8f99WjFawSvYgP9V64kgckbTbtdJ6YhVP58TnuYgr12urtwnIqWP9KSJ1e5vmgf3tunMqWNm6+AnsqNj8mCLdCuc5cEB74CwUeQcP2HQQmbCddBy2y0mEwIDAQAB'
headers["Origin"] = "https://www.nytimes.com"
headers["Referer"] = "https://www.nytimes.com/section/opinion"
headers["Sec-Fetch-Mode"] = "cors"

def nktime(begin_page,end_page,typ):
	current=1
	fn='download/nktime_'+str(begin_page)+'_'+str(end_page)+'.txt'
	fw=open(fn,'w')
	cursor="YXJyYXljb25uZWN0aW9uOjk="
	ids="/section/"+typ
	while begin_page<=end_page:
		# print current
		extensions={'persistedQuery':{'version':1,'sha256Hash':"d490fe2239efeae11635d7e5e6962377b03897a961aedf1013898c9ab3073934"}}
		variables={'id': ids,'first': 10,'query':{'sort': "newest"},'exclusionMode': "HIGHLIGHTS_AND_EMBEDDED",'cursor':cursor}
		post_json={'operationName':"CollectionsQuery",'variables':variables,'extensions':extensions}
		# post_json={"operationName":"CollectionsQuery","variables":{"id":"/section/science","first":10,"query":{"sort":"best","text":"asd"},"exclusionMode":"NONE"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"d490fe2239efeae11635d7e5e6962377b03897a961aedf1013898c9ab3073934"}}}
		print str(post_json)
		try:
			url='https://et.nytimes.com/?assetUrl=undefined&url=https%3A%2F%2Fwww.nytimes.com%2Fsection%2Fscience&subject=module-interactions&moduleData=%7B%22eventData%22%3A%7B%22pagetype%22%3A%22collection%22%2C%22trigger%22%3A%22module%22%2C%22type%22%3A%22click%22%7D%2C%22moduleObj%22%3A%7B%22name%22%3A%22showMore%22%2C%22context%22%3A%22%22%2C%22label%22%3A%22%22%2C%22region%22%3A%22%22%2C%22element%22%3A%7B%22name%22%3A%22show-more%22%2C%22label%22%3A%22Show%20More%22%2C%22url%22%3A%22%22%7D%7D%7D&parentDatumId=1757f828972dd35d&et2_pageview_id=o8b0Dbd4GV8asAUyUikdsRLd&sourceApp=nyt-vi&gtm=GTM-P528B3-330-Production&assetData=%7B%22wordCount%22%3A0%2C%22id%22%3A100000003695232%2C%22publishedDate%22%3A1433267469000%2C%22publishedTimestamp%22%3A1433267469000%2C%22lastUpdatedTimestamp%22%3A1567190589000%2C%22url%22%3A%22https%3A%2F%2Fwww.nytimes.com%2Fsection%2Fscience%22%2C%22uri%22%3A%22nyt%3A%2F%2Flegacycollection%2Fe3630e88-7801-57be-a9c5-128efad91df1%22%2C%22section%22%3A%22Science%22%2C%22sectionContent%22%3A%22science%22%2C%22contentTone%22%3A%22NEWS%22%2C%22slug%22%3A%22science%22%2C%22source%22%3A%22nyt_cms%22%2C%22derivedDesk%22%3A%22science_desk%22%2C%22type%22%3A%22sectioncollection%22%2C%22languageName%22%3A%22English%22%2C%22languageCode%22%3A%22en%22%2C%22jkiddSrc%22%3A%22fe%22%7D&skipFilter=%5B%22content%22%2C%22jkiddata%22%5D&instant=1&callback=window.EventTracker.cb11'
			requests.get(url, headers=headers, timeout=60)

			url = 'https://a.et.nytimes.com/track'
			track=[]
			# j1={"context_id":"ppQ5UTkjaEJmGgod3hTzTpyL","pageview_id":"o8b0Dbd4GV8asAUyUikdsRLd","event_id":"I6jZaCMaSWyFyxovzQN8BG5a","client_lib":"v1.0.5","sourceApp":"nyt-vi","how":"beacon","client_ts":1567427784591,"data":{"subject":"page_update","viewport":{"scrollTop":5810,"height":336,"width":1920,"documentHeight":6746,"activeTime":0},"gtm":"GTM-P528B3-330-Production","sourceApp":"nyt-vi"}}
			# track.append(j1)
			requests.post(url, data=track,headers=headers)

			url = 'https://samizdat-graphql.nytimes.com/graphql/v2'
			req = requests.post(url, data=post_json,headers=headers)
			# req.encoding="utf-8"
			print "result:",req.text
			try:
				json_text=json.loads(req.text)
				if json_text.get('data'):
					data=json_text['data'].encode('utf-8')
					if data.get('stream'):
						stream=data['stream']
						if stream.get('pageInfo') and stream['pageInfo'].get('endCursor'):
							cursor=stream['pageInfo']['endCursor']
						else:
							print 'no pageInfo or endCursor in stream'
						for item in stream['edges']:
							title=item['node']['headline']['default']
							date=item['node']['firstPublished']
							s=str(current)+" title: "+title.encode("utf-8").strip()+","+date.encode("utf-8").strip()
							print "page:",begin_page,s
							fw.write(s+"\n")
							current+=1
					else:
						print 'no stream in data'
				else:
					print "no data in reply"
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
	nktime(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])