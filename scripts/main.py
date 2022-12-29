# Importing the required libraries
from main_helper import *
from student import *
from librarian import *
from pwinput import pwinput
import os

# This method is the starting point of the application
def start():
    wrong_option = 5
    failed_auth = 5

    while True:
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|                  Home                  |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|          1. Student Login              |')
        print('\t\t\t\t|          2. Student Register           |')
        print('\t\t\t\t|          3. Librarian Login            |')
        print('\t\t\t\t|          4. Librarian Register         |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t\tPress enter to exit')
        print('\t\t\t\t\tEnter your option')
        choice = input('\t\t\t\t\t-> ').strip()

        if len(choice) == 0 or wrong_option == 0:
            break

        match choice:
            case '1':
                if failed_auth < 0:
                    break
                print('\t\t\t\t\tEnter your ID ')
                stud_id = input('\t\t\t\t\t-> ').strip()

                print('\t\t\t\t\tEnter your Password')
                stud_pass = pwinput('\t\t\t\t\t-> ', mask='x').strip()

                if len(stud_id) == 0 or len(stud_pass) == 0:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|         Error : Invalid Entry!         |')
                    print(f'\t\t\t\t\t|      Remaining attempts : {failed_auth}      |')
                    print('\t\t\t\t------------------------------------------')
                    failed_auth -= 1
                    continue

                stud_obj = stud_auth(stud_id, stud_pass)

                if stud_obj:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|                 Hello!                 |')
                    print('\t\t\t\t------------------------------------------')
                    print(stud_obj)
                    print('\t\t\t\t------------------------------------------')

                    stud_options(stud_obj)
                else:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|    Error : Authentication Failed!      |')
                    print(f'\t\t\t\t|    Remaining attempts : {failed_auth}              |')
                    print('\t\t\t\t------------------------------------------')
                    failed_auth -= 1

            case '2':
                status = False
                while True:
                    print('\t\t\t\t\tEnter your Name')
                    stud_name = input('\t\t\t\t\t-> ').strip()

                    print('\t\t\t\t\tEnter your Password')
                    stud_pass_1 = pwinput('\t\t\t\t\t-> ', mask='x').strip()

                    print('\t\t\t\t\tRe-enter your Password')
                    stud_pass_2 = pwinput('\t\t\t\t\t-> ', mask='x').strip()

                    if stud_pass_1 != stud_pass_2:
                        print('\t\t\t\t------------------------------------------')
                        print('\t\t\t\t|          Password not matching         |')
                        print('\t\t\t\t|           Press enter to exit          |')
                        print('\t\t\t\t------------------------------------------')
                        ch = input('\t\t\t\t\t\t-> ')
                        break

                    print('\t\t\t\t\tEnter Batch')
                    stud_batch = input('\t\t\t\t\t-> ')

                    if len(stud_name) < 1 or len(stud_pass_1) < 1 or len(stud_pass_2) < 1 or len(stud_batch) < 1:
                        print('\t\t\t\t\tPlease enter a valid student details.')
                        ch = input('\t\t\t\t\tPress Enter to continue....')
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

            case '3':
                if failed_auth < 0:
                    break
                print('\t\t\t\t\tEnter your ID')
                lib_id = input('\t\t\t\t\t-> ').strip()

                print('\t\t\t\t\tEnter your Password')
                lib_pass = pwinput('\t\t\t\t\t-> ', mask='x').strip()

                if len(lib_id) == 0 or len(lib_pass) == 0:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|         Error : Invalid Entry!         |')
                    print(f'\t\t\t\t\t|      Remaining attempts : {failed_auth}      |')
                    print('\t\t\t\t------------------------------------------')
                    failed_auth -= 1
                    continue

                lib_obj = lib_auth(lib_id, lib_pass)

                if lib_obj:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|                 Hello!                 |')
                    print('\t\t\t\t------------------------------------------')
                    print(lib_obj)
                    print('\t\t\t\t------------------------------------------')

                    lib_options(lib_obj)
                else:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|    Error : Authentication Failed!      |')
                    print(f'\t\t\t\t|    Remaining attempts : {failed_auth}              |')
                    print('\t\t\t\t------------------------------------------')
                    failed_auth -= 1
            
            case '4':
                status = False
                while True:
                    print('\t\t\t\t\tEnter your Name')
                    lib_name = input('\t\t\t\t\t-> ').strip()

                    print('\t\t\t\t\tEnter your Password')
                    lib_pass_1 = pwinput('\t\t\t\t\t-> ', mask='x').strip()

                    print('\t\t\t\t\tRe-enter your Password')
                    lib_pass_2 = pwinput('\t\t\t\t\t-> ', mask='x').strip()

                    if lib_pass_1 != lib_pass_2:
                        print('\t\t\t\t------------------------------------------')
                        print('\t\t\t\t|          Password not matching         |')
                        print('\t\t\t\t|           Press enter to exit          |')
                        print('\t\t\t\t------------------------------------------')
                        ch = input('\t\t\t\t\t-> ')
                        break

                    if len(lib_name) < 1 or len(lib_pass_1) < 1 or len(lib_pass_2) < 1:
                        print('\t\t\t\t\tPlease enter a valid details.')
                        ch = input('\t\t\t\t\tPress Enter to continue....')
                        if len(ch) <= 0:
                            break
                    else:
                        status = True
                        break

                if status:
                    lib = Librarian(librarian_id=create_lib_id(),
                                   librarian_name=lib_name,
                                   librarian_password=lib_pass_1)

                    save_librarian(lib)
            
            case _:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|       Enter the mentioned choices      |')
                print(f'\t\t\t\t|       Remaining attempts : {wrong_option}           |')
                print('\t\t\t\t------------------------------------------')
                wrong_option -= 1

