# Importing the required libraries
from datetime import datetime
from database import Database


class Student:
    # Constructor to initialize the student
    def __init__(self, student_id, student_name, student_password, student_batch):
        self.student_id = student_id
        self.student_name = student_name
        self.student_password = student_password
        self.student_batch = student_batch

    # This method is used to view all the books by the Student
    def view_books(self):
        db = Database()
        db.view_books()

    # This method is used to borrow a books by the Student
    def borrow_book(self):
        db = Database()
        selected_book_id = db.view_and_select_books()
        if not selected_book_id:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|             No Book Selected           |')
            print('\t\t\t\t------------------------------------------')
            return

        status = db.borrow_book(self, selected_book_id)

        if status:
            trans_id, today_date, book_obj = status
            print('\t\t\t\t------------------------------------------')
            print(f'\t\t\t\t|        Borrow Date  : {today_date}       |')
            print('\t\t\t\t------------------------------------------')
            print(book_obj)
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|              Borrowed By               |')
            print('\t\t\t\t------------------------------------------')
            print(self)
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|         Transaction Successful         |')
            print('\t\t\t\t------------------------------------------')
        else:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|    Error  :  Book is not available     |')
            print('\t\t\t\t------------------------------------------')

    # This method is used to return a books by the Student
    def return_book(self):
        db = Database()
        book_list = db.get_all_borrowed_books(self)
        if len(book_list) == 0:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|   Error : No Books are borrowed yet!   |')
            print('\t\t\t\t------------------------------------------')
            return

        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|             Borrowed Book(s)           |')
        print('\t\t\t\t------------------------------------------')

        for book in book_list:
            print(book)
            print('\t', '-'*110)

        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|           Enter Valid Book ID          |')
        print('\t\t\t\t|           Press enter to exit          |')
        print('\t\t\t\t------------------------------------------')
        ch = input('\t\t\t\t\t\t-> ')

        if len(ch) == 0:
            return

        for book in book_list:
            if book.book_id == ch:
                status = db.return_book(self, ch)
                if status:
                    borrow_date = datetime.strptime(book.borrow_date, '%d-%m-%Y')
                    current_date = datetime.now()
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|               Returned Book            |')
                    print('\t\t\t\t------------------------------------------')
                    print(book)

                    print(f'\t\t\t\t\t\tBorrow Date    : {book.borrow_date}', )
                    print(f'\t\t\t\t\t\tReturn Date    : {current_date.strftime("%d-%m-%Y")}')

                    d = current_date - borrow_date
                    print(f'\t\t\t\t\t\tHolding Period : {d.days} day(s)')
                    fine = (d.days // 7) * 20
                    print('\t\t\t\t\t\tFine           :  Rs. ', fine)

                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|               Returned By              |')
                    print('\t\t\t\t------------------------------------------')
                    print(self)
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|          Transaction Successful        |')
                    print('\t\t\t\t------------------------------------------')
                    return

        print('\t\t\t\t-----------------------------------------------------')
        print('\t\t\t\t|  Error: Book return unsuccessful (Check Book ID)  |')
        print('\t\t\t\t-----------------------------------------------------')

    # This method is used to check fines of the Student
    def check_fines(self):
        db = Database()
        book_list = db.get_all_borrowed_books(self)
        total = 0

        if len(book_list) == 0:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|   Alert : No Books are borrowed yet!   |')
            print('\t\t\t\t------------------------------------------')
            return total
        
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|        Borrowed Books with Fines       |')
        print('\t\t\t\t------------------------------------------')

        for book in book_list:

            print(book)

            borrow_date = datetime.strptime(book.borrow_date, '%d-%m-%Y')
            current_date = datetime.now()

            print('\t\t\t\t\tBorrow Date       : ', book.borrow_date)
            print('\t\t\t\t\tReturn Date       : ', current_date.strftime('%d-%m-%Y'))

            d = current_date - borrow_date
            print('\t\t\t\t\tHolding Period    : ', d.days, 'day(s)')

            fine = (d.days // 7) * 20
            print('\t\t\t\t\tFine              : Rs. ', fine)
            total += fine
            print('\t', '-' * 110)

        print('\t\t\t\t------------------------------------------')
        print(f'\t\t\t\t|      Total Fine    : Rs. {total}            |')
        print('\t\t\t\t------------------------------------------')

        if total == 0:
            total = -1
        return total

    # This method is used to deregister a Student
    def deregister(self):
        fine = self.check_fines() 
        if fine > 0:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|                 Alert!                 |')
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|      Please return borrowed books.     |')
            print('\t\t\t\t|        And clear all your fines.       |')
            print('\t\t\t\t------------------------------------------')
            return

        elif fine == -1:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|                 Alert!                 |')
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|      Please return borrowed books.     |')
            print('\t\t\t\t------------------------------------------')
            return

        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|                 Alert!                 |')
        print('\t\t\t\t------------------------------------------')
        print(self)
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\tAre you sure to De-register Yourself? Y/n')
        option = input('\t\t\t\t\t-> ')
        if option == 'Y':
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|             User Removed!              |')
            print('\t\t\t\t------------------------------------------')
            print(self)
            print('\t\t\t\t------------------------------------------')
            db = Database()
            db.deregister(self)
            return True
            
        return False

    # This method is used to print the details of the Student
    def __str__(self):
        return (f"""
                \t\t\tStudent ID     : {self.student_id}
                \t\t\tStudent Name   : {self.student_name}
                \t\t\tStudent Batch  : {self.student_batch}
                """)

