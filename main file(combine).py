#PROJECT DONE BY SHATAAYU MOHANTY,ANSUMAN PATRA,ANWESH DASH,SIDDHARTH ANAND,BHOUMES MAHAPATRA
import sys
import mysql.connector
passw=input("Enter your mysql password: ")
mydb = mysql.connector.connect(host='localhost', password=passw, user='root') 

mycursor = mydb.cursor(buffered = True)
cr=mydb.cursor()

try:
        cmd = 'create database library'
        mycursor.execute(cmd)
        cr.execute(cmd)
except mysql.connector.errors.DatabaseError:
        pass
mycursor.execute('USE library')

try:
        cmd = "CREATE TABLE booklist(Slot_No integer(5), Bookname varchar(255),Author varchar(255), Genre varchar(255), Age_Limit varchar(255))"
        mycursor.execute(cmd)
except mysql.connector.errors.DatabaseError:
        pass
try:
        cr.execute("create table oc (name varchar(220) , code varchar(250))")
    
except mysql.connector.errors.ProgrammingError:
        pass

cart=[] #to store the shopping cart of the user


b1 = [1, "ULYSSES", "JAMES JOYCE", "FICTION", "PG-13"]
b2 = [2, "WAR AND PEACE", "LEO TOLSTOY", "FICTION", "PG-13"]
b3 = [3, "EAST OF EDEN", "JOHN STEINBECK", "FICTION", "R"]
b4 = [4, "THE OLD MAN AND THE SEA", "ERNEST HEMINGWAY", "FICTION", "R"]
b5 = [5, "THE SOUND AND THE FURY", "WILLIAM FAULKNER", "FICTION", "PG-13"]
b6 = [6, "BELOVED", "TONI MORRISON", "FICTION", "PG-13"]
b7 = [7, "THE ILIAD", "HOMER", "FICTION", "UA"]
b8 = [8, "PRIDE AND PREJUDICE", "JANE AUSTEN", "FICTION", "PG-13"]
b9 = [9, "IN SEARCH OF LOST TIME", "MARCEL PROUST", "FICTION", "PG-13"]
b10 = [10, "HUCKLEBERRY FINN", "MARK TWAIN", "FICTION", "PG-13"]
b11 = [11, "THE LORD OF THE RINGS", "J.R.R. TOLKIEN", "FICTION", "PG-13"]
b12 = [12, "GAME OF THRONES", "GEORGE R.R. MARTIN", "FICTION", "R"]
b13 = [13, "FRANKENSTEIN", "MARY WOLLSTONECRAFT SHELLY", "SCIENCE FICTION", "PG-13"]
b14 = [14, "JOURNEY TO THE CENTRE OF THE EARTH", "JULES VERNE", "SCIENCE FICTION", "PG-13"]
b15 = [15, "THE TIME MACHINE", "H.G.WELLS", "SCIENCE FICTION", "UA"]
b16 = [16, "STAR WARS", "GEORGE LUCAS", "SCIENCE FRICTON", "PG-13"]
b17 = [17, "BRAVE NEW WORLD", "ALDOUS HUXLEY", "SCIENCE FICTION", "PG-13"]
b18 = [18, "1984", "GEORGE ORWELL", "SCIENCE FICTION", "R"]
b19 = [19, "I, ROBOT", "ISAAC ASIMOV", "SCIENCE FICTION", "PG-13"]
b20 = [20, "FOUNDATION", "SAAC ASIMOV", "SCIENCE FICTION", "PG-13"]
b21 = [21, "THE MARTIN CHRONICLES", "RAY BRADBURY", "SCIENCE FICTION", "PG-13"]
b22 = [22, "FAHRENHEIT 451", "RAY BRADBURY", "SCIENCE FICTION", "PG-13"]
b23 = [23, "PAY DIRT ROAD", "SAMANTHA JAYNE ALLEN", "MYSTERY", "No Age Rating"]
b24 = [24, "THE VIOLIN CONSPIRACY", "BRENDAN SLOCUMB", "MYSTERY", "R"]
b25 = [25, "THE BULLET THAT MISSED", "RICHARD OSMAN", "MYSTERY", "R"]
b26 = [26, "FALLEN", "LINDA CASTILLO", "MYSTERY", "PG-13"]
b27 = [27, "MY SISTER ,THE SERIAL KILLER", "OYINKAN BRAITHWAITE", "MYSTERY", "PG-13"]
b28 = [28, "THE GIRL WITH THE DRAGON TATTOO", "STIEG LARSSON", "MYSTERY", "PG-16"]
b29 = [29, "WHERE THE CRAWDADS SING", "DELIA OWENS", "MYSTERY", "PG-13"]
b30 = [30, "RUNNER", "TRACY CLARK", "MYSTERY", "UA"]
b31 = [31, "REBECCA", "DAPHNE DU MAURIER", "MYSTERY", "PG-13"]
b32 = [32, "GONE GIRL", "GILLIAN FLYNN", "MYSTERY", "R"]
b33 = [33, "IN THE WOODS", "TANA FRENCH", "MYSTERY", "PG-13"]
b34 = [34, "A STUDY IN SCARLET WOMEN", "SHERRY THOMAS", "MYSTERY", "PG-13"]
b35 = [35, "ONE OF THE MONKEY", "JANET EVANOVICH", "MYSTERY", "PG-UA"]
b36 = [36, "THE SIXTH EXTNCTION", "ELIZABETH KOLBERT", "NON FICTION", "UA"]
b37 = [37, "THE YEAR OF MAGICAL THINKING", "JOAN DIDION", "NON FICTION", "Not Given"]
b38 = [38, "BIRTHDAY LETTERS", "TED HUGHES", "NON FICTION", "R"]
b39 = [39, "A BRIEF HISTORY OF TIME", "STEPHEN HAWKING", "NON FICTION", "All Ages"]
b40 = [40, "THE RIGHT STUFF", "TOM WOLFE", "NON FICTION", "UA"]
b41 = [41, "HIROSHIMA", "JOHN HERSEY", "NON FICTION", "UA"]
b42 = [42, "BLACK BOY: A RECORD OF CHILDHOOD AND YOUTH", "RICHARD WRIGHT", "NON FICTION", "PG-15"]
b43 = [43, "THE WASTE LAND", "TS ELIOT", "NON FICTION", "PG-13"]
b44 = [44, "NO LOGO", "NAOMI KLEIN", "NON FICTION", "PG-15"]
b45 = [45, "DREAM FROM MY FATHER", "BARACK OBAMA", "NON FICTION", "PG-13"]
b46 = [46, "THE RIGHT STUFF", "TOM WOLFE", "NON FICTION", "UA"]
b47 = [47, "INTO THE WILD", "LON KRAKAUER", "NON FICTION", "PG-13"]
b48 = [48, "FREAKONOMICS", "STEVEN D. LEVITT AND STEPHEN J. DUBNER", "NON FICTION", "PG-13"]
b49 = [49, "MISTRESS", "AMANDA QUICK", "ROMANCE", "PG-13"]
b50 = [50, "RAVISHED", "AMANDA QUICK", "ROMANCE", "PG-13"]
b51 = [51, "DANGEROUS", "AMANDA QUICK", "ROMANCE", "PG-13"]
b52 = [52, "THE RAVENELS", "LISA KLEYPAS", "ROMANCE", "R"]
b53 = [53, "NIGHT SHIFT", "STEPHEN KING", "HORROR", "UA"]
b54 = [54, "THE OCTOBER COUNTRY", "RAY BRADBURY, JOE MUGNAINA", "HORROR", "Not Rated"]
b55 = [55, "THE BLOOD CHAMBER AND OTHER STORIES", "ANGELA CARTER", "HORROR", "R"]
b56 = [56, "BOOKS OF BLOOD", "CLIVE BARKER", "HORROR", "PG-13"]
b57 = [57, "THE DIARY OF A YOUNG GIRL", "ANNE FRANK", "AUTOBIOGRAPHY", "UA"]
b58 = [58, "BECOMING", "MICHELLE OBAMA", "AUTOBIOGRAPHY", "PG-13"]
b59 = [59, "LONG WALK TO FREEDOM", "NELSON MANDELA", "AUTOBIOGRAPHY", "PG-13"]
b60 = [60, "CHRONICLES", "BOB DYLAN", "AUTOBIOGRAPHY", "PG-13"]
b61 = [61, "WATCHMEN", "ALAN MOORE , DAVE GIBBONMS , JOHN HIGGINS", "GRAPHIC NOVEL", "PG-13"]
b62 = [62, "BATMAN:THE KILLING JOKE", "ALAN MOORE" , "TIM SALE", "GRAPHIC NOVEL", "R"]
b63 = [63, "GHOST WORLD", "DANIEL CLOWES", "GRAPHIC NOVEL", "PG-13"]
b64 = [64, "THE AVENGERS", "STAN LEE", "GRAPHIC NOVEL", "UA"]
b65 = [65, "GOOD OMEN", "NEIL GAIMAN", "FAIRY TALE", "R"]
b66 = [66, "HARRIET HALL AND THE MIRACLE CURE", "SONIA GARRETT", "FAIRY TALE", "UA"]
b67 = [67, "LEAGUE OF LEGENDS", "RIOT GAMES", "FAIRY TALE", "PG-13"]
b68 = [68, "THE QUEEN OF NOTHING", "HOLLY BLACK", "FAIRY TALE", "PG-13"]
b69 = [69, "MAGIC KINGDOM", "ZENITH PUBLISHING", "FAIRY TALE", "UA"]
b70 = [70, "HAMLET", "WILLIAM SHAKESPEARE", "DRAMA", "UA"]
b71 = [71, "ROMEO AND JULIET", "WILLIAM SHAKESPEARE", "DRAMA", "UA"]
b72 = [72, "THE FAULT IN OUR STARS", "JOHN GREEN", "DRAMA", "PG-13"]
b73 = [73, "OTHELLO", "WILLIAM SHAKESPEARE", "DRAMA", "UA"]
b74 = [74, "TWILIGHT", "STEPHENIE MEYER", "DRAMA", "PG-13"]
b75 = [75, "THE PILLARS OF THE EARTH", "KEN FOLLETT", "DRAMA", "R"]
l = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22,b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42,b43, b44, b45, b46, b47, b48, b49, b50, b51, b52, b53, b54, b55, b56, b57, b58, b59, b60, b61, b62,b63, b64, b65, b66, b67, b68, b69, b70, b71, b72, b73, b74, b75]
for i in range(75):
    Slot_No = l[i][0]
    Bookname = l[i][1]
    Author = l[i][2]
    Genre = l[i][3]
    Age_Limit = l[i][4]
    ins = "insert into booklist value({},'{}','{}','{}','{}')".format(Slot_No, Bookname, Author, Genre, Age_Limit)
    mycursor.execute(ins)
    mydb.commit()

