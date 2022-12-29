# Importing the required libraries
import csv
import datetime
import os
from book import *

class Database:
    # Intilizing the Database Object (Null in this case)
    def __init__(self):
        pass

    # This method is used to get all the book details from the books file.
    def view_books(self):
        with open('../data/books.csv', mode='r') as file:
            csv_file = csv.reader(file)
            count = 1
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|                All Book(s)             |')
            print('\t\t\t\t------------------------------------------')
            for lines in csv_file:
                self.print_it(lines)

                if count % 4 == 0:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|       Press enter to view more...      |')
                    print('\t\t\t\t|       Press other key to exit          |')
                    print('\t\t\t\t------------------------------------------')
                    inp = input('\t\t\t\t\t-> ')
                    if len(inp) != 0:
                        break
                count += 1

    # This method is used to view all the books and get the valid book id that the user has selected.
    def view_and_select_books(self):
        with open('../data/books.csv', mode='r') as file:
            csv_file = csv.reader(file)
            count = 1
            print('\t\t\t\t------------------------------------------')
            print('\t\t\t\t|                All Book(s)             |')
            print('\t\t\t\t------------------------------------------')
            for lines in csv_file:
                self.print_it(lines)

                if count % 4 == 0:
                    print('\t\t\t\t------------------------------------------')
                    print('\t\t\t\t|        Provide accurate Book ID.       |')
                    print('\t\t\t\t|        Press enter to view more...     |')
                    print('\t\t\t\t------------------------------------------')
                    inp = input('\t\t\t\t\t-> ')
                    if len(inp) != 0:
                        return inp
                count += 1

        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t|        Provide accurate Book ID.       |')
        print('\t\t\t\t|        Press enter to exit.            |')
        print('\t\t\t\t------------------------------------------')
        inp = input('\t\t\t\t\t-> ')

        if len(inp) == 0:
            return False

        return inp

    # This method is used to print the book details from the books file.
    def print_it(self, data):
        try:
            print('\t\t\t\tID            : ', data[0])
            print('\t\t\t\tName          : ', data[1])
            print('\t\t\t\tAuthor        : ', data[2])
            print('\t\t\t\tPublisher     : ', data[3])
            print('\t\t\t\tPublish Date  : ', data[4])
            print('\t\t\t\tAvailability  : ', data[5])
            print('\t\t\t\tNo. of Copies : ', data[6])
            print('\t', '-'*110)
        except IndexError:
            pass
        except Exception:
            pass
    
    # This method is used to validate the student details entered
    def authenticate(self, stud_id, stud_password):
        status = False
        from student import Student
        with open('../data/students.csv', mode='r', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            for lines in csv_file:
                try:
                    if lines[0] == stud_id and lines[2] == stud_password:
                        status = Student(lines[0], lines[1], lines[2], lines[3])
                        break
                except IndexError:
                    pass
                except Exception:
                    pass

        return status

    # This method is used to fetch the last student id which is used to generate new id.
    def fetch_last_student_id(self):
        last = []
        with open('../data/students.csv', mode='r', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            lines = []
            for lines in csv_file:
                if len(lines) > 0:
                    last = lines
            try:
                return lines[0]
            except IndexError:
                return last[0]
            except Exception:
                pass
    
    # This is used to store the student details in students file
    def save_student(self, stud_obj):
        data = [stud_obj.student_id, stud_obj.student_name, stud_obj.student_password, stud_obj.student_batch]
        with open('../data/students.csv', newline='', mode='a', encoding='utf-8') as file:
            writer_object = csv.writer(file)
            writer_object.writerow(data)

    # This method allows thee student to borrow a book.
    def borrow_book(self, stud_obj, book_id):
        with open('../data/books.csv', mode='r', encoding='utf-8') as file:
            books = csv.reader(file)
            success = False

            with open('../data/temp.csv', mode='a', newline='', encoding='utf-8') as temp_file:
                for book in books:
                    try:
                        if book[0] == book_id:
                            if int(book[6]) >= 1:
                                book[6] = str(int(book[6]) - 1)
                                if book[6] == 0:
                                    book[5] = "False"
                                success = book
                    except IndexError:
                        continue
                    except Exception:
                        continue

                    temp_books = csv.writer(temp_file)
                    temp_books.writerow(book)

        os.remove('../data/books.csv')
        os.rename('../data/temp.csv', '../data/books.csv')

        if success:
            book_obj = Book(success[0], success[1], success[2], success[3], success[4], success[5], success[6])
            trans_id, today_date = self.write_to_transaction_and_borrow_file(stud_obj, book_obj, 'b')
            return trans_id, today_date, book_obj

        return success

    # This method write to a file which track the borrow history.
    def update_all_borrows_file(self,stud_obj, book_obj):
        status = False

        with open('../data/temp.csv', mode='w', newline='', encoding='utf-8') as temp_file:
            temp_file_writer = csv.writer(temp_file)

            with open('../data/all_borrows.csv', mode='r', encoding='utf-8') as borrow_file:
                borrow_file_reader = csv.reader(borrow_file)

                for line in borrow_file_reader:
                    try:
                        if line[1] == stud_obj.student_id and line[2] == book_obj.book_id and not status:
                            status = True
                            continue
                    except IndexError:
                        continue
                    except Exception:
                        continue
                    temp_file_writer.writerow(line)

        os.remove('../data/all_borrows.csv')
        os.rename('../data/temp.csv', '../data/all_borrows.csv')

    # This method allows the student to return a book.
    def return_book(self, stud_obj, book_id):
        with open('../data/books.csv', mode='r', encoding='utf-8') as file:
            books = csv.reader(file)
            success = False

            with open('../data/temp.csv', mode='a', newline='', encoding='utf-8') as temp_file:
                for book in books:
                    try:
                        if book[0] == book_id and not success:
                            book[6] = str(int(book[6]) + 1)
                            book[5] = "True"
                            success = book
                    except IndexError:
                        continue
                    except Exception:
                        continue
                    temp_books = csv.writer(temp_file)
                    temp_books.writerow(book)

        os.remove('../data/books.csv')
        os.rename('../data/temp.csv', '../data/books.csv')

        if success:
            book_obj = Book(success[0], success[1], success[2], success[3], success[4], success[5], success[6])
            trans_id = self.write_to_transaction_and_borrow_file(stud_obj, book_obj, 'r')
            self.update_all_borrows_file(stud_obj, book_obj)

            return trans_id, book_obj
        return success

    # This methods gets the last transaction id of a borrow or return.
    def fetch_last_transaction_id(self):
        last = []
        lines = []
        with open('../data/all_transactions.csv', mode='r', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            for lines in csv_file:
                if len(lines) > 0:
                    last = lines
            try:
                return lines[0]
            except IndexError:
                return last[0]

    # This method generates current date.
    def get_current_date(self):
        x = datetime.datetime.now()
        return x.strftime("%d-%m-%Y")

    # This method writes borrows and returns to the all_transaction file.
    def write_to_transaction_and_borrow_file(self, stud_obj, book_obj, trans_type):
        transaction_id = self.create_transaction_id()
        today_date = self.get_current_date()

        with open('../data/all_transactions.csv', mode='a', newline='', encoding='utf-8') as file:
            data_to_write = [transaction_id, stud_obj.student_id, book_obj.book_id, today_date, trans_type]
            temp_books = csv.writer(file)
            temp_books.writerow(data_to_write)

        if trans_type == 'b':
            with open('../data/all_borrows.csv', mode='a', newline='', encoding='utf-8') as borrow_file:
                data_to_write = [transaction_id, stud_obj.student_id, book_obj.book_id, today_date]
                borrow_csv_writer = csv.writer(borrow_file)
                borrow_csv_writer.writerow(data_to_write)

        return transaction_id, today_date

    # This method creates a new transaction id.
    def create_transaction_id(self):
        num_of_zeros = 4
        try:
            returned_id = self.fetch_last_transaction_id()
            new_id = int(returned_id[2:]) + 1
            temp = new_id
            num_of_digits = 0

            while temp > 0:
                num_of_digits += 1
                temp //= 10

            new_id = 'tr' + '0' * (num_of_zeros - num_of_digits) + str(new_id)

        except IndexError:
            new_id = 'tr0001'

        return new_id

    # This method fetches all the borrowed books by a student.
    def get_all_borrowed_books(self, stud_obj):
        with open('../data/all_borrows.csv', mode='r', encoding='utf-8') as borrow_file:
            borrow_file_reader = csv.reader(borrow_file)
            book_list = []

            for line in borrow_file_reader:
                try:
                    if line[1] == stud_obj.student_id:

                        with open('../data/books.csv', mode='r', encoding='utf-8') as book_file:
                            book_file_reader = csv.reader(book_file)

                            for book_line in book_file_reader:
                                try:
                                    if line[2] == book_line[0]:
                                        book_obj = Book(book_line[0],
                                                        book_line[1],
                                                        book_line[2],
                                                        book_line[3],
                                                        book_line[4],
                                                        book_line[5],
                                                        book_line[6])

                                        book_obj.borrow_date = line[3]

                                        book_list.append(book_obj)
                                except IndexError:
                                    pass
                                except Exception:
                                    pass
                except IndexError:
                    pass
                except Exception:
                    pass

        return book_list

    # This method is used to de-register/remove a student.
    def deregister(self, student_obj):
        with open('../data/students.csv', mode='r', newline='', encoding='utf-8') as file_read_obj:
            csv_reader = csv.reader(file_read_obj)

            with open('../data/temp.csv', mode='w', newline='', encoding='utf-8') as file_write_object:
                csv_writer = csv.writer(file_write_object)

                for line in csv_reader:
                    if student_obj.student_id == line[0]:
                        continue
                    csv_writer.writerow(line)


        os.remove('../data/students.csv')
        os.rename('../data/temp.csv', '../data/students.csv')

    # This method is used to get the last librarian id.
    def fetch_last_librarian_id(self):
        last = []
        with open('../data/librarian.csv', mode='r', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            lines = []
            for lines in csv_file:
                if len(lines) > 0:
                    last = lines
            try:
                return lines[0]
            except IndexError:
                return last[0]
            except Exception:
                pass

    # This method is used to save a librarian
    def save_librarian(self, lib_obj):
        data = [lib_obj.librarian_id, lib_obj.librarian_name, lib_obj.librarian_password]
        with open('../data/librarian.csv', newline='', mode='a', encoding='utf-8') as file:
            writer_object = csv.writer(file)
            writer_object.writerow(data)

    # This method is used to authenticate the librarian.
    def lib_authenticate(self, lib_id, lib_pass):
        from librarian import Librarian
        status = False
        
        with open('../data/librarian.csv', mode='r', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            for lines in csv_file:
                try:
                    if lines[0] == lib_id and lines[2] == lib_pass:
                        status = Librarian(lines[0], lines[1], lines[2])
                        break
                except IndexError:
                    pass
                except Exception:
                    pass

        return status

    # This methods is used to get the last book id.
    def get_last_book_id(self):
        last = []
        with open('../data/books.csv', mode='r', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            lines = []
            for lines in csv_file:
                if len(lines) > 0:
                    last = lines
            try:
                return lines[0]
            except IndexError:
                return last[0]
            except Exception:
                pass

    # This method is used to save book details in the books file.
    def save_book(self, book_obj):
        book_data = [book_obj.book_id, book_obj.book_name, book_obj.book_author, book_obj.book_publisher, book_obj.book_publish_date,
        book_obj.book_availability_status, book_obj.book_copies]

        with open('../data/books.csv', newline='', mode='a', encoding='utf-8') as file_obj:
            writer_object = csv.writer(file_obj)
            writer_object.writerow(book_data)

    # This method is used to update book details in the books file.
    def update_book(self, book_obj):
        with open('../data/books.csv', mode='r', encoding='utf-8') as file:
            books = csv.reader(file)
            success = False

            with open('../data/temp.csv', mode='a', newline='', encoding='utf-8') as temp_file:
                temp_books = csv.writer(temp_file)

                for book in books:
                    try:
                        if book[0] == book_obj.book_id and not success:
                            success = book

                            data = [book_obj.book_id, book_obj.book_name, book_obj.book_author, book_obj.book_publisher, book_obj.book_publish_date, book_obj.book_availability_status, book_obj.book_copies]

                            temp_books.writerow(data)
                            continue
                    except IndexError:
                        continue
                    except Exception:
                        continue
                    
                    temp_books.writerow(book)

        os.remove('../data/books.csv')
        os.rename('../data/temp.csv', '../data/books.csv')

        return success

    # This method is used to remove book details from the books file.
    def remove_book(self, book_id):
        with open('../data/books.csv', mode='r', encoding='utf-8') as file:
            books = csv.reader(file)
            success = False

            with open('../data/temp.csv', mode='a', newline='', encoding='utf-8') as temp_file:
                temp_books = csv.writer(temp_file)

                for book in books:
                    try:
                        if book[0] == book_id and not success:
                            success = book
                            continue
                    except IndexError:
                        continue
                    except Exception:
                        continue
                    
                    temp_books.writerow(book)

        os.remove('../data/books.csv')
        os.rename('../data/temp.csv', '../data/books.csv')

        if success:
            success = Book(success[0], success[1], success[2], success[3], success[4], success[5], success[6])
        return success

