import os,requests, re

os.system("clear")

regex ='[a-zA-Z0-9+-._]+@[a-zA-Z0-9+-._]+\.[a-zA-Z0-9+-._]+'
url = 'http://stat.nccu.edu.tw/zh_tw/members'

print("正在解析...", url)
html = requests.get(url).text

emails = re.findall(regex,html)
emails = list(set(emails))
emails.sort()
for email in emails:
    print(email)
