'''
Its the base of the home page part which creates the basic tables. and braches out to others.
'''
import mysql.connector
con=mysql.connector.connect(host='localhost',password='admin',user='root')

if con.is_connected():
    print('connection with python is established...')
    cr = con.cursor()

    #creating and using database
    
    try:
        cmd='create database Library'
        cr.execute(cmd)
        print('database created')
        
    except mysql.connector.errors.DatabaseError:
        
        print('database already created')
        

    cr.execute('USE Library')

    #creating and using table
    
    try:
        cmd="CREATE TABLE booklist(Slot_No integer(5), Bookname varchar(255),Author varchar(255), Genre varchar(255), Age_Limit varchar(255))"
        cr.execute(cmd)
        print('table created')
    except mysql.connector.errors.DatabaseError:
        print('table already created')
        pass

    cr.execute('table booklist')
    

    #inserting values to booklist
    
    while True:
        slot_no=int(input("Enter Slot no"))
        name=input('Enter name of the book')
        author=input("Enter author name")
        genre=input('Enter genre')
        agelimit=input('Enter age limit')
        print('\n')
        
        insert="insert into booklist values({},'{}','{}','{}','{}')".format(slot_no,name,author,genre,agelimit)
        cr.execute(insert)
        con.commit()

        ch=input('continue?---> c')

        if ch!=c:
            break;
            
        
        
        

    
    
   
      


    
    '''
    cr.execute('select * from booklist')
    booklist=cr.featchall()
     
    for i in booklist:
         print(i)
         '''
        


    
        
    

    
        
    
