import mysql.connector as sql
import random as r
print('imported succesfully ')
conn = sql.connect(user = 'root' , password = 'coder' , host = 'localhost' , database ='library')
print('connected successfully')
cursor = conn.cursor()
print('cursor created successfully')

cursor.execute("insert into members (ID , name , Valid_Till) values (135 , 'abc' , 12032023)")
print("inserted into members sucessfully")
conn.commit()
cursor.execute("insert into members (ID , name , Valid_Till) values (165 , 'def' , 25062023)")
print("inserted into members sucessfully")
conn.commit()
cursor.execute("insert into members (ID , name , Valid_Till) values (186 , 'ghi' , 28022025)")
print("inserted into members sucessfully")
conn.commit()

for q in range(20) :
    a = q+1
    # ('a' , 'b' , 'c' , 'd' , 'e')
    # print(b)
    cursor.execute("insert into books (name , Book_ID , Avaliable ) values ('abc' , 123456 , 'yes')")
    conn.commit()
    print(a , "inserted succesfully")


cursor.execute("insert into books (name , Book_ID , Avaliable ) values ('efd' , 123654 , 'yes')")
conn.commit()
cursor.execute("insert into books (name , Book_ID , Avaliable ) values ('adf' , 854697 , 'yes')")
conn.commit()
cursor.execute("insert into books (name , Book_ID , Avaliable ) values ('fdy' , 524685 , 'yes')")
conn.commit()
cursor.execute("insert into books (name , Book_ID , Avaliable ) values ('fdy' , 74185 , 'yes')")
conn.commit()