def homepage():
    # inserting values to booklist   
    print("\nEnter:", '\n',"1. if you want to publish your book(s)\n\n 2. if you want to Buy a book,\n\n 3. if you want to rent a book\n\n 4. Exit\n")
    Nom = 6
    while Nom not in range(1,5):
            Nom = int(input())
            if Nom in range(1,5):
                            break
            print("invalid input. Please enter a valid number from 1 to 4: ")            
    def publish():
            n = int(input("Num of books you want to publish: "))
            slot_no = len(l)
            for i in range(n):
                slot_no += 1
                Bookname = input('Enter name of book: ')
                author = input('Enter name of the author of book: ')
                genre = input('Enter genre of book: ')
                agelimit = input('Enter age limit: ')
                print('\n')
                ins = "insert into booklist values({},'{}','{}','{}','{}')".format(slot_no, Bookname, author, genre,agelimit)
                mycursor.execute(ins)
                mydb.commit()


    def BuyOrRent():            
            print('\nEnter:\n1. To see Latest in Collection \n2. To see Popular this month  \n3. To Search a book by Genre\n4. View all Books:  ')
            M=6
            multi=0
            while M not in range(1,5):
                    M = int(input())
                    if M in range(1,5):
                            break
                    print("invalid input. Please enter a valid number from 1 to 5 ")
                    
            
            def Latest():
                print("4 books have been added recently:", '\n', "1. JOURNEY TO THE CENTRE OF THE EARTH", '\n',"2. THE HARRY POTTER SERIES", '\n', "3. THE PILLARS OF THE EARTH", '\n','4. GHOST WORLD')
                Bk = ''
                while True:
                        Bk = input("Enter the name of the book to get further details, else press NO: ")
                        Bk=Bk.upper()
                        
                        if Bk == "NO" or Bk == 'no':
                                    print("We see that you are not interested in these books, please select from other options: ") 
                                    BuyOrRent()
                                    break
                        elif Bk not in("JOURNEY TO THE CENTRE OF THE EARTH","THE HARRY POTTER SERIES","THE PILLARS OF THE EARTH","GHOST WORLD"):                        
                              print("Please try again") 
                              continue
                        else:
                                
                                mycursor.execute("select * from booklist where Bookname=%s",(Bk,))
                                for i in mycursor:
                                        print(i)
                                        break
                         
                                if Nom == 2:
                                        print("To buy the book-", Bk, '\t', "You have to pay ₹1000")
                                if Nom == 3:
                                         print("To rent the book-", Bk, '\t', "You have to pay ₹100 per week")
                                cart.append(Bk)        
                                return (Bk)
                                

            def Popular():
                print("\n4 books are popular this month and have been bought by many")
                print("1. MY SISTER, THE SERIAL KILLER")
                print("2. FAHRENHEIT 451")
                print("3. IN SEARCH OF LOST TIME")
                print("4. LEAGUE OF LEGENDS")
                Bk = ''
                while True:
                        
                        Bk = input("Enter the name of the book(in caps), if interested to get further details, else press NO: ")
                        Bk=Bk.upper()
                        
                        if Bk == "NO" or Bk == 'no':
                            print("We see that you are not interested in these books, please select from other options: ") 
                            BuyOrRent()
                            break
                        elif Bk not in("MY SISTER, THE SERIAL KILLER","FAHRENHEIT 451","IN SEARCH OF LOST TIME","LEAGUE OF LEGENDS"):
                                print("Please try again")
                                continue
                        else:
                                
                                mycursor.execute("select * from booklist where Bookname=%s",(Bk,))
                                for i in mycursor:
                                        print(i)
                                        break
                                    
                                
                                if Nom == 2:
                                        print("To buy the book-", Bk, '\t', "You have to pay ₹1000")
                                if Nom == 3:
                                        print("To rent the book-", Bk, '\t', "You have to pay ₹100 per week")
                                cart.append(Bk) 
                                return (Bk)
                        
            def Genre():
                Bk = ''
                print("\nEnter the GENRE you want to read:", "\n", "1)FICTION", '\n', "2)SCIENCE FICTION", '\n', "3)MYSTERY",'\n', "4)NON FICTION", '\n', "5)ROMANCE", '\n', "6)HORROR", '\n', '7)AUTOBIOGRAHY', '\n','8)GRAPHIC NOVEL', '\n', "9)FAIRY TALES", '\n', "10)DRAMA", '\n')
                g = (input()).upper()
                nombor=1
                for i in range(len(l)):
                                if l[i][3]==g:
                                        print(nombor,'.)\t',l[i],sep='')
                                        nombor+=1
                while True:
                        
                        Bk = input("Enter the name of the book you want to buy, if not press NO: ")
                        Bk=Bk.upper()
                
                        if Bk == 'NO' or Bk=="no":
                            gg = input("If u want to read a different genre, enter YES, else enter NO again: ")
                            if gg == "NO":
                               
                                print( "We see that you are not interested in these books, please select from other options: ")  
                                BuyOrRent()
                                break
                            else:
                                Genre()
                                break
                        mycursor.execute("select Bookname from booklist ") 
                        if (Bk,) not in mycursor:
                                print("Please try again")
                                Bk=input()
                                continue                            
                        else:
                            if Nom == 2:
                                print("To buy the book-", Bk, '\t', "You have to pay ₹1000")
                            if Nom == 3:
                                print("To rent the book-", Bk, '\t', "You have to pay ₹100 per week")
                            cart.append(Bk)     
                            return (Bk)
          
            def ViewAll():
                 c=0
                 print("Here are all the books available in the library")
                 for i in l:
                         print(i)
                 while True:
                    Bk = input("Enter the name of the book, if interested to get further details, else press NO: ")
                    Bk=Bk.upper()
                    
                    if Bk == "NO" or Bk == 'no':                        
                        
                        print("We see that you are not interested in these books, please select from other options: \n")
                        BuyOrRent()
                        break
                    for i in l:
                           if Bk==i[1]:
                                   invalid_input=True
                                   break
                           else:
                                   invalid_input=False
                    if invalid_input==False:
                            continue
                    else:
                            break
                 
                 if Nom == 2:
                                print("To buy the book-", Bk, '/t', "You have to pay ₹1000")
                 if Nom == 3:
                                print("To rent the book-", Bk, '/t', "You have to pay ₹100 per week")
                 cart.append(Bk) 
                 return (Bk)

            if M == 1:
                Book_=Latest()
            elif M == 2:
                Book_=Popular()
            elif M == 3:
                Book_=Genre()
            elif M==4:
                Book_=ViewAll()
            return(Book_)

    if Nom == 1:
        publish()
        print("Your book(s) have been successfully published.")
    if Nom == 2:
        book = BuyOrRent()
        
        # direct to checkout fn/end fn
            
    if Nom == 3:
        book = BuyOrRent()
        # direct to checkout fn/end fn
 
                 
    if Nom == 4:
        sys.exit('\n\nThank you for visitng UNREAL LIBRARY.')
    else  :
       while True:
        multi=0
        repeat=input("\n\nEnter A to purchase a book ,\nE to exit the library, \nC to continue with billing:  ")
        if repeat=='A' or repeat=='a':
                BuyOrRent()
                multi=1
        if multi!=1:
                break
        if  repeat=='E' or repeat=='e':
                sys.exit("thank you for visiting us.")

        elif repeat=='C' or repeat=='c':
                break

        
    def bill():      
     if Nom==2: 
        n= len(cart)
        amt = n*1000
        print("\n\n")
        for i in range(n):
            print(i+1,cart[i],"₹1000",sep="\t")
                
        if newcust==0 : # 1 for new cust and 0 for old     
            discode=input("Enter code for discount if you have any code else enter c: ")
            if discode=="UNREAL" or discode == 'unreal':
                amt-=500    
        elif newcust==1:
                print("You got a newcomer discount of ₹200")
                amt-=200
        print("Total amount  = ₹",amt)
        print("Mode of payment will be Cash On Delivery.\nThank you for buying from us")
             
     elif Nom==3:
        r=100
        time=int(input("Enter for how many weeks you want to rent the book: "))
        #code unreal-500 discount
        amt=r*time
        if newcust==0 : # 1 for new cust and 0 for old     
            discode=input("Enter code for discount if you have any code else enter c: ")
            if discode=="UNREAL" or discode == 'unreal':
                amt-=(time*25)    
        elif newcust==1:
                print("You got a newcomer discount of ₹200")
                amt-=(time*20)
        print("Total amount  = ₹",amt)
        print("Mode of payment will be Cash On Delivery.\nThank you for renting a book from us")      
    
    if repeat=='C' or repeat=='c':
            print(cart)
            bill()
            

