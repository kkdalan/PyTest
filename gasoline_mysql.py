# _*_ coding: utf-8 _*_
# 程式 gasoline_mysql.py ( Python 3 version)

from mysql import connector

### 主程式
db = connector.connect(
        host = '127.0.0.1',
        port = '8889',
        user='root',
        passwd='root',
        database='ptest'
        )
cur = db.cursor()
sqlstr="select * from prices;"
cur.execute(sqlstr)
rows = list()
for row in cur:
    rows.append(row)

for i in range(0,10):
    print("日期: {}, 92無鉛: {}, 95無鉛: {}, 98無鉛: {}".format(rows[i][0],rows[i][1],rows[i][2],rows[i][3]))
