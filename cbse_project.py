import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="cbseproject",database='library')
mycursor = mydb.cursor()
'''mycursor.execute("create database library")
mycursor.execute("show databases")
for db in mycursor:
    print(db)
'''
'''mycursor.execute("create table booklist (name varchar(220) , genre varchar(250))")'''
'''for i in range(0,2):
    n=input("enter name:")
    gen = input("enter genre: ")
    ins = "insert into booklist values( '{}' , '{}')".format(n,gen)
    mycursor.execute(ins)
    mycursor.execute("select * from booklist")
    for x in mycursor:
        print(x)
'''
'''ignore comment lines
create ur own database and cursor obj
'''
    
mycursor.execute("create table booklist6 (sn Integer(10), na varchar(220), author varchar(220), gen varchar(220), al varchar(220))")

def entry():    
    b1=[1,"ULYSSES" ,"JAMES JOYCE","FICTION","PG-13"]
    b2=[2,"WAR AND PEACE" ,"LEO TOLSTOY","FICTION","PG-13"]
    b3=[3,"EAST OF EDEN" ,"JOHN STEINBECK","FICTION","R"]
    b4=[4,"THE OLD MAN AND THE SEA" ,"ERNEST HEMINGWAY","FICTION","R"]
    b5=[5,"THE SOUND AND THE FURY" ,"WILLIAM FAULKNER","FICTION","PG-13"]
    b6=[6,"BELOVED" ,"TONI MORRISON","FICTION","PG-13"]
    b7=[7,"THE ILIAD" ,"HOMER","FICTION","UA"]
    b8=[8,"PRIDE AND PREJUDICE" ,"JANE AUSTEN","FICTION","PG-13"]
    b9=[9,"IN SEARCH OF LOST TIME" ,"MARCEL PROUST","FICTION","PG-13"]
    b10=[10,"HUCKLEBERRY FINN" ,"MARK TWAIN","FICTION","PG-13"]
    l=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
    for i in range(10):
        sn=l[i][0]
        name=l[i][1]
        author=l[i][2]
        genre=l[i][3]
        agelimit=l[i][4]
        ins="insert into booklist6 value({},'{}','{}','{}','{}')".format(sn,name,author,genre,agelimit)
        mycursor.execute(ins)
        mydb.commit()
entry()

    















 
