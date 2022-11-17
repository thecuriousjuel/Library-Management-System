from database import *

def fetch_last_student_id(self):
    db = Database()
    returned_id = db.fetch_last_student_id()
    return returned_id


def save_student(student):
    db = Database()
    db.save_student(student)




def stud_auth(student_id, student_password):
    db = Database()
    allow = db.authenticate(student_id, student_password)
    return allow
