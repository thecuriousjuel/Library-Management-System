from book import Book
from database import *
class Librarian:
    def __init__(self, librarian_id, librarian_name, librarian_password):
        self.librarian_id = librarian_id
        self.librarian_name = librarian_name
        self.librarian_password = librarian_password

    def add_books(self, book_name, book_author, book_publisher, book_publish_date, book_copies):
        db = Database()
        book_id = int(db.get_last_book_id()) + 1

        book_obj = Book(book_id=book_id,
                        book_name=book_name, 
                        book_author=book_author, 
                        book_publisher=book_publisher, 
                        book_publish_date=book_publish_date, 
                        book_copies=book_copies)

        db.save_book(book_obj)
        print('\t\t\t\t------------------------------------------')
        print(f'\t\t\t\t|              Book Saved               |')
        print('\t\t\t\t------------------------------------------')
        print(book_obj)
        print('\t\t\t\t------------------------------------------')


    def __str__(self):
        return (f"""
                \t\t\tLibrarian ID     : {self.librarian_id}
                \t\t\tLibrarian Name   : {self.librarian_name}
                """)