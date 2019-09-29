#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time,os

def swarm_bloomberg(begin_page,end_page,typ):

	begin_page=int(begin_page)
	end_page=int(end_page)

	file_name='bloomberg_page_'+str(begin_page)+"_to_"+str(end_page)+"_"+".txt"
	count=1
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

	driver = webdriver.Chrome()
	driver.implicitly_wait(1)
	url='https://www.google.com/search?q=opinion+site:https://www.bloomberg.com/opinion&lr=&hl=en&tbs=qdr:y&ei=YvuHXd-HCbOKk74Ps4SZkAI&start=0&sa=N&ved=0ahUKEwjfwLncwuXkAhUzxcQBHTNCBiIQ8NMDCL8B&biw=1920&bih=403'
	driver.get(url)
	try:
		# load = WebDriverWait(driver, 5).until(
		#     EC.presence_of_element_located((By.XPATH, '//*[@id="stream-panel"]/div[1]/div/div/div/button'))

		# )
		load_button=driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]')
		current_count=0
		fw=open(file_name,'w')
		# try:
		for i in range(begin_page,end_page):
			print i,"loding..."
			# load_button.click()
			time.sleep(7)
			srg=driver.find_element_by_class_name('srg')
			if srg:
				item_list=srg.find_elements_by_class_name('g')
				item_count=len(item_list)
				for index in range(0,item_count):
					title_str=''
					date_str=''
					title=item_list[index].find_element_by_class_name('LC20lb')	#标题
					if title:
						title_str=title.text.encode('utf-8').strip()
						title_str=title_str.replace(': Opinion - Bloomberg','')
						title_str=title_str.replace('- Bloomberg','')
						if '...' in title_str: 							#显示不全，从链接中 提取
							r=item_list[index].find_element_by_class_name('r')  
							if r:
								a=r.find_element_by_tag_name('a')				#获取链接
								if a:
									title=a.get_attribute('href').encode('utf-8').strip().split('/')[-1]
									title_str=title.replace('-',' ')
								else:
									print 'div->a no find'
							else:
								print "div no find of title",item
					date=item_list[index].find_element_by_class_name('f')
					if date:
					    date_str=date.text.encode('utf-8')[:-2]
					current_count+=1
					print i,current_count,"title:",title_str,',',date_str
					s=title_str+', '+date_str
					fw.write(s+'\n')
					fw.flush()
			else:
				print "no find srg"
			element = driver.find_element_by_xpath('//*[@id="pnnext"]/span[2]')
			driver.execute_script("arguments[0].click();", element)
		fw.close()
	except Exception as e:
		print "try error:",e
	finally:
		print "quit"
		os.system("pause")
	# driver.quit()
swarm_bloomberg(sys.argv[1],sys.argv[2],sys.argv[3])
#driver.find_element_by_xpath('//*[@id="stream-panel"]/div[1]/div/div/div/button').click()