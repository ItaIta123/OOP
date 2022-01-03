# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book():
    # the initializer function - called before any other function
    def __init__(self, title):
        self.title = title


# TODO: create instances of the class
b1 = Book("Brave New World")
b2 = Book("War and Peace")


# TODO: print the class and property
print("The Class Book:")
print(b1)
print("and the book name is:")
print(b1.title)
print("The Class Book:")
print(b2)
print("and the book name is:")
print(b2.title)
