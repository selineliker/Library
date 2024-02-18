import sqlite3
file=open('books.txt','a+')

class library:
    def __init__(self, title, author, year, page):
        self.title = title
        self.author = author
        self.year = year
        self.page = page




def add_book():
    state=0
    mylist=[]
    title = input("Title: ")
    with open('books.txt', 'r') as file:
        for line in file:
            books = line.strip().split(",")
            mylist.append(books[0])
        for x in mylist:
            if title == x:
                print(30 * "*")
                print("This book is already registered")
                print(30 * "*")
                state=1
            else:
                continue
        if state==0:
            author = input("Author: ")
            year = input("Year: ")
            page = input("Page: ")
            with open('books.txt', 'a+') as file:
                file.write(f"{title},{author},{year},{page}\n")

            print(30 * "*")
            print("Book is added succesfully")
            print(30 * "*")







def remove_book():
    title = input("Enter title of the book to remove: ")
    lines = []
    with open('books.txt', 'r') as file:
        for line in file:
            if title not in line:
                lines.append(line)

    with open('books.txt', 'w') as file:
        file.writelines(lines)
    print(30*"*")
    print("Book is removed succesfully.")
    print(30*"*")


def show():
    books = []
    with open('books.txt', 'r') as file:
        for line in file:
            book_details = line.strip().split(",")
            if len(book_details) != 4:  # Hata ayıklama adımı: Dört öğe olup olmadığını kontrol et
                print(30 * "*")
                print("Invalid format in line:", line)
                print(30 * "*")
                continue  # Geçersiz formatı olan satırı atla
            books.append(book_details)

    if not books:
        print(30*"*")
        print("There isn't any registered book")
        print(30*"*")
    else:
        for book in books:
            print("Title:",book[0],  ",Author:",book[1])



while True:
    print("""
    ***MENU**
    1) List Books
    2) Add Book
    3) Remove Book
    4) Search
    5) Clean
    6) Quit
    """)

    answer = input("Which number of operations do you want to do (1-4): ")
    if answer == "1":
        show()

    elif answer == '2':
        add_book()

    elif answer == '3':
        remove_book()

    elif answer=='4':
        mylist = []
        title = input("Title: ")
        with open('books.txt', 'r') as file:
            for line in file:
                books = line.strip().split(",")
                mylist.append(books[0])
            for x in mylist:
                state=1
                if title == x:
                    print(30 * "*")
                    print("This book exists")
                    print(30 * "*")
                    state=0
                    break
                else:
                    continue
            if state==1:
                print("This book doesn't exist")

    elif answer=='5':
        with open('books.txt', 'w') as file:
            file.truncate(0)
        print("All books are cleaned")


    elif answer == '6':
        choice = input("if you want to exit please click 'q' please")
        if choice == "q":
            print(30 * "*")
            print("Program is ended")
            print(30 * "*")
            file.close()
            break












