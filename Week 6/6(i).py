import sqlite3

try:
    conn = sqlite3.connect('test.db')
except Exception as e:
    print("Error in connecting",str(e))

c = conn.cursor()
c.execute("create table students(sname varchar(20), stuid number(10))")

c.execute("insert into students values('A',598)")
c.execute("insert into students values('B',603)")
c.execute("insert into students values('C',574)")

conn.commit()

for row in c.execute("select * from students"):
    print(row)

conn.close()  