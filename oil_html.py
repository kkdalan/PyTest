# _*_ coding: utf-8 _*_

from bs4 import BeautifulSoup
import requests

pre_html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset = 'utf-8'>
    <title>中油油價歷史資料</title>
</head>
<body>
    <h2>中油油價歷史資料 ( 取自中油官方網站 ) </h2>
    <table width = 600 border = 1>
    <tr><th>日期</th><th>92無鉛</th><th>95無鉛</th><th>98無鉛</th></tr>
'''

post_html = '''
    </table>
</body>
</html>
'''

url = 'http://new.cpc.com.tw/division/mb/oil-more4.aspx'
html = requests.get(url).text
sp = BeautifulSoup(html,'html.parser')
data = sp.find_all('span',{'id':'Showtd'})
rows = data[0].find_all('tr')

prices = list()
for row in rows:
    cols = row.find_all('td')
    if len(cols[1].text) > 0:
        item = [ cols[0].text , cols[1].text , cols[2].text , cols[3].text ]
        prices.append(item)

html_body = ''
for p in prices:
    html_body += "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(p[0],p[1],p[2],p[3])

html_file = pre_html + html_body + post_html
fp = open("oil_price.html",'w')
fp.write(html_file)
fp.close()

print("已產生 oil_price.html")






