Nom=int(input("Enter 1. if you want to publish your book/s, 2. if you want to Buy a book, 3. if you want to rent a book"))

def publish():
    n=int(input("Num of books you want to publish"))
    for i in range(n):
        slot_no+=75+1
        name=input('Enter name of book')
        author=input('Enter name of the author of book')
        genre=input('Enter genre of book')
        agelimit=input('Enter age limit')
        print('\n')
        ins="insert into booklist value({},'{}','{}','{}','{}')".format(slot_no,name,author,genre,agelimit)
        cr.execute(ins)
        con.commit()
        
def BuyOrRent():
    g=input("Enter the genre you want to read:","\n","1)FICTION",'/n',"2)SCIENCE FICTION",'/n',"3)MYSTERY",'/n',"4)NON FICTION",'/n',"5)ROMANCE",'/n',"6)HORROR",'/n','7)AUTOBIOGRAHY','/n','8)GRAPHIC NOVEL','/n',"9)FAIRY TALES",'/n',"10)DRAMA",'/n')
    cr.execute("select * from library where Genre=g")
    res=cr.fetchall()
    for i in res:
        b=''
        print(i)
    if Nom==2:
        b=input("Enter the name of the book you want to buy:")
        print("To buy the book-",b,'/t',"You have to pay ₹1000")

    if Nom==3:
        b=input("Enter the name of the book you want to rent:")
        print("To rent the book-",b,'/t',"You have to pay ₹100 per week")
    return(b)
if Nom==1:
    publish()
    print("Congrats! Your book/s have been published.")
if Nom==2:
    booK=BuyOrRent()
    print("Thank you for buying our book-",booK)

if Nom==3:
    booK=BuyOrRent()
    print("Thank you for renting our book-",booK)
    
    
        
        
        
        
    
        
    
    
    
        
        
                
