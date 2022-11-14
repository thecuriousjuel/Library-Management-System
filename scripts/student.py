from database import *


class Student:
    def __init__(self,
                 student_id='undefined',
                 student_name='undefined',
                 student_password='undefined',
                 student_batch='undefined'):

        self.student_id = student_id
        self.student_name = student_name
        self.student_password = student_password
        self.student_class = student_batch

    def view_books(self):
        db = Database()
        db.view_books()

    def stud_auth(self, user_type):
        db = Database()
        allow = db.authenticate(self, user_type)
        return allow