#Put this whole program under def homepage()
Nom=int(input("Enter:",'\n'," 1. if you want to publish your book/s\n\n2. if you want to Buy a book,\n\n3. if you want to rent a book\n\n4. Exit"))
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
    dead_end=0
    M=int(input("Enter:",'\n','1. To see Latest in Collection, 2. To see Popular this month, 3 To Search a book by Genre: ')
    def Latest():
        c=0
        print("4 books have been added recently:",'\n',"1. JOURNEY TO THE CENTRE OF THE EARTH",'\n',"2. THE HARRY POTTER SERIES",'\n',"3. THE PILLARS OF THE EARTH (SERIES)",'\n','4. GHOST WORLD')
        Bk=''
        Bk=input("Enter the name of the book, if interested to get further details, else press NO: ")
        if Bk="NO" or Bk='no':
            c+=1
            print("We see that you are not interested in these books, please select from other options: ") #dead end direct to buy or rent menu 
            break
        
        else:
            cr.execute("select * from booklist where name=Bk") #tu table he kichi beneinu ta ae command kahinki use karichu? suggestion: put the 4 books in a list and search for the required book  in that list and display it.
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
        print("1. MY SISTER, THE SERIAL KILLER")
        print("2. FAHRENHEIT 451")
        print("3. IN SEARCH OF LOST TIME")
        print("4. LEAGUE OF LEGENDS")
        Bk=''
        Bk=input("Enter the name of the book, if interested to get further details, else press NO: ")
        if Bk ="NO" or Bk='no':
            c+=1
            print("We see that you are not interested in these books, please select from other options: ")#dead end direct to buy or rent menu 
            break
        else:
            cr.execute("select * from booklist where name=Bk")#same mistake as in 29
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
        cr.execute("select * from booklist where genre=g")# will be refers to the booklist table here not library table.lib is database
        res=cr.fetchall()
        no=1
        for i in res:
            print(no,i)
            no+=1
        
        Bk=input("Enter the name of the book you want to buy, if not press NO: ")
        if  Bk=='NO':
            gg=input("If u want to read a different genre, enter YES, else enter NO again: ")
            if gg="NO":
                c+=1
                print("We see that you are not interested in these books, please select from other options: ")#same mistake as in 26
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
        if c!=0:
            dead_end+=1
    if M==1:
        Latest()
    elif M==2:
        Popular()
    elif M==3:
        Genre()
    if c1!=0:
        Genre()
        
 #c au c1 ra purpose plz explain.   
if dead_end!=0:
    BuyOrRent()
if Nom==1:
    publish()
    print("Your book(s) have been successfully published.")
if Nom==2:
    booK=BuyOrRent()
    print("Thank you for buying our book-",book)
    #direct to checkout fn/end fn
if Nom==3:
    booK=BuyOrRent()
    print("Thank you for renting our book-",book)
    #direct to checkout fn/end fn
if Nom==4:
    print('Thank you for visitng UNREAL LIBRARY.')    
    
    
        
        
        
        
    
        
    
    
    
        
        
                
