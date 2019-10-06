#coding=utf8
#author		 heaven
#date		 2019/2/1
#脚本描述	 将cnvd漏洞信息导入到数据库中
#脚本使用说明 python swarm_cve.py

from bs4 import BeautifulSoup
import requests
import sys,re
 

def swarm_test():
	headers = {}							#设置headers
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30"
	headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
	headers["Accept-Language"] = "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
	headers["Accept-Encoding"] = "gzip, deflate"
	headers["Upgrade-Insecure-Requests"] = "1"
	try:
		url = 'https://www.baidu.com'			#爬取的指定url
		req = requests.get(url, headers=headers)#使用get方法请求url,同时设置请求头headers
		html_content=req.text.encode('utf-8')
		req.encoding="utf-8"					#返回数据编码为utf-8
		# fw=open('baidu.html','w')
		# fw.write(html_content)
		# fw.close()
		soup = BeautifulSoup(req.text.encode('utf-8'), 'html.parser')		#将requests返回的网页字符串解析成对象soup
		a_object_list=soup.find_all(name='a',attrs={"class":"mnav"})		#查找标签为a，class为mnav的所有对象
		for a_object in a_object_list:										#遍历符合条件的a标签对象
			text_content=a_object.text    									#提取a标签的文本
			a_class=a_object['class']										#eg. 获取a标签的class属性值
			print text_content							    				#打印输出a标签中的文本内容
	except Exception as e:
		print "error:",
		print e

if __name__ == "__main__":
	swarm_test()


