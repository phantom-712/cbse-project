def p_14():
    s=[]
    top=None
    def isEmpty(stk):
        if len(stk)==0:
            return True
        else:
            return False
        
    def pushit(stk,item):
        global top
        stk.append(item)
        top=len(stk)-1
        
    def popit(stk):
        global top
        if isEmpty(stk):
            print("underflow")
        else:
            x=stk.pop()
            if len(stk)==0:
                top = None
            else:
                top-=1
        return x
    
    d={}
    while True:
        n=input("enter name of city: ")
        p=int(input("enter population: "))
        d[n]=p
        ch=input("to exit press E and to continue press any other key: ")
        if ch.upper()=="E":
            break
    for i in d:
        if d[i]>1000:
            pushit(s,i)
    print("The city names are: ")
    while isEmpty(s)==False:
        a= popit(s)
        print(a)

    
def p_16():
    top=None
    s=[]
    def isEmpty(stk):
        if len(stk)==0:
            return True
        else:
            return False
    def Push(stk,item):
        global top
        stk.append(item)
        top=len(stk)-1
        
    def Pop(stk):
        global top
        if isEmpty(stk):
            print("underflow")
        else:
            x=stk.pop()
            if len(x)==0:
                top=None
            else:
                top-=1
        return x
    enter_string=input("enter a string: ")
    for i in enter_string:
        if i.isupper():
            Push(s,i)
    if isEmpty(s):
        print("No uppercase Letters")
    else:
        print("The upper case letters are-")
        while isEmpty(s)==False:
            a=Pop(s)
            print(a)        

def p_17():
        s=[]
        top=None

        def isEmpty(stk):
            if len(stk)==0:
                return True
            else:
                return False
        def pushit(stk,item):
            global top
            stk.append(item)
            top=len(stk)-1
        def popit(stk):
            global top
            if isEmpty(stk):
                print("underflow")
            else:
                x=stk.pop()
                if len(stk)==0:
                    top=None
                else:
                    top-=1
            return x
        d={}
        for i in range(6):
            n=input("enter name: ")
            m=float(input("enter marks: "))
            d[n]=m
        for i in d:
            if d[i]>75:
                pushit(s,i)
        print("The students who have scored marks greater than 75 are-")
        while isEmpty(s)==False:
            a=popit(s)
            print(a)
p_17()
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="cbseproject",database='library')
mycursor = mydb.cursor()
def p_11():
    def accept(roll):
        mycursor.execute("select roll from student")
        d=mycursor.fetchall()
        if (roll,) in d:
            print("Yes record is present")
        else:
            print("record not present")
    r1=int(input("enter roll number to search: "))
    accept(r1)


        
