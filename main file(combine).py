'''
Its the base of the home page part which mycursoreates the basic tables. and braches out to others.
'''


def homapage():
    import mysql.connector
    mydb = mysql.connector.connect(host='localhost', password='admin', user='root')  # enter your password
    if mydb.is_connected():
        print('connection with python is established...')
        mycursor = mydb.cursor()

        # mycursoreating and using database
    try:
        cmd = 'create database library'
        mycursor.execute(cmd)
    except mysql.connector.errors.DatabaseError:
        pass
    mycursor.execute('USE library')

    # mycursoreating and using table

    try:
        cmd = "mycursorEATE TABLE booklist(Slot_No integer(5), Bookname varchar(255),Author varchar(255), Genre varchar(255), Age_Limit varchar(255))"
        mycursor.execute(cmd)
    except mysql.connector.errors.DatabaseError:
        pass

    mycursor.execute('table booklist')

    # inserting values to booklist
    def booklist_():

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
        b12 = [12, "A GAME OF THRONES", "GEORGE R.R. MARTIN", "FICTION", "R"]
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
        b33 = [33, "IN THE WOODS (Series)", "TANA FRENCH", "MYSTERY", "PG-13"]
        b34 = [34, "A STUDY IN SCARLET WOMEN", "SHERRY THOMAS", "MYSTERY", "PG-13"]
        b35 = [35, "ONE OF THE MONKEY (Series)", "JANET EVANOVICH", "MYSTERY", "PG-UA"]
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
        b46 = [46, "THE RIGHT STUFF (Series)", "TOM WOLFE", "NON FICTION", "UA"]
        b47 = [47, "INTO THE WILD (Series)", "LON KRAKAUER", "NON FICTION", "PG-13"]
        b48 = [48, "FREAKONOMICS (Series)", "STEVEN D. LEVITT AND STEPHEN J. DUBNER", "NON FICTION", "PG-13"]
        b49 = [49, "MISTRESS", "AMANDA QUICK", "ROMANCE", "PG-13"]
        b50 = [50, "RAVISHED", "AMANDA QUICK", "ROMANCE", "PG-13"]
        b51 = [51, "DANGEROUS", "AMANDA QUICK", "ROMANCE", "PG-13"]
        b52 = [52, "THE RAVENELS (Series)", "LISA KLEYPAS", "ROMANCE", "R"]
        b53 = [53, "NIGHT SHIFT", "STEPHEN KING", "HORROR", "UA"]
        b54 = [54, "THE OCTOBER COUNTRY", "RAY BRADBURY, JOE MUGNAINA", "HORROR", "Not Rated"]
        b55 = [55, "THE BLOOD CHAMBER AND OTHER STORIES", "ANGELA CARTER", "HORROR", "R"]
        b56 = [56, "BOOKS OF BLOOD (Series)", "CLIVE BARKER", "HORROR", "PG-13"]
        b57 = [57, "THE DIARY OF A YOUNG GIRL", "ANNE FRANK", "AUTOBIOGRAPHY", "UA"]
        b58 = [58, "BECOMING", "MICHELLE OBAMA", "AUTOBIOGRAPHY", "PG-13"]
        b59 = [59, "LONG WALK TO FREEDOM", "NELSON MANDELA", "AUTOBIOGRAPHY", "PG-13"]
        b60 = [60, "CHRONICLES (Series)", "BOB DYLAN", "AUTOBIOGRAPHY", "PG-13"]
        b61 = [61, "WATCHMEN", "ALAN MOORE , DAVE GIBBONMS , JOHN HIGGINS", "GRAPHIC NOVEL", "PG-13"]
        b62 = [62, "BATMAN:THE KILLING JOKE", "ALAN MOORE , BRIAN BOLLAND , TIM SALE", "GRAPHIC NOVEL", "R"]
        b63 = [63, "GHOST WORLD", "DANIEL CLOWES", "GRAPHIC NOVEL", "PG-13"]
        b64 = [64, "THE AVENGERS (Series)", "STAN LEE", "GRAPHIC NOVEL", "UA"]
        b65 = [65, "GOOD OMEN", "NEIL GAIMAN", "FAIRY TALE", "R"]
        b66 = [66, "HARRIET HALL AND THE MIRACLE CURE", "SONIA GARRETT", "FAIRY TALE", "UA"]
        b67 = [67, "LEAGUE OF LEGENDS", "RIOT GAMES", "FAIRY TALE", "PG-13"]
        b68 = [68, "THE QUEEN OF NOTHING (Series)", "HOLLY BLACK", "FAIRY TALE", "PG-13"]
        b69 = [69, "MAGIC KINGDOM (Series)", "ZENITH PUBLISHING", "FAIRY TALE", "UA"]
        b70 = [70, "HAMLET", "WILLIAM SHAKESPEARE", "DRAMA", "UA"]
        b71 = [71, "ROMEO AND JULIET", "WILLIAM SHAKESPEARE , DR. BARBARA A. MOWAT , PAUL WERSTINE", "DRAMA", "UA"]
        b72 = [72, "THE FAULT IN OUR STARS", "JOHN GREEN", "DRAMA", "PG-13"]
        b73 = [73, "OTHELLO", "WILLIAM SHAKESPEARE", "DRAMA", "UA"]
        b74 = [74, "TWILIGHT (Series)", "STEPHENIE MEYER", "DRAMA", "PG-13"]
        b75 = [75, "THE PILLARS OF THE EARTH (Series)", "KEN FOLLETT", "DRAMA", "R"]
        l = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22,b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42,b43, b44, b45, b46, b47, b48, b49, b50, b51, b52, b53, b54, b55, b56, b57, b58, b59, b60, b61, b62,b63, b64, b65, b66, b67, b68, b69, b70, b71, b72, b73, b74, b75]
        for i in range(75):
            sn = l[i][0]
            name = l[i][1]
            author = l[i][2]
            genre = l[i][3]
            agelimit = l[i][4]
            ins = "insert into booklist6 value({},'{}','{}','{}','{}')".format(sn, name, author, genre, agelimit)
            mycursor.execute(ins)
            mydb.commit()

        print("Enter:", '\n'," 1. if you want to publish your book(s)\n\n2. if you want to Buy a book,\n\n3. if you want to rent a book\n\n4. Exit\n")
        Nom = int(input())
        dead_end = 0

        def publish():
            n = int(input("Num of books you want to publish: "))
            slot_no = 75
            for i in range(n):
                slot_no += 1
                name = input('Enter name of book: ')
                author = input('Enter name of the author of book: ')
                genre = input('Enter genre of book: ')
                agelimit = input('Enter age limit: ')
                print('\n')
                ins = "insert into booklist value({},'{}','{}','{}','{}')".format(slot_no, name, author, genre,
                                                                                  agelimit)
                mycursor.execute(ins)
                mydb.commit()

        c, c1 = 0, 0

        def BuyOrRent():
            dead_end = 0
            print("Enter:", '\n','1. To see Latest in Collection, 2. To see Popular this month, 3 To Search a book by Genre: ')
            M = int(input())

            def Latest():
                c = 0
                print("4 books have been added recently:", '\n', "1. JOURNEY TO THE CENTRE OF THE EARTH", '\n',"2. THE HARRY POTTER SERIES", '\n', "3. THE PILLARS OF THE EARTH (SERIES)", '\n','4. GHOST WORLD')
                Bk = ''
                Bk = input("Enter the name of the book, if interested to get further details, else press NO: ")
                if Bk == "NO" or Bk == 'no':
                    c += 1
                    print("We see that you are not interested in these books, please select from other options: ")

                else:
                    mycursor.execute("select * from booklist where name=Bk")  # tu table he kichi beneinu ta ae command kahinki use karichu? suggestion: put the 4 books in a list and search for the required book  in that list and display it.
                    res = mycursor.fetchall()
                    for i in res:
                        print(i)
                    if Nom == 2:
                        print("To buy the book-", Bk, '/t', "You have to pay ₹1000")

                    if Nom == 3:
                        print("To rent the book-", Bk, '/t', "You have to pay ₹100 per week")
                    return (Bk)

            def Popular():
                c = 0
                print("5 books are popular this month and have been bought by many")
                print("1. MY SISTER, THE SERIAL KILLER")
                print("2. FAHRENHEIT 451")
                print("3. IN SEARCH OF LOST TIME")
                print("4. LEAGUE OF LEGENDS")
                Bk = ''
                Bk = input("Enter the name of the book, if interested to get further details, else press NO: ")
                if Bk == "NO" or Bk == 'no':
                    c += 1
                    print(
                        "We see that you are not interested in these books, please select from other options: ") 
                else:
                    mycursor.execute("select * from booklist where name=Bk")  # same mistake as in 29
                    res = mycursor.fetchall()
                    for i in res:
                        print(i)
                    if Nom == 2:
                        print("To buy the book-", Bk, '/t', "You have to pay ₹1000")
                    if Nom == 3:
                        print("To rent the book-", Bk, '/t', "You have to pay ₹100 per week")
                    return (Bk)

            def Genre():
                c, c1 = 0, 0
                Bk = ''
                print("Enter the genre you want to read:", "\n", "1)FICTION", '/n', "2)SCIENCE FICTION", '/n',
                      "3)MYSTERY",
                      '/n', "4)NON FICTION", '/n', "5)ROMANCE", '/n', "6)HORROR", '/n', '7)AUTOBIOGRAHY', '/n',
                      '8)GRAPHIC NOVEL', '/n', "9)FAIRY TALES", '/n', "10)DRAMA", '/n')
                g = input()
                mycursor.execute(
                    "select * from booklist where genre=g")  # will be refers to the booklist table here not library table.lib is database
                res = mycursor.fetchall()
                no = 1
                for i in res:
                    print(no, i)
                    no += 1

                Bk = input("Enter the name of the book you want to buy, if not press NO: ")
                if Bk == 'NO':
                    gg = input("If u want to read a different genre, enter YES, else enter NO again: ")
                    if gg == "NO":
                        c += 1
                        print(
                            "We see that you are not interested in these books, please select from other options: ")  
                    else:
                        c1 += 1

                else:
                    if Nom == 2:
                        print("To buy the book-", Bk, '/t', "You have to pay ₹1000")
                    if Nom == 3:
                        print("To rent the book-", Bk, '/t', "You have to pay ₹100 per week")
                    return (Bk)

            if c != 0:
                dead_end += 1
            if M == 1:
                Latest()
            elif M == 2:
                Popular()
            elif M == 3:
                Genre()
            if c1 != 0:
                Genre()

        # c au c1 ra purpose plz explain.

        if Nom == 1:
            publish()
            print("Your book(s) have been successfully published.")
        if Nom == 2 and dead_end==0:
            book = BuyOrRent()
            print("Thank you for buying our book-", book)
            # direct to checkout fn/end fn
        if Nom == 3 and dead_end==0:
            book = BuyOrRent()
            print("Thank you for renting our book-", book)
            # direct to checkout fn/end fn
        if Nom == 4:
            print('Thank you for visitng UNREAL LIBRARY.')
        if dead_end != 0:
            BuyOrRent()

            '''check for any further errors/
            +working check karihabani karana tables create hin heini
            last ku sabu compile karila pare check haba'''
