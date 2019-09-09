from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time,os

def swarm_nktimes(begin_page,end_page,typ):

    begin_page=int(begin_page)
    end_page=int(end_page)

    file_name='nktimes_page_'+str(begin_page)+"_to_"+str(end_page)+"_"+typ+".txt"
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
    url='https://www.nytimes.com/section/opinion/'+typ
    driver.get(url)
    try:
        # load = WebDriverWait(driver, 5).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="stream-panel"]/div[1]/div/div/div/button'))

        # )
        load_button=driver.find_element_by_xpath('//*[@id="stream-panel"]/div[1]/div/div/div/button')
        current_count=0
        fw=open(file_name,'w')
        # try:
        for i in range(begin_page,end_page):
            print i,"loding..."
            element = driver.find_element_by_xpath('//*[@id="stream-panel"]/div[1]/div/div/div/button')
            driver.execute_script("arguments[0].click();", element)
            # load_button.click()
            time.sleep(7)
            item_list=driver.find_elements_by_class_name('css-ye6x8s')
            item_count=len(item_list)
            print "current:",current_count,"item_count",item_count
            for index in range(current_count,item_count):
                title_str=''
                date_str=''
                title=item_list[index].find_element_by_class_name('css-1j9dxys')
                if title:
                    title_str=title.text.encode('utf-8')
                date=item_list[index].find_element_by_tag_name('time')
                if date:
                    date_str=date.text.encode('utf-8')
                print index#,"title:",title_str
                s=title_str+','+date_str
                fw.write(s+'\n')
                fw.flush()
                current_count+=1
            
        # except Exception as e:
        #     print "click error",e
        fw.close()
    except Exception as e:
        print "try error:",e
    finally:

        print "quit"
        os.system("pause")
    # driver.quit()
swarm_nktimes(sys.argv[1],sys.argv[2],sys.argv[3])
#driver.find_element_by_xpath('//*[@id="stream-panel"]/div[1]/div/div/div/button').click()