Nom=int(input("Enter 1. if you want to publish your book/s, 2. if you want to Buy a book, 3. if you want to rent a book"))
def publish():
    n=int(input("Num of books you want to publish: "))
    slot_no=75
    for i in range(n):
        slot_no+=1
        name=input('Enter name of book: ')
        author=input('Enter name of the author of book: ')
        genre=input('Enter genre of book: ')
        agelimit=input('Enter age limit: ')
        print('\n')
        ins="insert into booklist value({},'{}','{}','{}','{}')".format(slot_no,name,author,genre,agelimit)
        cr.execute(ins)
        con.commit()
c,c1=0,0        
def BuyOrRent():
    M=int(input("Enter:",'\n','1 for Search by Latest in Collection, 2 for Search by Popular this month, 3 for Search by Genre: ')
    def Latest():
        c=0
        print("4 books have been added recently:",'\n',"JOURNEY TO THE CENTRE OF THE EARTH",'\n',"THE HARRY POTTER SERIES",'\n',"THE PILLARS OF THE EARTH (SERIES)",'\n','GHOST WORLD')
        Bk=''
        Bk=input("Enter the name of the book, if interested to get further details, else press NO: ")
        if Bk="NO":
            c+=1
            print("We see that you are not interested in these books, please select from other options: ")
            break
        else:
            cr.execute("select * from library where name=Bk")
            res=cr.fetchall()
            for i in res:
                print(i)
            if Nom==2:
                print("To buy the book-",Bk,'/t',"You have to pay ₹1000")

            if Nom==3:
                print("To rent the book-",Bk,'/t',"You have to pay ₹100 per week")
            return(Bk)
    
    def Popular():
        c=0
        print("5 books are popular this month and have been bought by many")
        print("MY SISTER, THE SERIAL KILLER")
        print("FAHRENHEIT 451")
        print("IN SEARCH OF LOST TIME")
        print("LEAGUE OF LEGENDS")
        Bk=''
        Bk=input("Enter the name of the book, if interested to get further details, else press NO: ")
        if Bk ="NO":
            c+=1
            print("We see that you are not interested in these books, please select from other options: ")
            break
        else:
            cr.execute("select * from library where name=Bk")
            res=cr.fetchall()
            for i in res:
                print(i)
            if Nom==2:
                print("To buy the book-",Bk,'/t',"You have to pay ₹1000")
            if Nom==3:
                print("To rent the book-",Bk,'/t',"You have to pay ₹100 per week")
            return(Bk)
    def Genre():
        c=0,c1=0
        Bk=''
        g=input("Enter the genre you want to read:","\n","1)FICTION",'/n',"2)SCIENCE FICTION",'/n',"3)MYSTERY",'/n',"4)NON FICTION",'/n',"5)ROMANCE",'/n',"6)HORROR",'/n','7)AUTOBIOGRAHY','/n','8)GRAPHIC NOVEL','/n',"9)FAIRY TALES",'/n',"10)DRAMA",'/n')
        cr.execute("select * from library where genre=g")
        res=cr.fetchall()
        for i in res:
            print(i)
        
        Bk=input("Enter the name of the book you want to buy, if not press NO: ")
        if  Bk=='NO':
            gg=input("If u want to read a different genre, enter YES, else enter NO again: ")
            if gg="NO":
                c+=1
                print("We see that you are not interested in these books, please select from other options: ")
                break
            else:
                c1+=1
                break
                
        else:
            if Nom==2:
                print("To buy the book-",Bk,'/t',"You have to pay ₹1000")
            if Nom==3:
                print("To rent the book-",Bk,'/t',"You have to pay ₹100 per week")
            return(Bk)
    if M==1:
        Latest()
    if M==2:
        Popular()
    if M==3:
        Genre()
    if c1!=0:
        Genre()
        
    
if c!=0:
    BuyOrRent()
if Nom==1:
    publish()
    print("Congrats! Your book/s have been published.")
if Nom==2:
    booK=BuyOrRent()
    print("Thank you for buying our book-",booK)

if Nom==3:
    booK=BuyOrRent()
    print("Thank you for renting our book-",booK)
    
    
        
        
        
        
    
        
    
    
    
        
        
                
