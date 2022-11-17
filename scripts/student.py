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
            print('Borrow successful')
            print(status)
        else:
            print('Book is not available')

    def return_book(self):
        db = Database()
        status = db.return_book('9')
        if status:
            print('Return successful')
            print(status)
        else:
            print('Book return unsuccessful (Check Book ID)')


    def __str__(self):
        return (f"""
            ID    : {self.student_id}
            Name  : {self.student_name}
            Batch : {self.student_batch}
                   """)
