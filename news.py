
from selenium import webdriver
import time

url = 'http://drho.tw/news'
web = webdriver.Firefox()
web.get(url)

for i in range(1,9):
    btn = web.find_element_by_id('btn{}'.format(i))
    print("==> 開始播放: " + btn.text)
    btn.click()
    time.sleep(10)
web.quit()
