
import sqlite3
import datetime
import openpyxl
conn = sqlite3.connect('test.db', isolation_level = None)
nowdatetime = datetime.datetime.now()
print(nowdatetime)
cur = conn.cursor() #cursor생성
cur.execute(("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, usernae TEXT, email TEXT, phone TEXT, web TEXT, regdate TEXT)"))
result = []
#cur.execute("INSERT INTO users VALUES(1,  'love','aqi222@naver.com' ,'010-3957-5034','www.min.co.kr',?)", (nowdatetime,))
#cur.execute("INSERT INTO users VALUES(20,  'dog','aqi222@naver.com' ,'010-3957-5034','www.min.co.kr',?)", (nowdatetime,))
#cur.execute("INSERT INTO users VALUES(30,  'cat','aqi222@naver.com' ,'010-3957-5034','www.min.co.kr',?)", (nowdatetime,))
#cur.execute("INSERT INTO users VALUES(40,  'cute','aqi222@naver.com' ,'010-3957-5034','www.min.co.kr',?)", (nowdatetime,))
cur.execute("SELECT * FROM users")
rows = cur.fetchall()

param1 = ('love',)
cur.execute('SELECT * FROM users WHERE usernae=?', param1) #조건사용하기
print(cur.fetchall())

with conn:
    with open('testdb_dump.sql','w') as f:
        for line in conn.iterdump():
            f.write('%s\n' %line)
        print('Dump print complete.')
conn.commit()

