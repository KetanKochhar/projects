We need 
1) Python
2) mysql installed to the computer

Command in mysql are :

create database hotel ;
use hotel;

create table coustdata (name char(10) ,  address char(10) , checkin char(10) , checkout char(10) , room char(10) , specs char(10));

create table room (srno int , RoomType char(10) , rent  int);
insert into room values (1 , '1 Bedroom' , 1000);
insert into room values (2 , '2 Bedroom' , 2000);
insert into room values (3 , '1Bed Royal' , 5000);
insert into room values (4 , '2Bed Royal' , 8000);

create table restaurent (srno int , ItemName char(10) , rate int);
insert into restaurent values(1,'tea',10);
insert into restaurent values(2,'coffee',10);
insert into restaurent values(3,'colddrink',10);
insert into restaurent values(4,'samosa',10);
insert into restaurent values(5,'kachori',10);
insert into restaurent values(6,'sandwich',50);
insert into restaurent values(7,'dhokla',30);
insert into restaurent values(8,'milk',20);
insert into restaurent values(9,'noodles',50);
insert into restaurent values(10,'pasta',50);


create table laundary(sno int,itemname char(10),rate int);
insert into laundary values(1,'pant',10);
insert into laundary values(2,'shirt',10);
insert into laundary values(3,'suit',10);
insert into laundary values(4,'sari',10);







