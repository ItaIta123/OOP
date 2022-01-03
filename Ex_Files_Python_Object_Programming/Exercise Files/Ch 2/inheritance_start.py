# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance


class Publication:
    def __init__(self, title, price):
        self.price = price
        self.title = title

# Below is a nested class inheritance
class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

"""
The below is an example of inheritance. Setting self.title and price
for each of the classes below is a bit redundant.
The solution is to create an additional class (such as the above),
and inherent them like the followning:

class New_Class(Class_inherenting_from)
class Book(Publication)

Access inheritance: 
super().method_in_the_other_class

"""
class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
