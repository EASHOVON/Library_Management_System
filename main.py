class User:
    allUsers = []
    def __init__(self,name,roll,password) -> None:
        self.name = name
        self.roll = roll
        self.password = password
        self.borrow_books = []
        self.returned_books = []

class Library:
    def __init__(self,book_list) -> None:
        self.book_list = book_list
    def borrow_books(self,bookName,user):
        for book in self.book_list:
            if book == bookName:
                if bookName in user.borrow_books:
                    print("Boi Age Niso, Ferot Daw!")
                    return
                if self.book_list[book]==0:
                    print("Sorry, Boi Ses Hoye Gese")
                    return
                self.book_list[book] -= 1
                user.borrow_books.append(bookName)
                print("You have borrowed this book")
                return
        print("Book Not Available")
    def returne_books(self,bookName,user):
        for book in self.book_list:
            if book == bookName:
                self.book_list[book] += 1
                user.borrow_books.remove(bookName)
                user.returned_books.append(bookName)
                print("Book returned successfully")
                return
        print("Kar boi ferot dite ashcho??")



library = Library({"English":2,"Bangla":5,"Math":3})
allUsers = []
currentUser = None

while True:
    if currentUser == None:
        print("Not Logged In\nPlease Login or create account (L/C)")
        option = input()
        if option == "L":
            roll = int(input("Roll: "))
            password = input("Password: ")
            match = False
            for user in allUsers:
                if user.roll==roll and user.password == password:
                    currentUser = user
                    match = True
            if match == False:
                print("No user found")
        else:
            name = input("Name: ")
            roll = int(input("Roll: "))
            password = input("Password: ")
            user = User(name,roll,password)
            currentUser = user
    else:
        print("OPTIONS")
        print("________")
        print("1. Borrow a book")
        print("2. Return a book")
        x = int(input("Give Option: "))
        if x==1:
            bookName = input("Book Name: ")
            library.borrow_books(bookName,currentUser)
        elif x==2:
            bookName = input("Book Name: ")
            library.returne_books(bookName,currentUser)