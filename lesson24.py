class Book:
  def __init__(self, name, janr, author, year, dds_number):
        self.name = name
        self.janr = janr
        self.author = author
        self.year = year
        self.dds_number = dds_number


class Author:
    def __init__(self, name, age, nickname):
        self.name = name
        self.age = age
        self.nickname = nickname


class Catalog:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search(self,name):
        for book in self.books:
            if book.name == name:
                return book.dds_number


a1 = Author('Ali', 81, 'Vali')

b1 = Book('sariq dev', 'badiiy', a1, 2012, 32)
b2 = Book('red dev', 'badiiy', a1, 2014, 34)
b3 = Book('oq dev', 'badiiy', a1, 2016, 34)

c1 = Catalog('2-etaj')
# c1.books = [b1, b2, b3]
c1.add_book(b2)
c1.add_book(b3)
c1.add_book(b1)

c1.search('sariq dev')
print(c1.search('sariq dev'))