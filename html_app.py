import requests

url = 'http://www.com.tw/exam/check_0001_NO_0_101_0_3.html'
html = requests.get(url).text

while True:
    name = input("請輸入要查詢的姓名(q 結束): ")
    if name == 'q': break
    if name in html:
        print("=> 恭喜 {} 名列金榜".format(name))
    else:
        print("=> 不好意思,榜單中找不到 {} 的名字".format(name))


