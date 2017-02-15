# _*_ coding: utf-8 _*_
# score_sqlite.py ( Python 3 version )

import sqlite3, os

def disp_menu():
    print("學生資料編輯")
    print("-----------------")
    print("1. 新增")
    print("2. 編輯")
    print("3. 刪除")
    print("4. 顯示所有學生")
    print("0. 結束")
    print("-----------------")

def append_data():
    while True:
        no = int(input("請輸入學生座號(-1 停止輸入): "))
        if no == -1 : break
        name = input("請輸入學生姓名: ")
        sqlstr = "select * from student where stdno = {};".format(no)
        cursor = conn.execute(sqlstr)
        if len(cursor.fetchall()) > 0 :
            print("您輸入的座號已經有資料")
        else:
            sqlstr = "insert into student values({},'{}');".format(no,name)
            conn.execute(sqlstr)
            conn.commit()

def edit_data():
    no = input("請輸入要編輯的學生座號:")
    sqlstr = "select * from student where stdno = {};".format(no)
    cursor = conn.execute(sqlstr)
    rows = cursor.fetchall()
    if len(rows) > 0 :
        print("目前學生姓名: ", rows[0][1])
        name = input("請輸入學生姓名: ")
        sqlstr = "update student set name = '{}' where stdno = {};".format(name,no)
        conn.execute(sqlstr)
        conn.commit()
    else:
        print("找不到要編輯的學生！")

def del_data():
    no = input("請輸入要刪除的學生座號:")
    sqlstr = "select * from student where stdno = {};".format(no)
    cursor = conn.execute(sqlstr)
    rows = cursor.fetchall()
    print(len(rows))

    if len(rows) > 0 :
        print("您目前要刪除的是座號 {} 的學生 {}: ".format(rows[0][0],rows[0][1]))
        answer = input("確定要刪除嗎？(y/n)")
        if answer.upper() == 'Y':
            sqlstr = "delete from student where stdno = {};".format(no)
            conn.execute(sqlstr)
            conn.commit()
            print("已刪除學生: {}".format(rows[0][1]))
        else:
            print("已取消刪除！")
    else:
        print("找不到要刪除的學生!")

def disp_data():
    sqlstr = "select * from student;"
    cursor = conn.execute(sqlstr)
    for row in cursor:
        print("No {}: {}".format(row[0],row[1]))


### 主程式
conn = sqlite3.connect('score.sqlite')
while True:
    disp_menu()
    try:
        choice = int(input("請輸入您的選擇: "))
        if choice == 1 : 
            append_data()
        elif choice == 2 :
            edit_data()
        elif choice == 3 :
            del_data()
        elif choice == 4 :
            disp_data()
        else:
            print("Good bye!")
            break
    except Exception as e:
        print("錯誤訊息: {}".format(e))

    x = input("請按Enter 鍵回到主選單 ")

