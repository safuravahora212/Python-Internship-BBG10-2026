class Library:
    def __init__(self):
        self.__books = []  # private list

    def add_book(self, title):
        self.__books.append(title)

    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)

    def list_books(self):
        return self.__books.copy()

# Test
lib = Library()
lib.add_book("Harry Potter")
lib.add_book("Python Easy")
print(lib.list_books())

lib.remove_book("Harry Potter")
print(lib.list_books())

# print(lib.__books) # This will give error, because private

