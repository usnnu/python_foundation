#coding:utf-8


import urllib.request
import selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


url = 'https://www.guazi.com/bj/buy/'

'''
browser = webdriver.PhantomJS()
try:
    browser.get("https://www.taobao.com")
    #time.sleep(5)
    print(browser.page_source)
    browser.close()
    input_first = browser.find_element_by_id("q")
    input_sencond = browser.find_element_by_css_selector("#q")
    input_third = browser.find_element_by_xpath('//*[@id="q"]')
    print(input_first," ",input_sencond,input_third)
except:
    print("error!")
finally:
    print("done!")
'''

urls = ['https://www.taobao.com/','https://www.tmall.com/','https://www.csdn.net/']

time1 = time.time()
try:
    cookie_t = {}
    # 设置浏览器参数，包括无头，代理等
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    #chrome_option.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_option)
    browser.get(url)
    cookie_t['antipas'] = browser.get_cookie('antipas')['value']
    print(cookie_t)
    for _ in urls:
        browser.get(_)
        time.sleep(3)
        with open('xxx.txt','a+',encoding='utf-8') as fi:
            fi.write(browser.page_source)
    
    browser.close()
except:
    print('error')
finally:
    time2 = time.time()
    print(time2-time1)



'''
chromeOptions = webdriver.ChromeOptions()

# 设置代理
chromeOptions.add_argument("--proxy-server=http://202.20.16.82:10152")
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152




'''
