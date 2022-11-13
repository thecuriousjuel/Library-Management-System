from student import Student


def start():
    wrong_option = 5

    while True:
        print('1. Admin')
        print('2. Student')

        choice = input('Enter your option -> ')

        if len(choice) == 0 or wrong_option == 0:
            return

        if choice == '1':
            # authticate()
            admin()
        elif choice == '2':
            # authticate()
            stud()
        else:
            print('Enter the mentioned choices.')
            print('Remaining options : ', wrong_option)
            wrong_option -= 1



def admin():
    pass


def stud():
    wrong_option = 5

    while True:
        print('-'*50)
        print('|\t1. View Book','\t\t\t7. Delete Complain')
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
