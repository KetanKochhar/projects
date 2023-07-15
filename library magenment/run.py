import mysql.connector as sql
print('imported succesfully ')
conn = sql.connect(user = 'root' , password = 'coder' , host = 'localhost')
print('connected successfully')
cursor = conn.cursor()
print('cursor created successfully')

cursor.execute("Create database library")
print("database created")

cursor.execute("use library")
print("Using Library")

cursor.execute("create table members (ID int , name char(20) , Valid_Till int)")
print("table members created ")

cursor.execute("create table books (name char(50) , Book_ID int , Avaliable char(5))")
print("table Books created ")