def default():
    
    a=["Ansuman Patra","1001"]
    b=["Anwesh Dash","1002"]
    c=["Bhoumesh Mohapatra","1003"]
    d=["Shataayu Mohanty","1004"]
    e=["Siddharth Anand","1005"]
    l=[a,b,c,d,e]
    #storing pre defined user values
    for i in range(0,5):
        ins="insert into oc values('{}','{}')".format(l[i][0], l[i][1])
        mycursor.execute(ins)
        mydb.commit()   
    
def time_delay():
    for i in range(500):
        print("",end="")
        
def start_menu():
    wrong_choice=0 
    print("\t\t\t\t\tUNREAL LIBRARY")
    print("WELCOME!")
    time_delay()
    print("Unreal Library is your go-to virtual library for buying,renting and selling books.\n")
    time_delay()
    print("But before that we would like to know if you are an existing user or new user.\n")
    
    ch=input("\n\nIf existing user,enter the user-code or press N for new user: ")
    global newcust
    while True:
            mycursor.execute("select code from oc")
            if ch=="N"or ch =="n":
                    break
            elif (ch,) in mycursor:
                    break
            else:
                    ch=input("Enter again: ")
    if ch=="N" or ch=='n':
            newcust=1
            custname=input("\n\nWelcome aboard!\nPlease enter your name: ")
    else:
                    time_delay()
                    print("\n\nGlad to have you back.\nYou will be receiving a special discount at the end. Just enter the code - 'UNREAL' ")
                    
    print("\nThe books are stored in the format [serial no.,Book name,author,genre,age rating]\n")   
def end_menu():
                global newcust
                time_delay()
                if newcust==1:
                    print("We would like to give you a special reward")
                    cc=input("Please enter a 4 digit user code: ")
                    mycursor.execute("select code from oc")
                                                     
        
                    while True:
                            choice=1                        
                            for existingcode in mycursor:
                                if existingcode == (cc,):
                                        choice=-1
                                        break
                 
                            if choice==-1:
                                print('This user code already exist .Please Try again!')
                                cc=input()
                            else:
                                break
            
                    print("You will be using this code to avail a discount in your next visit")
                
                    ins="insert into oc values('{}','{}')".format(custname,cc)
                    mycursor.execute(ins)
                    mydb.commit()
                elif newcust==0:
                        pass
                cf = input("\nto enter feedback press f and any other key to exit")
                if cf=="f" or cf=="F":            
                        feed=input("Please enter feedback: ")
                        time_delay()
                        print("\nThank you for the feedback and for visiting Unreal Library. We hope you had a great experience")
                else:  
                        print("\nThank you for visiting Unreal Library. We hope you had a great experience")

newcust=0
global multi
bor=0#bor=2 for buying and 3 for renting
custname=''
default()
start_menu()
homepage()    
end_menu()
