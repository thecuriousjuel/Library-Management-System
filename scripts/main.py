from main_helper import *
from student import *
from pwinput import pwinput


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
                    print('\t\t\t\t\t\tEnter your Name')
                    stud_name = input('\t\t\t\t\t\t-> ').strip()

                    print('\t\t\t\t\t\tEnter your Password')
                    stud_pass_1 = pwinput('\t\t\t\t\t\t-> ', mask='x').strip()

                    print('\t\t\t\t\t\tRe-enter your Password')
                    stud_pass_2 = pwinput('\t\t\t\t\t\t-> ', mask='x').strip()

                    print('\t\t\t\t\t\tEnter Batch')
                    stud_batch = input('\t\t\t\t\t\t-> ')

                    if len(stud_name) < 1 or len(stud_pass_1) < 1 or len(stud_pass_2) < 1 or len(stud_batch) < 1:
                        print('\t\t\t\t\t\tPlease enter a valid student details.')
                        ch = input('\t\t\t\t\t\tPress Enter to continue....')
                        if len(ch) <= 0:
                            break

                    elif stud_pass_1 != stud_pass_2:
                        print('\t\t\t\t------------------------------------------')
                        print('\t\t\t\t|          Password not matching         |')
                        print('\t\t\t\t|           Press enter to exit          |')
                        print('\t\t\t\t------------------------------------------')
                        ch = input('\t\t\t\t\t\t-> ')
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
            case _:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|       Enter the mentioned choices      |')
                print(f'\t\t\t\t|       Remaining attempts : {wrong_option}           |')
                print('\t\t\t\t------------------------------------------')
                wrong_option -= 1


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
                fine = stud_obj.check_fines() 
                if fine > 0:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|                 Alert!                 |')
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|      Please return borrowed books.     |')
                    print('\t\t\t\t|        And clear all your fines.       |')
                    print('\t\t\t\t------------------------------------------')
                    continue

                elif fine == -1:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|                 Alert!                 |')
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|      Please return borrowed books.     |')
                    print('\t\t\t\t------------------------------------------')
                    continue

                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|                 Alert!                 |')
                print('\t\t\t\t------------------------------------------')
                print(stud_obj)
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\tAre you sure to De-register Yourself? Y/n')
                option = input('\t\t\t\t\t-> ')
                if option == 'Y':
                    stud_obj.remove()


            case _:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|       Enter the mentioned choices      |')
                print(f'\t\t\t\t|       Remaining attempts : {wrong_option}           |')
                print('\t\t\t\t------------------------------------------')
                wrong_option -= 1


def lib_options(lib_obj):
    wrong_option = 5

    while True:
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|              Librarian Menu            |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|             1. Add Books               |')
        print('\t\t\t\t|             2. Update Books            |')
        print('\t\t\t\t|             3. Remove Books            |')
        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t\tPress enter to exit')
        print('\t\t\t\t\tEnter your option ')
        choice = input('\t\t\t\t\t-> ')

        if len(choice) == 0 or wrong_option == 0:
            break

        match choice:
            case '1':
                try:
                    print('\t\t\t\t\tEnter Book Name')
                    book_name = input('\t\t\t\t\t-> ').strip()

                    print('\t\t\t\t\tEnter Book Author')
                    book_author = input('\t\t\t\t\t-> ').strip()

                    print('\t\t\t\t\tEnter Book Publisher [Optional]')
                    book_publisher = input('\t\t\t\t\t-> ').strip()

                    print('\t\t\t\t\tEnter Book Publish Date (DD-MM-YYYY) [Optional]')
                    book_publish_date = input('\t\t\t\t\t-> ').strip()

                    print('\t\t\t\t\tEnter No. of copies (Default: 1) [Optional]')
                    book_copies = int(input('\t\t\t\t\t-> ').strip())

                    flag = False
                    if len(book_publish_date) == 0 or len(book_publish_date) == 10:
                        pass
                    else:
                        flag = True

                    if len(book_name) == 0 and len(book_author) == 0 and flag == True and book_copies < 0:
                        print('\t\t\t\t------------------------------------------')
                        print('\t\t\t\t|                 Error!                 |')
                        print('\t\t\t\t------------------------------------------')
                        print('\t\t\t\t|        Please Check books details.     |')
                        print('\t\t\t\t------------------------------------------')

                except ValueError:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|                 Error!                 |')
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|        Please Check books details.     |')
                    print('\t\t\t\t------------------------------------------')
                except Exception as exp:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|        Some Error occur                |')
                    print('\t\t\t\t------------------------------------------')
                    print(f'\t\t\t\t|        {exp}               |')
                    print('\t\t\t\t------------------------------------------')

                    
                lib_obj.add_books(book_name=book_name, 
                                    book_author=book_author, 
                                    book_publisher=book_publisher, 
                                    book_publish_date=book_publish_date, 
                                    book_copies=book_copies)

            case '2':
                lib_obj.update_book()
            case '3':
                lib_obj.remove_book()
            case _:
                print('\t\t\t\t------------------------------------------')
                print('\t\t\t\t|       Enter the mentioned choices      |')
                print(f'\t\t\t\t|       Remaining attempts : {wrong_option}           |')
                print('\t\t\t\t------------------------------------------')
                wrong_option -= 1


if __name__ == '__main__':
    start()
