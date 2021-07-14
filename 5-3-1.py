import sqlite3
import simplejson as json
import datetime

#DB 생성
#isolation_level = None -> 이 DB에 코드를 짜는 내용은 자동으로 커밋된다.
#위 옵션이 없다면 conn.commit()으로 커밋을 해줘야 한다
#conn = sqlite3.connect('C:\python\\section5\\databases\\sqlite1.db', isolation_level=None)
conn = sqlite3.connect('C:\python\\section5\\databases\\sqlite1.db')

#DB 생성(메모리DB)
#conn = sqlite3.connect(":memory:")

#날짜 생성
now = datetime.datetime.now()
print('now',now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime',nowDatetime)

#sqlite3 버전확인
print('sqlite3.version', sqlite3.version)
print('sqlite3.sqlite_version', sqlite3.sqlite_version)

#Cursor 연결
c = conn.cursor()
print(type(c))

#테이블 생성(SQLite3 Datatype : TEXT, NUMERIC, INTEGER, REAL, BLOB)
#AUTOINCREMENT를 넣어주면, 예를들어 integer에 넣어주면 자동으로 1,2,3,4....로 된다
c.execute("CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

#데이터삽입
#nowDatatime은 그대로 넣게 되면 ""안으로 들어가서 문자열로 인식이 되어 오류가 난다
#이럴때 맵핑이 필요한데, ?를 넣고 튜플형태로 항목을 추가해 주면 된다
#c.execute("INSERT INTO users VALUES(1, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.co,kr', ?)", (nowDatetime,))

userList = (
    (2, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.co,kr', nowDatetime),
    (3, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.co,kr', nowDatetime),
    (4, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.co,kr', nowDatetime),
)

#c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", userList)

with open('C:\python\\section5\\data\\users.json','r') as infile:
    r = json.load(infile)
    userData = []
    for user in r:
        t = (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDatetime)
        #print('t',t)
        userData.append(t)
    #print('userData',userData)
    #print('userData',tuple(userData))
    #c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", userData)
    #위처럼 써도 튜플로 자동 형변환이 된다.
    c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", tuple(userData))

#print("users db delete", conn.execute("delete from users").rowcount, "rows")
conn.commit()

conn.close()
