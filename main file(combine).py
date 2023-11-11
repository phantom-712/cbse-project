'''
Its the base of the home page part which mycursoreates the basic tables. and braches out to others.
'''
import mysql.connector
mydb=mysql.connector.connect(host='localhost',password='admin',user='root')

if mydb.is_connected():
    print('connection with python is established...')
    mycursor = mydb.cursor()

    #mycursoreating and using database
    
    try:
        cmd='create database Library'
        mycursor.execute(cmd)
        
    except mysql.connector.errors.DatabaseError:
        
        pass
        

    mycursor.execute('USE Library')

    #mycursoreating and using table
    
    try:
        cmd="mycursorEATE TABLE booklist(Slot_No integer(5), Bookname varchar(255),Author varchar(255), Genre varchar(255), Age_Limit varchar(255))"
        mycursor.execute(cmd)
    except mysql.connector.errors.DatabaseError:
        pass

    mycursor.execute('table booklist')
    

    #inserting values to booklist
    
    while True:
        slot_no=int(input("Enter Slot no"))
        name=input('Enter name of the book')
        author=input("Enter author name")
        genre=input('Enter genre')
        agelimit=input('Enter age limit')
        print('\n')
        
        insert="insert into booklist values({},'{}','{}','{}','{}')".format(slot_no,name,author,genre,agelimit)
        mycursor.execute(insert)
        mydb.commit()

        ch=input('continue?---> c')

        if ch!=c:
            break;
            
        
        
        

    
    
   
      


    
    '''
    mycursor.execute('select * from booklist')
    booklist=mycursor.featchall()
     
    for i in booklist:
         print(i)
         '''
        
