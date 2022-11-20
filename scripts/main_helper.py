from database import *


def fetch_last_student_id(self):
    db = Database()
    returned_id = db.fetch_last_student_id()
    return returned_id


def save_student(student):
    db = Database()
    db.save_student(student)

    print('\t\t\t\t------------------------------------')
    print('\t\t\t\t|    Student Saved successfully    |')
    print('\t\t\t\t------------------------------------')
    print(student)
    print('\t\t\t\t------------------------------------')


def stud_auth(student_id, student_password):
    db = Database()
    allow = db.authenticate(student_id, student_password)
    return allow


def create_id():
    db = Database()

    num_of_zeros = 4
    returned_id = db.fetch_last_student_id()

    new_id = int(returned_id[2:]) + 1

    temp = new_id
    num_of_digits = 0

    while temp > 0:
        num_of_digits += 1
        temp //= 10

    new_id = 'st' + '0' * (num_of_zeros - num_of_digits) + str(new_id)
    return new_id
