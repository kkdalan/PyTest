from selenium import webdriver

urls = [
'https://facebook.com',
'https://www.google.com.tw',
'https://ebank.esunbank.com.tw/index.jsp'
]

web = webdriver.Firefox()
web.set_window_position(0,0)
web.set_window_size(800,600)
i = 0
for url in urls:
    web.get(url)
    web.save_screenshot("webpage_{}.png".format(i))
    print("截圖: " + url )
    i += 1
web.quit()
