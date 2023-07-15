import mysql.connector as sql
import random as r
print('imported succesfully ')
conn = sql.connect(user = 'root' , password = 'coder' , host = 'localhost' , database ='library')
print('connected successfully')
cursor = conn.cursor()
print('cursor created successfully')

def ViewBooks():
     q = "select * from Books"
     cursor.execute(q)
     data = cursor.fetchall()
     for x in data :
        print(x)
def CheckBook():
     print("1. Search by book Name")
     print("2. Search by book id ")
     choice = int(input("Enter your Choice : "))
     if choice == 1:
        db = []
        user_inp = input("enter the name of the book : ")
        db.append(user_inp)
        q = "select * from books where name = %s"
        cursor.execute(q , db)
        data = cursor.fetchall()
        for x in data :
            print(x)
     if choice == 2 :
        db = []
        Inp = int(input("ENter the Book ID : "))
        db.append(Inp)
        q = "select * from books where Book_ID = %s"
        cursor.execute(q , db)
        dat = cursor.fetchall()
        for x in dat :
            print(x)
def IssueBook():
    db = []
    Inp = int(input("Enter the book ID to be Issued : "))
    db.append(Inp)
    q = "update books set Avaliable = 'no' where Book_ID = %s"
    cursor.execute(q , db)
    conn.commit()
def addbooks():
    db = []
    name = input("enter the name of the book : ")
    db.append(name)
    BookID = int(input("Enter the ID of the book "))
    db.append(BookID)
    q = "insert into books (name , Book_ID , Avaliable) values (%s , %s ,'yes')"
    cursor.execute(q , db)
    conn.commit()
def AddMember():
    db = []
    id = int(input("Enter the ID of the Member : "))
    db.append(id)
    name = input("Enter the name of the Member : ")
    db.append(name)
    till = int(input("Enter the valid date of member : "))
    db.append(till)
    q = "insert into members (ID , name , Valid_Till) values (%s , %s , %s)"
    cursor.execute(q , db)
    conn.commit()
def ViewMember():
    q = "select * from Members"
    cursor.execute(q)
    data = cursor.fetchall()
    for x in data :
        print(x)

while True :
    print("Welcome to Library")
    print("1. Add Member ")
    print("2. View Member ")
    print("3. View books ")
    print("4. check books ")
    print("5. issue books ")
    print("6. add books ")
    print("7. Exit")
    ch = int(int(input("Enter your choice : ")))
    if ch == 1 :
        AddMember()
    if ch == 2 :
        ViewMember()
    if ch == 3 :
        ViewBooks()
    if ch == 4 :
        CheckBook()
    if ch == 5 :
        IssueBook()
    if ch == 6 :
        addbooks()
    if ch == 7 :
        break