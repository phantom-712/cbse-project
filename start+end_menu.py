import mysql.connector
#pass=input('Enter password')
mydb = mysql.connector.connect(host="localhost",user="root",passwd="cbseproject",database='library')#set password as your own device
mycursor = mydb.cursor()
mycursor.execute("use library")
def default():
    try:
        mycursor.execute("create table oc (name varchar(220) , code varchar(250))")
    
    except mysql.connector.errors.ProgrammingError:
        pass
    
    a=["Ansuman Patra","1001"]
    b=["Anwesh Dash","1002"]
    c=["Bhoumesh Mohapatra","1003"]
    d=["Shataayu Mohanty","1004"]
    e=["Siddharth Anand","1005"]
    l=[a,b,c,d,e]
    #storing pre defined user values
    for i in range(0,5):
        ins="insert into oc values('{}','{}')".format(l[i][0], l[i][1])#oc is table under library
        mycursor.execute(ins)
        mydb.commit()   
    
def time_delay():
    for i in range(800):
        print("",end="")
        
def start_menu():
    wrong_choice=0
    print("\t\t\t\t\tUNREAL LIBRARY")
    x=[]
    mycursor.execute("select code from oc")
    for y in mycursor:
        x.append(y)
    print("WELCOME!")
    time_delay()
    print("Unreal Library is your go-to virtual library for buying,renting and selling books")
    time_delay()
    print("But before that we would like to know if you are an existing user or new user.")
    time_delay()    
    ch=input("if existing user,enter the user-code or press N for new user: ")
    if ch=="N":
        print("Welcome aboard! Please  select whether you would like to buy,rent or sell")
        '''from here connect it to buy/purchase module'''
    elif (ch,) in x:#means an existing user
        time_delay()
        print("Glad to have an old customer back.You will be receiving a special discount at the end. Just enter the code - 'UNREAL' ")
        '''connect to buy and sell'''
    else:
        print("Wrong choice! \n Try Again. ")
        wrong_choice=1
        break
        
def end_menu():#calculation  of total amount billing address discount add here.
    print("To enter again press R and any other key to exit: ")
    CH = input()
    if CH =="R"or CH == "r":
        pass
        '''remove this pass statement in the final draft'''
        '''direct the user to the starting not startmenu but home page'''
    else:
        print("We would like to give you a special reward")
        time_delay()
        nc =input("Please enter your name: ")
        while True:
             cc=input("Please enter a user code greater than 2000 (4digit): ")
             mycursor.execute("select code from oc")
             choice=1
             for existingcode in mycursor:
                 if existingcode == (cc,):
                     choice=-1
                  break
                 
             if choice==-1:
                 print('This user code already exist .Please Try again!')
             else:
                 break
        
        print("You will be using this code to avail a discount in your next visit")
        ins="insert into oc values('{}','{}')".format(nc,cc)
        mycursor.execute(ins)
        mydb.commit()
        cf = input("to enter feedback press f and any other key to exit")
        if cf=="f" or cf=="F":            
            feed=input("Please enter feedback: ")
            time_delay()
            print("Thank you for the feedback and for visiting Unreal Library. We hope you had a great experience")
        else:  
            print("Thank you for visiting Unreal Library. We hope you had a great experience")

default()
start_menu()
if wrong_choice!=0:
    start_menu()
hompage()    
end_menu()
        







        
