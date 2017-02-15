from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen
import requests
import sys, os, time

if len(sys.argv) < 2:
    print("程式: python3 beautiful_soup.py <<target url>>")
    exit(1)

url = sys.argv[1]
domain = "{}://{}".format(urlparse(url).scheme,urlparse(url).hostname)
html = requests.get(url).text
sp = BeautifulSoup(html,'html.parser')

all_links = sp.find_all(['a','img'])
for link in all_links:
    src = link.get('src')
    href = link.get('href')
    targets = [src,href]
    for t in targets:
        if t != None and ('.jpg' in t or '.png' in t):
            if t.startswith('http'): full_path = t
            elif t.startswith('/'): full_path = domain + t
            else: continue
            
            image_dir = url.split('/')[-1]
            if not os.path.exists(image_dir) : os.mkdir(image_dir)
            filename = full_path.split('/')[-1]
            ext = filename.split('.')[-1]
            filename = filename.split('.')[-2]
            filename += ("." + ext)
            image = urlopen(full_path)
            image_path = os.path.join(image_dir,filename)
            fp = open(image_path,'wb')
            fp.write(image.read())
            print("正在寫入: " + image_path , " <- " + full_path)
            fp.close()