# This method lists all the actions that student can perform
def stud_options(stud_obj):
    wrong_option = 5

    while True:
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|              Student Menu              |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|             1. View Books              |')
        print('\t\t\t\t|             2. Borrow Books            |')
        print('\t\t\t\t|             3. Return Books            |')
        print('\t\t\t\t|             4. Compute Fines           |')
        print('\t\t\t\t|             5. De-Register             |')
        print('\t\t\t\t------------------------------------------')

        print('\t\t\t\t\tPress enter to exit')
        print('\t\t\t\t\tEnter your option ')
        choice = input('\t\t\t\t\t-> ')

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
            case '5':
                status = stud_obj.deregister()
                if status:
                    break
            case _:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|       Enter the mentioned choices      |')
                print(f'\t\t\t\t|       Remaining attempts : {wrong_option}           |')
                print('\t\t\t\t------------------------------------------')
                wrong_option -= 1

# This method lists all the actions that librarian can perform
def lib_options(lib_obj):
    wrong_option = 5

    while True:
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|              Librarian Menu            |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|             1. View Books              |')
        print('\t\t\t\t|             2. Add Books               |')
        print('\t\t\t\t|             3. Update Books            |')
        print('\t\t\t\t|             4. Remove Books            |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t\tPress enter to exit')
        print('\t\t\t\t\tEnter your option ')
        choice = input('\t\t\t\t\t-> ')

        if len(choice) == 0 or wrong_option == 0:
            break

        match choice:
            case '1':
                lib_obj.view_books()
            case '2':
                lib_obj.add_books()
            case '3':
                lib_obj.update_book()
            case '4':
                lib_obj.remove_book()
            case _:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|       Enter the mentioned choices      |')
                print(f'\t\t\t\t|       Remaining attempts : {wrong_option}           |')
                print('\t\t\t\t------------------------------------------')
                wrong_option -= 1

# This method checks whether a file exists or not and creates files if required.
def check_and_create_file(path, file_name):
    file_path = f'{path}/{file_name}'
    check_file = os.path.isfile(file_path)

    if check_file:
        return

    with open(file_path, mode='w') as f:
        pass

# This method creates the folders and files just before starting the application. 
def create_files_and_folders():
    path = '../data'
    check_folder = os.path.isdir(path)

    if not check_folder:
        os.mkdir(path)
        
    check_and_create_file(path, 'all_borrows.csv')
    check_and_create_file(path, 'all_transactions.csv')
    check_and_create_file(path, 'books.csv')
    check_and_create_file(path, 'librarian.csv')
    check_and_create_file(path, 'students.csv')   

    print('\t\t\t\t------------------------------------------')
    print('\t\t\t\t|         Database Initialized           |')
    print('\t\t\t\t------------------------------------------') 

# This statement controls that no other module can this main file.
if __name__ == '__main__':
    create_files_and_folders()
    start()
