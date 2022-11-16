from database import *


class Student:
    def __init__(self, student_id=None, student_name=None, student_password=None, student_batch=None):
        if student_id == None:
            student_id = self.create_id()
        self.student_id = student_id
        self.student_name = student_name
        self.student_password = student_password
        self.student_batch = student_batch

    def create_id(self):
        num_of_zeros = 4
        returned_id = self.fetch_last_id()

        new_id = int(returned_id[2:]) + 1

        temp = new_id
        num_of_digits = 0

        while temp > 0:
            num_of_digits += 1
            temp //= 10

        new_id = 'ST' + '0' * (num_of_zeros - num_of_digits) + str(new_id)
        return new_id

    def fetch_last_id(self):
        db = Database()
        returned_id = db.fetch_last_id()
        return returned_id

    def save_student(self):
        db = Database()
        db.save_student(self)

        print('Student Saved successfully')
        print('ID    : ', self.student_id)
        print('Name  : ', self.student_name)
        print('Batch : ', self.student_batch)

    def view_books(self):
        db = Database()
        db.view_books()

    def stud_auth(self):
        db = Database()
        allow = db.authenticate(self)
        return allow

    def borrow_book(self):
        db = Database()
        selected_book_id = db.view_and_select_books()
        status = db.borrow_book(selected_book_id)

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
