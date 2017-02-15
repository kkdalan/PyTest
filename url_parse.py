import requests

url = 'https://udb.moe.edu.tw/Home/About'
html = requests.get(url).text.splitlines()
for i in range(0,len(html)):
    print(html[i])

