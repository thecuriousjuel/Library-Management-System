from database import *


class Student:
    def __init__(self, student_name='undefined', student_class='undefined'):
        self.student_name = student_name
        self.student_class = student_class

    def view_books(self):
        db = Database()
        db.view_books()
