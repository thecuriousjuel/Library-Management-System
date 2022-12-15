# Importing the required libraries
from database import Database

# This method is used to get the last student id from the database
def fetch_last_student_id(self):
    db = Database()
    returned_id = db.fetch_last_student_id()
    return returned_id

# This method is used to save student to database
def save_student(student):
    db = Database()
    db.save_student(student)

    print('\t\t\t\t------------------------------------------')
    print('\t\t\t\t|       Student Saved successfully       |')
    print('\t\t\t\t------------------------------------------')
    print(student)
    print('\t\t\t\t------------------------------------------')

# This method is used to authenticate students
def stud_auth(student_id, student_password):
    db = Database()
    allow = db.authenticate(student_id, student_password)
    return allow

# This method is used to generate Student ID
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

# This method is used to authenticate librarians
def lib_auth(lib_id, lib_pass):
    db = Database()
    allow = db.lib_authenticate(lib_id, lib_pass)
    return allow