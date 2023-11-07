def p_1():
    import random
    l = []
    while True:
        a = random.randint(1, 10)
        print("random value generated - ", a)
        s = input("to stop press s. press any other letter to continue: ")
        l.append(a)
        if s == "s":
            break
    print("original list - ", l)
    temp=l.copy()
    le=len(temp)
    for i in temp:
        if i%2==1:
            l.remove(i)

    print("new list - ", l)


def p_2():
    def palindrome():
        s = input("enter a string: ")
        if s == s[::-1]:
            print(s, " is a palindrome string")
        else:
            print(s, " is not a palindrome string")

    palindrome()

def p_3():
    def reverse():
        n = int(input("enter number of elements for the list: "))
        l = []
        for i in range(n):
            a = int(input("enter list element: "))
            l.append(a)
        r = l[::-1]
        print("original list - ", l, "\nreverse list - ", r)
    reverse()

def p_4():
    n = int(input("enter number of elements for the list: "))
    l = []
    for i in range(n):
        a = int(input("enter list element: "))
        l.append(a)
    c = 0
    temp = l
    res = []
    for i in l:
        c = 0
        if i in res:
            continue
        for j in temp:
            if i == j:
                c += 1
        if c == 1:
            res.append(i)
        else:
            res.append(i)
            res.append(0)
    print("original list - ", l, "\nnew list - ", res)


def p_5():
    import pickle

    def store():
        f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\employee.dat", 'wb')
        n = int(input("enter number of employees: "))
        for i in range(n):
            enumber = int(input("enter employee number: "))
            name = input("enter name: ")
            sal = float(input("enter salary: "))
            dep = input("enter department: ")
            l = [enumber, name, sal, dep]
            pickle.dump(l, f)
        f.close()

    def average():
        f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\employee.dat", 'rb')
        c = 0
        s = 0
        try:
            while True:
                l = pickle.load(f)
                if l[3] == "accounts":
                    s += l[2]
                    c += 1
        except EOFError:
            print("average = ", s / c)
            f.close()

    store()
    average()

def p_6():
    f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\flower.txt", 'w')
    while True:
        s = input("enter a sentence: ")
        f.write(s)
        ch = input("to stop press S and to continue press any other key: ")
        if ch == "s":
            break
    f.close()
    f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\flower.txt", 'r')
    cc = 0
    c = 0
    for i in f:
        l = i.split()
        for j in l:
            if j == "lily":
                c += 1
        if c > 3:
            cc += 1
        c = 0
    print("number of required lines = ", cc)


def p_7():
    def Newfile():
        f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\online.txt", 'w')
        while True:
            s = input("enter a sentence: ")
            f.write(s)
            f.write(" ")
            ch = input("to stop press S and to continue press any other key: ")
            if ch == "s":
                break
        f.close()

    def Count_t_word():
        f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\online.txt", 'r')
        c = 0
        for i in f:
            l = i.split()
            for j in l:
                if len(j) == 5 and j[0].lower() == "t":
                    c += 1
        print("number of required words = ", c)
        f.close()

    Newfile()
    Count_t_word()

def p_8():
    import pickle
    import os
    def accept_info():
        f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\bank.dat", 'wb')
        for i in range(10):
            accno = int(input("enter account number: "))
            custname = input("enter name: ")
            balance = float(input("enter balance: "))
            l = [accno, custname, balance]
            pickle.dump(l, f)
        f.close()

    def deletion():
        f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\bank.dat", 'rb')
        g = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\bank2.dat", 'wb')
        a = int(input("enter account number to be deleted: "))
        try:
            while True:
                l = pickle.load(f)
                if l[0] == a:
                    print("record deleted successfully")
                    continue
                else:
                    pickle.dump(l, g)
        except EOFError:
            f.close()
            g.close()
            os.remove(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\bank.dat")
            os.rename(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\bank2.dat",
                      r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\bank.dat")

    accept_info()
    deletion()


def p_9():
    import pickle
    def accept_info():
        f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\cinema.dat", 'wb')
        n = int(input("enter number of movies: "))
        for i in range(n):
            dateofrelease = input("enter date of release: ")
            moviename = input("enter name of movie : ")
            movietype = input("enter type of movie: ")
            l = [dateofrelease, moviename, movietype]
            pickle.dump(l, f)
        f.close()

    def display():
        f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\cinema.dat", 'rb')
        try:
            while True:
                l = pickle.load(f)
                if l[2] == "comedy":
                    print(l)
        except EOFError:
            f.close()

    accept_info()
    display()


def p_10():
    import pickle
    def accept_info():
        f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\Directory.dat", 'wb')
        n = int(input("enter number of customers: "))
        for i in range(n):
            telephone = {}
            name = input("enter customer name: ")
            address = input("enter address: ")
            num = int(input("enter mobile number: "))
            telephone["customer_name"] = name
            telephone["address"] = address
            telephone["mobno"] = num
            pickle.dump(telephone, f)
        f.close()

    def display():
        f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\Directory.dat", 'rb')
        try:
            while True:
                telephone = pickle.load(f)
                if str(telephone["mobno"])[0] == "8":
                    print(telephone)
        except EOFError:
            f.close()

    accept_info()
    display()


def p_12():
    import pickle
    def accept():
        f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\student.dat", 'wb')
        n = int(input("enter number of students: "))
        for i in range(n):
            d = {}
            id = int(input("enter id: "))
            name = input("enter student name: ")
            marks = float(input("enter marks: "))
            d["name"] = name
            d["id"] = id
            d["marks"] = marks
            pickle.dump(d, f)
        f.close()
    def update():
        n=int(input("enter id for updation: "))
        m=int(input("enter new marks: "))
        f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\student.dat", 'rb+')
        c=0
        try:
            while True:
                pos=f.tell()
                d = pickle.load(f)
                if d["id"]==n:
                    d["marks"]=m
                    f.seek(pos)
                    pickle.dump(d,f)
                    c+=1
        except EOFError:
            f.close()
            if c==0:
                print("record does not exist")
            else:
                print("marks updated successfully")
    accept()
    update()


def p_13():
    import csv
    def records():
        f = open(r"C:\Users\Ansuman Patra\Dropbox\My PC (Ansuman)\Downloads\employee.csv", 'w', newline="")
        w = csv.writer(f)
        w.writerow(["Enumber", "Ename", "Basic", "DRA", "HRA", "Salary"])
        l = []
        n = int(input("enter number of employees: "))
        for i in range(n):
            enum = int(input("enter employee number: "))
            ename = input("enter employee name: ")
            basic = float(input("enter basic: "))
            da = float(input("enter da: "))
            hra = float(input("enter hra: "))
            sal = basic + da + hra
            l.append([enum, ename, basic, da, hra, sal])
        w.writerows(l)
        f.close()
    records()
p_13()
