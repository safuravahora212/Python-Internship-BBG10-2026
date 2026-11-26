class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Issued"
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

class Library:
    def __init__(self):
        self.books = []

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def add_book(self, book):
        if self.find_book(book.book_id) is not None:
            print("Error: Book ID already exists!")
            return
        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available in library!")
            return
        print("========== BOOK LIST ==========")
        for book in self.books:
            book.display()
            print("------------------------------")

    def search_book(self, book_id):
        book = self.find_book(book_id)
        if book is None:
            print("Error: Book not found!")
            return
        print("Book Found!")
        print()
        book.display()

    def issue_book(self, book_id):
        book = self.find_book(book_id)
        if book is None:
            print("Error: Book not found!")
            return
        if not book.is_available:
            print("Sorry! This book is already issued!")
            return
        book.is_available = False
        print("Book issued successfully!")

    def return_book(self, book_id):
        book = self.find_book(book_id)
        if book is None:
            print("Error: Book not found!")
            return
        if book.is_available:
            print("Sorry! This book is not issued!")
            return
        book.is_available = True
        print("Book returned successfully!")

def main():
    library = Library()

    while True:
        print("========== LIBRARY MANAGEMENT ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid choice! Please try again.")
            continue

        if choice == 1:
            try:
                book_id = int(input("Enter Book ID: "))
            except ValueError:
                print("Invalid Book ID!")
                continue
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            new_book = Book(book_id, title, author)
            library.add_book(new_book)

        elif choice == 2:
            library.view_books()

        elif choice == 3:
            try:
                book_id = int(input("Enter Book ID: "))
            except ValueError:
                print("Invalid Book ID!")
                continue
            library.search_book(book_id)

        elif choice == 4:
            try:
                book_id = int(input("Enter Book ID: "))
            except ValueError:
                print("Invalid Book ID!")
                continue
            library.issue_book(book_id)

        elif choice == 5:
            try:
                book_id = int(input("Enter Book ID: "))
            except ValueError:
                print("Invalid Book ID!")
                continue
            library.return_book(book_id)

        elif choice == 6:
            print("Thank you! Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
    
