#! /usr/bin/python
# _*_ coding: utf-8 _*_

import requests,json,datetime,os.path,hashlib
from mysql import connector

url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson'
r = requests.get(url)
sig = hashlib.md5(r.text.encode('utf-8')).hexdigest()
old_sig = ''

if os.path.exists('eq_sig.txt'):
    with open('eq_sig.txt','r') as fp:
        old_sig = fp.read()
    with open('eq_sig.txt','w') as fp:
        fp.write(sig)
else:
    with open('eq_sig.txt','w') as fp:
        fp.write(sig)

if sig == old_sig:
    print("資料未更新, 不需處理...")
    exit()

earthquakes = json.loads(r.text)
dataset = list()
for eq in earthquakes['features']:
    item = dict()
    et = float(eq['properties']['time'])/1000.0 
    d = datetime.datetime.fromtimestamp(et).strftime('%Y-%m-%d %H-%M-%S')
    item['eqtime'] = d
    item['mag'] = eq['properties']['mag']
    item['place']=eq['properties']['place']
    dataset.append(item)

db = connector.connect(
        host = '127.0.0.1',
        port = '8889',
        user='root',
        passwd='root',
        database='ptest'
)
cur = db.cursor()
cur.execute('delete from eq;')
for data in dataset:
    sqlstr = 'insert into eq (eqtime, mag, place) values("{}",{},"{}");'.format(data['eqtime'],data['mag'],data['place'])
    cur.execute(sqlstr)
    print(sqlstr)
print("資料更新完成")
db.commit()
db.close()





