from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class ContentFormatter(Formatter):
    def format(self, book: Book):
        return book.content


class AuthorFormatter(Formatter):
    def format(self, book: Book):
        return book.author


class Printer:
    def print(self, book: Book, formatter: Formatter):
        return formatter.format(book)




book = Book('Principles', 'Ray Dalio', 'Lorem ipsum')
printer = Printer()
print(printer.print(book, AuthorFormatter()))
