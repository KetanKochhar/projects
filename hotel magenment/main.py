import mysql.connector as sql
# print('imported succesfully ')
conn = sql.connect(user = 'root' , password = 'coder' , host = 'localhost' , database = 'hotel')
# print('connected successfully')
cursor = conn.cursor()
# print('cursor created successfully')
CB = [] #list to calculste complete bill
def AddCoust():
    db = []
    name = input("Enter Coustmer name : ")
    db.append(name)
    address = input("Enter Coustmer address : ")
    db.append(address)
    CheckIn = input("Enter Check In date : ")
    db.append(CheckIn)
    CheckOut = input("Enter Check Out Date : ")
    db.append(CheckOut)
    values = (db)
    room = input("Enter the room selected : ")
    db.append(room)
    specs = input("Royal or Normal : ")
    db.append(specs)
    query1 = "insert into coustdata(name , address , checkin , checkout , room , specs)values(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query1,values)
    conn.commit()
    print(db)
    print("added sucessfully")
    
    
#AddCoust()

def RoomType():
    print("Types Of Rooms Avaliable in Our Hotel Are ")
    query2 = "select * from room"
    cursor.execute(query2)
    result = cursor.fetchall()
    for x in result :
        print(x)
#RoomType()


def RoomRent():
    print(" 1 bed room nornal ------> rs 1000 per night")
    print(" 2 bed room nornal ------> rs 2000 per night")
    print(" 1 bed room Royal ------> rs 5000 per night")
    print(" 2 bed room Royal ------> rs 8000 per night")
    RoomType = int(input("which room would you like to choose : "))
    stay = int(input("how long you want to stay : "))
    if RoomType == 1 :
        print("you had choosen 1 bed normal")
        rent = stay*1000
        print('your total room bill is : ',rent)
        
    if RoomType == 2 :
        print("you had choosen 2 bed normal")
        rent = stay*2000
        print('your total room bill is : ',rent)
        #break
    if RoomType == 3 :
        print("you had choosen 1 bed royal")
        rent = stay*5000
        print('your total room bill is : ',rent)
        #break
    if RoomType == 4 :
        print("you had choosen 2 bed royal")
        rent = stay*8000
        print('your total room bill is : ',rent)
    CompleteBill(rent)
        #break
    # else :
    #     print('invalid input')
# RoomRent()

def ViewMenu():
    print("our restaurent menu ")
    query3 = 'select * from restaurent'
    cursor.execute(query3)
    result = cursor.fetchall()
    for x in result:
        print(x)
# ViewMenu()

def OrderItem():
    ViewMenu()
    print('Enter the srno of item you want to order (1 to 10 )')
    order = int(input("Enter your choice : "))
    if order == 1 :
        print("You have order a tea ")
        quantity = int(input("Enter the quantity : "))
        bill = 10*quantity
        print("your restraurent bill is :" , bill)
    if order == 2 :
        print("You have order a coffee ")
        quantity = int(input("Enter the quantity : "))
        bill = 10*quantity
        print("your restraurent bill is :" , bill)
    if order == 3 :
        print("You have order a colddrink ")
        quantity = int(input("Enter the quantity : "))
        bill = 10*quantity
        print("your restraurent bill is :" , bill)
    if order == 4 :
        print("You have order a samosa ")
        quantity = int(input("Enter the quantity : "))
        bill = 10*quantity
        print("your restraurent bill is :" , bill)
    if order == 5 :
        print("You have order a kachori ")
        quantity = int(input("Enter the quantity : "))
        bill = 10*quantity
        print("your restraurent bill is :" , bill)
    if order == 6 :
        print("You have order a sandwich ")
        quantity = int(input("Enter the quantity : "))
        bill = 50*quantity
        print("your restraurent bill is :" , bill)
    if order == 7 :
        print("You have order a dhokla ")
        quantity = int(input("Enter the quantity : "))
        bill = 30*quantity
        print("your restraurent bill is :" , bill)
    if order == 8 :
        print("You have order a milk ")
        quantity = int(input("Enter the quantity : "))
        bill = 20*quantity
        print("your restraurent bill is :" , bill)
    if order == 9 :
        print("You have order a Noodles ")
        quantity = int(input("Enter the quantity : "))
        bill = 50*quantity
        print("your restraurent bill is :" , bill)
    if order == 10 :
        print("You have order a Pasta ")
        quantity = int(input("Enter the quantity : "))
        bill = 50*quantity
        print("your restraurent bill is :" , bill)
    else :
        print("try again ")
    CompleteBill(bill)
# OrderItem()

def ViewLaundary():
    query4 = "Select * from laundary"
    cursor.execute(query4)
    result = cursor.fetchall()
    for x in result :
        print(x)
def LaundaryBill():
    ViewLaundary()
    clothes = int(input("Enter the number of clothes : "))
    LBill = clothes * 10
    print("Your Laundary Bill is : " , LBill)
    CompleteBill(LBill)
# LaundaryBill()

def CompleteBill(x):
    choice = input("DO you want to see this in complte bill ? (y/n)")
    if choice == 'y':
        CB.append(x)
def calCB():
    print("your complete bill is : ", sum(CB))


def Menu():
    print("1. Enter the Coustemer data ")
    print("2. View roomms ")
    print("3. Calculate room bill ")
    print("4. view Restraurent menu ")
    print("5. Calculate restraurent bill ")
    print("6. Calculate laundary bill ")
    print("7. calculate complete bill ")
    print("8. Exit ")
    UserInput = int(input("Enter your choice from above "))
    if UserInput == 1:
        AddCoust()
    if UserInput == 2:
        RoomType()
    if UserInput == 3:
        RoomRent()
    if UserInput == 4:
        ViewMenu()
    if UserInput == 5:
        OrderItem()
    if UserInput == 6:
        LaundaryBill()
    if UserInput == 7:
        calCB()
    if UserInput== 8:
        quit()
    # else :
    #     print("Invalid choice try again")
def Again():
    again = input("Do you want to run again ? (y/n)")
    ragain = again.lower()
    if ragain == "y":
        Menu()
    else :
        print("Thank You ")
        print("You are quiting ")
        quit()
while True :
    Menu()
    Again()
            
conn.close()