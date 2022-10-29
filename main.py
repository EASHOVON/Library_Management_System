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


library = Library({"English":2,"Bangla":5,"Math":3})
allUsers = []
currentUser = None