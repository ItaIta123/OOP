# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This atrr will lead to an error if a user is trying to access it!"

    # TODO: create instance methods
    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price

    # TODO: try setting the discount
    def set_discount(self, amount):
        # an underscore indicates that this attr is for internal class use only
        self._discount = amount


    

# TODO: create some book instances
b1 = Book("War and Peace", "Leo", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD", 234, 29.95)

# TODO: print the price of book1
print(b1.get_price())

# TODO: try setting the discount
print("B2 price before discount:")
print(b2.get_price())
b2.set_discount(0.5)
print("B2 price after discount:")
print(b2.get_price())


# TODO: properties with double underscores are hidden by the interpreter
print(b1._Book__secret)