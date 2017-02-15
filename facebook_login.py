from selenium import webdriver

url ='https://www.facebook.com/'

web = webdriver.Firefox()
web.get(url)
web.find_element_by_id('email').send_keys('kkd.alan@gmail.com')
web.find_element_by_id('pass').send_keys('kkd32214@alan')
web.find_element_by_id('loginbutton').click()
print("Facebook login.")


