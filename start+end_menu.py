import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="cbseproject",database='library')
mycursor = mydb.cursor()
mycursor.execute("use library")
'''mycursor.execute("create table oc (name varchar(220) , code varchar(250))")'''
'''remove the above comment and write it as a line in the main program'''
a=["Ansuman Patra","1001"]
b=["Anwesh Dash","1002"]
c=["Bhoumesh Mohapatra","1003"]
d=["Shataayu Mohanty","1004"]
e=["Siddharth Anand","1005"]
l=[a,b,c,d,e]
for i in range(0,5):
    ins="insert into oc values('{}','{}')".format(l[i][0], l[i][1])
    mycursor.execute(ins)
    mydb.commit()
def time_delay():
    for i in range(800):
        print("",end="")
def start_menu():
    print("\t\t\t\t\tUNREAL LIBRARY")
    x=[]
    mycursor.execute("select code from oc")
    for y in mycursor:
        x.append(y)
    print("WELCOME!")
    time_delay()
    print("Unreal Library is your go-to virtual library for buying and selling books")
    time_delay()
    print("But before that we would like to know if you are an old or new customer.")
    time_delay()    
    ch=input("if old customer,enter the user code  and press  N for new customer: ")
    if ch=="N":
        print("Welcome aboard! Please select buy or sell")
        '''from here connect it to buy/purchase module'''
    elif (ch,) in x:
        time_delay()
        print("Glad to have an old customer back.You will be receiving a special discount at the end. Just enter the code - ABSAS")
        print("buy or sell")
        '''connect to buy and sell'''
    else:
        print("wrong choice")                    


def end_menu():
    print("To enter again press R and any other key to exit: ")
    CH = input()
    if CH =="R"or CH == "r":
        pass
        '''remove this pass statement in the final draft'''
        '''direct the user to the starting'''
    else:
        print("We would like to give you a special reward")
        time_delay()
        nc =input("Please enter your name: ")
        cc=input("Please enter a random code(4digit): ")
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

start_menu()
end_menu()
        







        
