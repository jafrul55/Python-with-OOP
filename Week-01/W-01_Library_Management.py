class User:
    def __init__(self,name,roll,password) -> None:
        self.name = name
        self.roll = roll
        self.password = password
        self.borrowed_books = []
        self.returned_books = []

class Library:
    def __init__(self,book_list) -> None:
        self.book_list = book_list

    def borrow_book(self,bookName,user):
        for book in self.book_list:
            if book == bookName:
                if bookName in user.borrowed_books:
                    print("Give me Back borrow book")
                    return
                if self.book_list[book] == 0:
                    print("Book is not available")
                    return
                self.book_list[book] -= 1
                user.borrowed_books.append(bookName)
                print("You have borrowed this book")
                return
        print("Book not available")
    
    def return_book(self,bookName,user):
        for book in self.book_list:
            if book == bookName:
                self.book_list[book] += 1
                user.borrowed_books.remove(bookName)
                user.returned_books.append(bookName)
                print("Book returned successfully")
                return
            else:
                print("Thanks but onner boi nabo na")
                return
        print("kar boi ferot dite ashco??")

    def availability(self):
        for book in self.book_list:
            if self.book_list[book] > 0:
                print(book,self.book_list[book])

    def donate(self,bookName,amount):
        for book in self.book_list:
            if book == bookName:
                self.book_list[book] += amount
                print("Thanks for donating")
                return
        self.book_list[bookName] = amount
        print("Thank you so much !")


# if english book is empty
library = Library({"English":1,"Bangla":5,"Math":3})
# library = Library({"English":2,"Bangla":5,"Math":3})

allusers = []
currentUser = None

while True:
    if currentUser == None:
        print("Not Logged in\nPlease Login or create account(L/C)")
        option = input()
        if option == "L":
            roll = int(input("Roll: "))
            password = input("Password: ")
            match = False
            for user in allusers:
                if user.roll == roll and user.password == password:
                    currentUser = user
                    match = True
            if match == False:
                print("No user found")
        else:
            name = input("Name: ")
            roll = int(input("Roll: "))
            password = input("Password: ")
            found = False
            for user in allusers:
                if user.roll == roll:
                    found = True
            if found:
                print("koi Bar account Kolba")
                continue
            user = User(name,roll,password)
            currentUser = user
            allusers.append(user)
    else:
        print("OPTIONS")
        print("_________")
        print("1.Borrow a book")
        print("2.Return a book")
        print("3.Borrowed books list")
        print("4.Returned books list")
        print("5.Check availability")
        print("6.Donate")
        print("7.Logout")
        # library.borrow_book("Somaj",currentUser)
        # library.borrow_book("English",currentUser)
        # print(library.book_list)
        # print(user.borrow_books)
        #if again I want to say that again give me once more book
        # library.borrow_book("English",currentUser)
        # break
        x = int(input("Give Option: "))
        if x == 1:
            bookName = input("Book name: ")
            library.borrow_book(bookName,currentUser)

        elif x == 2:
            bookName = input("Book name: ")
            library.return_book(bookName,currentUser)

        elif x == 3:
            print(currentUser.borrowed_books)

        elif x == 4:
            print(currentUser.returned_books)

        elif x == 5:
            library.availability()

        elif x == 6:
            bookName = input("Book Name: ")
            amount = int(input("Amount: "))
            library.donate(bookName,amount)

        elif x == 7:
            currentUser = None

        print("\n\n")

# Jafrul
# 15
# 123

