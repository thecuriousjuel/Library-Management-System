from student import Student


def start():
    wrong_option = 5

    while True:
        print('1. Admin')
        print('2. Student')
        print('3. Exit')
        choice = input('Enter your option -> ')

        if len(choice) == 0 or wrong_option == 0:
            return

        if choice == '1':
            # authenticate()
            admin()
        elif choice == '2':
            stud_id = input('Enter your ID -> ')
            stud_pass = input('Enter your Password -> ')

            if len(stud_id) == 0 or len(stud_pass) == 0:
                print('Error : Invalid Entry!')
                continue

            stud = Student(student_id=stud_id, student_password=stud_pass)
            allow = stud.stud_auth(user_type='S')
            if allow:
                print("Hello!")
                print("Student ID    :", allow['student_id'])
                print("Student Name  : ", allow['student_name'])
                print("Student Batch : ", allow['student_batch'])

                stud_options()
            else:
                print('Error : Authentication Failed!')
        elif choice == '3':
            break
        else:
            print('Enter the mentioned choices.')
            print('Remaining options : ', wrong_option)
            wrong_option -= 1


def admin():
    pass


def stud_options():
    wrong_option = 5

    while True:
        print('-' * 50)
        print('|\t1. View Book', '\t\t\t7. Delete Complain')
        print('|\t2. Borrow Book', '\t\t\t8. View Seat')
        print('|\t3. Return Book', '\t\t\t9. Book Seat')
        print('|\t4. Create Complain', '\t\t10. Update Seat')
        print('|\t5. View Complain', '\t\t11. Release Seat')
        print('|\t6. Update Complain')
        print('-' * 50)

        print('Press enter to exit')
        choice = input('Enter your option -> ')

        if len(choice) == 0 or wrong_option == 0:
            break

        if choice == '1':
            stud_obj = Student()
            stud_obj.view_books()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        elif choice == '7':
            pass
        elif choice == '8':
            pass
        elif choice == '9':
            pass
        elif choice == '10':
            pass
        elif choice == '11':
            pass
        else:
            print('Enter the mentioned choices.')
            print('Remaining options : ', wrong_option)
            wrong_option -= 1


if __name__ == '__main__':
    start()
