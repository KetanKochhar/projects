import mysql.connector as sql
print('imported succesfully ')
conn = sql.connect(user = 'root' , password = 'coder' , host = 'localhost')
print('connected successfully')
cursor = conn.cursor()
print('cursor created successfully')

query1 = "create database hotel"
cursor.execute(query1)
print("Created database")

query2 = 'use hotel'
cursor.execute(query2)
print("using data base")

query3 = 'create table coustdata (name char(10) ,  address char(10) , checkin char(10) , checkout char(10) , room char(10) , specs char(10))'
cursor.execute(query3)
print("table created ")

query4 = 'create table room (srno int , RoomType char(10) , rent  int)'
cursor.execute(query4)
print("table created ")

query5 = "insert into room values (1 , '1 Bedroom' , 1000)"
cursor.execute(query5)
conn.commit()
print("inserting")

query6 = "insert into room values (2 , '2 Bedroom ', 2000)"
cursor.execute(query6)
conn.commit()
print("inserting")

query7 = "insert into room values (3 , '1Bed Royal' , 5000)"
cursor.execute(query7)
conn.commit()
print("inserting")

query8 = "insert into room values (4 , '2Bed Royal' , 8000)"
cursor.execute(query8)
conn.commit()
print("inserting")

q1 = "create table restaurent (srno int , ItemName char(10) , rate int)"
cursor.execute(q1)
print("table created ")

q2 = "insert into restaurent values(1,'tea',10)"
cursor.execute(q2)
conn.commit()
print("inserting")

q3 = "insert into restaurent values(2,'coffee',10)"
cursor.execute(q3)
conn.commit()
print("inserting")

q4 = "insert into restaurent values(3,'colddrink',10)"
cursor.execute(q4)
conn.commit()
print("inserting")

q5 = "insert into restaurent values(4,'samosa',10)"
cursor.execute(q5)
conn.commit()
print("inserting")

q6 = "insert into restaurent values(5,'kachori',10)"
cursor.execute(q6)
conn.commit()
print("inserting")

q7 = "insert into restaurent values(6,'sandwich',50)"
cursor.execute(q7)
conn.commit()
print("inserting")

q8 = "insert into restaurent values(7,'dhokla',30)"
cursor.execute(q8)
conn.commit()
print("inserting")

q9 = "insert into restaurent values(8,'milk',20)"
cursor.execute(q9)
conn.commit()
print("inserting")

q10 = "insert into restaurent values(9,'noodles',50)"
cursor.execute(q10)
conn.commit()
print("inserting")

q11 = "insert into restaurent values(10,'pasta',50)"
cursor.execute(q11)
conn.commit()
print("inserting")

q01 = "create table laundary(sno int,itemname char(10),rate int)"
cursor.execute(q01)
print("table created ")

q02 = "insert into laundary values(1,'pant',10)"
cursor.execute(q02)
conn.commit()
print("inserting")

q03 = "insert into laundary values(2,'shirt',10)"
cursor.execute(q02)
conn.commit()
print("inserting")

q04 = "insert into laundary values(3,'suit',10)"
cursor.execute(q02)
conn.commit()
print("inserting")

q05 = "insert into laundary values(4,'sari',10)"
cursor.execute(q02)
conn.commit()
print("inserting")


print("completed mysql commands")
