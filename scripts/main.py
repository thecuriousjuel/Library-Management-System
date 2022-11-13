from student import Student


def start():
    wrong_option = 5
    print('1. Admin')
    print('2. Student')

    choice = input('Enter your option -> ')

    if len(choice) == 0 or wrong_option == 0:
        return

    if choice == '1':
        admin()
    elif choice == '2':
        stud()
    else:
        print('Enter the mentioned choices.')
        print('Remaining options : ', wrong_option)
        wrong_option -= 1



def admin():
    pass


def


wrong_option = 5
while True:
    print('1. View Books')
    print('Press enter to exit')
    choice = input('Enter your option -> ')

    if len(choice) == 0 or wrong_option == 0:
        break

    try:
        choice = int(choice)
    except ValueError:
        print('Enter the mentioned choices.')
        print('Remaining options : ', wrong_option)
        wrong_option -= 1

    stud1 = Student(student_name='Biswajit', student_class='7A')
    stud1.view_books()

if __name__ == '__main__':
    start()
