# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pageCount
        return result


class Author():
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

    def __str__(self):
        return self.fName + " " + self.lName


class Chapter():
    def __init__(self, name, pageCount):
        self.name = name
        self.pageCount = pageCount


author = Author("Leo", "Bla Bla")
b1 = Book("War and Peace", 39.0, author)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.author)
print(b1.author.fName)
print(b1.getbookpagecount())
print(b1.title)
