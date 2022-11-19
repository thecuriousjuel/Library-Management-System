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
            print('-----------------------')
            print('|  No Book Selected   |')
            print('-----------------------')
            return

        status = db.borrow_book(self, selected_book_id)

        if status:
            trans_id, today_date, book_obj = status
            print('-----------------------')
            print('Date : ', today_date)
            print('-----------------------')
            print(self)
            print('-----------------------')
            print('Borrowed Book')
            print('-----------------------')
            print(book_obj)
            print('-----------------------')
            print('Borrow successful. ')
            print('-----------------------')
        else:
            print('Book is not available')

    def return_book(self):
        db = Database()
        book_list = db.get_all_borrowed_books(self)
        if len(book_list) == 0:
            print('No Books are borrowed yet!')
            return

        flag = True

        while flag:

            for book in book_list:
                print(book)

            print('Enter the Book ID : ')
            print('Press enter to exit')
            ch = input('-> ')

            if len(ch) == 0:
                return

            for book in book_list:
                if book.book_id == ch:
                    flag = False
                    break

            if flag == True:
                print('Enter Valid Book ID')

        status = db.return_book(self, ch)
        if status:
            print('Return successful')
            print(status[0])
            print(status[1])
        else:
            print('Book return unsuccessful (Check Book ID)')

    def __str__(self):
        return (f"""
            Student ID     : {self.student_id}
            Student Name   : {self.student_name}
            Student Batch  : {self.student_batch}
                   """)
