from main_helper import *
from student import *
def start():
    wrong_option = 5
    failed_auth = 5

    while True:
        print('-------------------------')
        print('|         Home          |')
        print('-------------------------')
        print('|      1. Login         |')
        print('|      2. Register      |')
        print('-------------------------')
        print('Press enter to exit')
        choice = input('Enter your option -> ').strip()

        if len(choice) == 0 or wrong_option == 0:
            break

        match choice:
            case '1':
                if failed_auth < 0:
                    break

                stud_id = input('Enter your ID -> ').strip()
                stud_pass = input('Enter your Password -> ').strip()

                if len(stud_id) == 0 or len(stud_pass) == 0:
                    print('------------------------')
                    print('Error : Invalid Entry!')
                    print('Remaining attempts : ', failed_auth)
                    print('------------------------')
                    failed_auth -= 1
                    continue

                stud_obj = stud_auth(stud_id, stud_pass)

                if stud_obj:
                    print('------------------------------------')
                    print("Hello!")
                    print("Student ID    :", stud_obj.student_id)
                    print("Student Name  : ", stud_obj.student_name)
                    print("Student Batch : ", stud_obj.student_batch)
                    print('------------------------------------')

                    stud_options(stud_obj)
                else:
                    print('Error : Authentication Failed!')
                    print('Remaining attempts : ', failed_auth)
                    failed_auth -= 1

            case '2':
                status = False
                while True:
                    stud_name = input('Enter your Name -> ').strip()
                    stud_pass_1 = input('Enter your Password -> ').strip()
                    stud_pass_2 = input('Re-enter your Password -> ').strip()
                    stud_batch = input('Enter Batch -> ')

                    if len(stud_name) < 1 or len(stud_pass_1) < 1 or len(stud_pass_2) < 1 or len(stud_batch) < 1:
                        print('Please enter a valid student details.')
                        ch = input('Press Enter to continue....')
                        if len(ch) <= 0:
                            break

                    elif stud_pass_1 != stud_pass_2:
                        print('Password not matching')
                        ch = input('Press Enter to continue....')
                        if len(ch) <= 0:
                            break
                    else:
                        status = True
                        break

                if status:

                    stud = Student(student_id=create_id(),
                                   student_name=stud_name,
                                   student_password=stud_pass_1,
                                   student_batch=stud_batch)

                    save_student(stud)

            case _:
                print('Enter the mentioned choices.')
                print('Remaining attempts : ', wrong_option)
                wrong_option -= 1


def stud_options(stud_obj):
    wrong_option = 5

    while True:
        print('-------------------------')
        print('|     Student Menu      |')
        print('-------------------------')
        print('|    1. View Books      |')
        print('|    2. Borrow Books    |')
        print('|    3. Return Books    |')
        print('|    4. Compute Fines   |')
        print('-------------------------')

        print('Press enter to exit')
        choice = input('Enter your option -> ')

        if len(choice) == 0 or wrong_option == 0:
            break

        match choice:
            case '1':
                stud_obj.view_books()
            case '2':
                stud_obj.borrow_book()
            case '3':
                stud_obj.return_book()
            case '4':
                stud_obj.check_fines()
            case _:
                print('Enter the mentioned choices.')
                print('Remaining attempts : ', wrong_option)
                wrong_option -= 1


if __name__ == '__main__':
    start()
