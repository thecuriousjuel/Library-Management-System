# Importing the required libraries
from book import Book
from database import Database
from datetime import datetime
class Librarian:
    # Constructor to initialize the librarian
    def __init__(self, librarian_id, librarian_name, librarian_password):
        self.librarian_id = librarian_id
        self.librarian_name = librarian_name
        self.librarian_password = librarian_password

    # This method is used to view all the books by the librarian
    def view_books(self):
        db = Database()
        db.view_books()
    
    # This method is used to add a book by the librarian
    def add_books(self):
        try:
            print('\t\t\t\t\tEnter Book Name')
            book_name = input('\t\t\t\t\t-> ').strip()

            print('\t\t\t\t\tEnter Book Author')
            book_author = input('\t\t\t\t\t-> ').strip()

            print('\t\t\t\t\tEnter Book Publisher [Optional]')
            book_publisher = input('\t\t\t\t\t-> ').strip()

            print('\t\t\t\t\tEnter Book Publish Date (DD-MM-YYYY) [Optional]')
            book_publish_date = input('\t\t\t\t\t-> ').strip()

            print('\t\t\t\t\tEnter No. of copies (Default: 1) [Optional]')
            book_copies = input('\t\t\t\t\t-> ').strip()

            if len(book_copies) == 0:
                book_copies = '1'

            flag = False
            if len(book_publish_date) == 0 or len(book_publish_date) == 10:
                if len(book_publish_date) == 10:
                    day, month, year = book_publish_date.split('-')
                    datetime(day=int(day), month=int(month), year=int(year))
            else:
                flag = True

            if len(book_name) == 0 or len(book_author) == 0 or flag == True or int(book_copies) < 0:
                raise ValueError

        except ValueError as exp:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|                 Error!                 |')
            print('\t\t\t\t------------------------------------------')
            print(f'\t\t\t\t\t\t{exp}')
            print('\t\t\t\t------------------------------------------')

        except Exception as exp:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|        Some Error occur                |')
            print('\t\t\t\t------------------------------------------')
            print(f'\t\t\t\t\t\t{exp}')
            print('\t\t\t\t------------------------------------------')

        else:
            try:
                db = Database()
                book_id = int(db.get_last_book_id()) + 1
            except IndexError:
                book_id = '1'

            book_obj = Book(book_id=book_id,
                            book_name=book_name, 
                            book_author=book_author, 
                            book_publisher=book_publisher, 
                            book_publish_date=book_publish_date, 
                            book_copies=book_copies)

            db.save_book(book_obj)
            print('\t\t\t\t------------------------------------------')
            print(f'\t\t\t\t|               Book Saved               |')
            print('\t\t\t\t------------------------------------------')
            print(book_obj)
            print('\t\t\t\t------------------------------------------')

    # This method is used to update a book by the librarian
    def update_book(self):
        db = Database()
        selected_book_id = db.view_and_select_books()
        if not selected_book_id:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|             No Book Selected           |')
            print('\t\t\t\t------------------------------------------')
            return
        
        try:
            print('\t\t\t\t\tEnter New Book Name')
            book_name = input('\t\t\t\t\t-> ').strip()

            print('\t\t\t\t\tEnter New Book Author')
            book_author = input('\t\t\t\t\t-> ').strip()

            print('\t\t\t\t\tEnter New Book Publisher [Optional]')
            book_publisher = input('\t\t\t\t\t-> ').strip()

            print('\t\t\t\t\tEnter New Book Publish Date (DD-MM-YYYY) [Optional]')
            book_publish_date = input('\t\t\t\t\t-> ').strip()

            print('\t\t\t\t\tEnter New No. of copies (Default: 1) [Optional]')
            book_copies = input('\t\t\t\t\t-> ').strip()

            if len(book_copies) == 0:
                book_copies = '1'

            flag = False
            if len(book_publish_date) == 0 or len(book_publish_date) == 10:
                if len(book_publish_date) == 10:
                    day, month, year = book_publish_date.split('-')
                    datetime(day=int(day), month=int(month), year=int(year))
            else:
                flag = True

            if len(book_name) == 0 or len(book_author) == 0 or flag == True or int(book_copies) < 0:
                raise ValueError('Book Details not valid')

        except ValueError as exp:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|                 Error!                 |')
            print('\t\t\t\t------------------------------------------')
            print(f'\t\t\t\t\t\t{exp}')
            print('\t\t\t\t------------------------------------------')

        except Exception as exp:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|        Some Error occur!               |')
            print('\t\t\t\t------------------------------------------')
            print(f'\t\t\t\t\t\t{exp}')
            print('\t\t\t\t------------------------------------------')

        else:
            book_obj = Book(book_id=selected_book_id,
                            book_name=book_name, 
                            book_author=book_author, 
                            book_publisher=book_publisher, 
                            book_publish_date=book_publish_date, 
                            book_copies=book_copies)

            status = db.update_book(book_obj)

    
            if status:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|              Book Updated              |')
                print('\t\t\t\t------------------------------------------')
                print(book_obj)
                print('\t\t\t\t------------------------------------------')
            else:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|         Error  :  Check Book ID        |')
                print('\t\t\t\t------------------------------------------')

    # This method is used to remove a book by the librarian
    def remove_book(self):
        db = Database()
        selected_book_id = db.view_and_select_books()
        if not selected_book_id:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|             No Book Selected           |')
            print('\t\t\t\t------------------------------------------')
            return

        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|                 Alert!                 |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\tAre you sure to remove the book? Y/n')
        option = input('\t\t\t\t\t-> ')

        if option == 'Y':
            status = db.remove_book(selected_book_id)
            if status:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|              Book Deleted              |')
                    print('\t\t\t\t------------------------------------------')
                    print(status)
                    print('\t\t\t\t------------------------------------------')
            else:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|         Error  :  Check Book ID        |')
                print('\t\t\t\t------------------------------------------')

    # This method is used to print the details of the librarian
    def __str__(self):
        return (f"""
                \t\t\tLibrarian ID     : {self.librarian_id}
                \t\t\tLibrarian Name   : {self.librarian_name}
                """)

    