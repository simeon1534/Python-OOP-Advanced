class User:
    books = []

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: 'Library'):
        """Already rented"""
        for key, value in library.rented_books.items():
            for book_name_rented, days_left in value.items():
                if book_name_rented == book_name:
                    return f"The book {book_name} is already rented and will be available in {days_left} days!"
        """Available"""
        for key, value in library.books_available.items(): # value is list
            if key == author and book_name in value:

                self.books.append(book_name)

                library.books_available[author].remove(book_name)  # ako ostane samo avtor bez knigi mahame avtora
                # ot books_available?
                if self.username in library.rented_books:
                    library.rented_books[self.username][book_name] = days_to_return
                else:
                    library.rented_books[self.username] = {book_name: days_to_return}

        """Not available"""
        # do nothing

    def return_book(self, author: str, book_name: str, library: 'Library'):
        returned = False
        for kniga in self.books:
            if kniga == book_name:

                del library.rented_books[self.username][book_name]
                library.books_available[author].append(book_name)
                self.books.remove(book_name)
                returned = True

        #for i in list(self.books):      # delete empty keys
           # if self.books[i] == []:
            #    del self.books[i]

        if not returned:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return sorted(self.books)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.info()}"
