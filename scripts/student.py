from datetime import datetime

from database import Database


class Student:
    def __init__(self, student_id, student_name, student_password, student_batch):
        self.student_id = student_id
        self.student_name = student_name
        self.student_password = student_password
        self.student_batch = student_batch

    def view_books(self):
        db = Database()
        db.view_books()

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
            print('\t\t\t\t\tBorrow Date  : ', today_date)
            print('\t\t\t\t------------------------------------------')

            print(book_obj)
            print('\t\t\t\t------------------------------------------')

            print('\t\t\t\t\t\t\t\tBorrowed By')
            print('\t\t\t\t------------------------------------------')
            print(self)
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t\t\t\tTransaction Successful')
            print('\t\t\t\t------------------------------------------')


        else:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t\t\t\tBook is not available')
            print('\t\t\t\t------------------------------------------')

    def return_book(self):
        db = Database()
        book_list = db.get_all_borrowed_books(self)
        if len(book_list) == 0:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t\t\t\tNo Books are borrowed yet!')
            print('\t\t\t\t------------------------------------------')
            return

        flag = True

        while flag:

            for book in book_list:
                print('\t', '-'*110)
                print(book)

            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t\t\tEnter Valid Book ID')
            print('\t\t\t\t\t\tPress enter to exit')
            print('\t\t\t\t------------------------------------------')
            ch = input('\t\t\t\t\t\t-> ')

            if len(ch) == 0:
                return

            for book in book_list:
                if book.book_id == ch:
                    flag = False
                    break

            if flag:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t\t\tError : Book ID not Found')
                print('\t\t\t\t------------------------------------------')
                return

        status = db.return_book(self, ch)

        if status:
            borrow_date = datetime.strptime(book.borrow_date, '%d-%m-%Y')
            current_date = datetime.now()
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t\t\t\t\tReturned Book')
            print('\t\t\t\t------------------------------------------')
            print(book)
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\tBorrow Date    : ', book.borrow_date)
            print('\t\t\t\tReturn Date    : ', current_date.strftime('%d-%m-%Y'))

            d = current_date - borrow_date
            print('\t\t\t\tHolding Period : ', d.days, 'day(s)')
            fine = (d.days // 7) * 20
            print('\t\t\t\tFine           :  Rs. ', fine)
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t\t\t\tTransaction Successful')
            print('\t\t\t\t------------------------------------------')
        else:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\tError: Book return unsuccessful (Check Book ID)')
            print('\t\t\t\t------------------------------------------')

    def check_fines(self):
        db = Database()
        book_list = db.get_all_borrowed_books(self)
        if len(book_list) == 0:
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\tError : No Books are borrowed yet!')
            print('\t\t\t\t------------------------------------------')
            return

        total = 0
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\tBorrowed Books with Fines')
        print('\t\t\t\t------------------------------------------')

        for book in book_list:
            print('\t', '-' * 110)
            print(book)

            borrow_date = datetime.strptime(book.borrow_date, '%d-%m-%Y')
            current_date = datetime.now()

            print('\t\t\t\tBorrow Date       : ', book.borrow_date)
            print('\t\t\t\tReturn Date       : ', current_date.strftime('%d-%m-%Y'))

            d = current_date - borrow_date
            print('\t\t\t\tHolding Period    : ', d.days, 'day(s)')

            fine = (d.days // 7) * 20
            print('\t\t\t\tFine              : Rs. ', fine)
            total += fine

        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t\t\tTotal     : Rs. ', total)
        print('\t\t\t\t------------------------------------------')

    def __str__(self):
        return (f"""
                    Student ID     : {self.student_id}
                    Student Name   : {self.student_name}
                    Student Batch  : {self.student_batch}
                   """)
