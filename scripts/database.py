import csv
import datetime
import os

from book import *


class Database:
    def __init__(self):
        pass

    def view_books(self):
        with open('../data/books.csv', mode='r') as file:
            csv_file = csv.reader(file)
            count = 1
            for lines in csv_file:
                self.print_it(lines)

                if count % 4 == 0:
                    print('\t\t\t\t', '-' * 50)
                    print('\t\t\t\t\t\tPress enter to view more...')
                    print('\t\t\t\t\t\tPress other key to exit')
                    print('\t\t\t\t', '-' * 50)
                    inp = input('\t\t\t\t\t\t-> ')
                    if len(inp) != 0:
                        break
                count += 1

    def view_and_select_books(self):
        with open('../data/books.csv', mode='r') as file:
            csv_file = csv.reader(file)
            count = 1
            for lines in csv_file:
                self.print_it(lines)

                if count % 4 == 0:
                    print('\t\t\t\t', '-' * 50)
                    print('\t\t\t\t\t\t\tProvide accurate book id.')
                    print('\t\t\t\t\t\t\tPress enter to view more...')
                    print('\t\t\t\t', '-' * 50)
                    inp = input('\t\t\t\t\t\t\t-> ')
                    if len(inp) != 0:
                        return inp
                count += 1

        print('\t\t\t\t------------------------------------------')
        print('\t\t\t\t\t\t\tProvide accurate book id.')
        print('\t\t\t\t\t\t\tPress enter to view more...')
        print('\t\t\t\t------------------------------------------')
        inp = input('\t\t\t\t-> ')
        return inp

    def print_it(self, data):
        print('\t', '-'*110)
        print('\t\t\t\tID            : ', data[0])
        print('\t\t\t\tName          : ', data[1])
        print('\t\t\t\tAuthor        : ', data[2])
        print('\t\t\t\tPublisher     : ', data[3])
        print('\t\t\t\tPublish Date  : ', data[4])
        print('\t\t\t\tAvailability  : ', data[5])
        print('\t\t\t\tNo. of Copies : ', data[6])

    def authenticate(self, stud_id, stud_password):
        from student import Student
        status = False
        with open('../data/students.csv', mode='r', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            for lines in csv_file:
                if lines[0] == stud_id and lines[2] == stud_password:
                    status = Student(lines[0], lines[1], lines[2], lines[3])
                    break

        return status

    def fetch_last_student_id(self):
        last = []
        with open('../data/students.csv', mode='r', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            for lines in csv_file:
                if len(lines) > 0:
                    last = lines
            try:
                return lines[0]
            except IndexError:
                return last[0]

    def save_student(self, stud_obj):
        data = [stud_obj.student_id, stud_obj.student_name, stud_obj.student_password, stud_obj.student_batch]
        with open('../data/students.csv', newline='', mode='a', encoding='utf-8') as file:
            writer_object = csv.writer(file)
            writer_object.writerow(data)

    def borrow_book(self, stud_obj, book_id):
        with open('../data/books.csv', mode='r', encoding='utf-8') as file:
            books = csv.reader(file)
            success = False

            with open('../data/temp.csv', mode='a', newline='', encoding='utf-8') as temp_file:
                for book in books:
                    if book[0] == book_id:
                        if int(book[6]) >= 1:
                            book[6] = int(book[6]) - 1
                            if book[6] == 0:
                                book[5] = False
                            success = book

                    temp_books = csv.writer(temp_file)
                    temp_books.writerow(book)

        os.remove('../data/books.csv')
        os.rename('../data/temp.csv', '../data/books.csv')

        if success:
            book_obj = Book(success[0], success[1], success[2], success[3], success[4], success[5], success[6])
            trans_id, today_date = self.write_to_transaction_and_borrow_file(stud_obj, book_obj, 'b')
            return trans_id, today_date, book_obj

        return success

    def update_all_borrows_file(self,stud_obj, book_obj):
        status = False

        with open('../data/temp.csv', mode='w', newline='', encoding='utf-8') as temp_file:
            temp_file_writer = csv.writer(temp_file)

            with open('../data/all_borrows.csv', mode='r', encoding='utf-8') as borrow_file:
                borrow_file_reader = csv.reader(borrow_file)

                for line in borrow_file_reader:
                    if line[1] == stud_obj.student_id and line[2] == book_obj.book_id and not status:
                        status = True
                        continue
                    temp_file_writer.writerow(line)

        os.remove('../data/all_borrows.csv')
        os.rename('../data/temp.csv', '../data/all_borrows.csv')

    def return_book(self, stud_obj, book_id):
        with open('../data/books.csv', mode='r', encoding='utf-8') as file:
            books = csv.reader(file)
            success = False

            with open('../data/temp.csv', mode='a', newline='', encoding='utf-8') as temp_file:
                for book in books:
                    if book[0] == book_id and not success:
                        book[6] = int(book[6]) + 1
                        book[5] = True
                        success = book

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

    def fetch_last_transaction_id(self):
        check_file_presence = os.path.isfile('../data/all_transaction.csv')
        if not check_file_presence:
            return 'tr0001'

        last = []
        with open('../data/all_transaction.csv', mode='r', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            for lines in csv_file:
                if len(lines) > 0:
                    last = lines
            try:
                return lines[0]
            except IndexError:
                return last[0]

    def get_current_date(self):
        x = datetime.datetime.now()
        return x.strftime("%d-%m-%Y")

    def write_to_transaction_and_borrow_file(self, stud_obj, book_obj, trans_type):
        transaction_id = self.create_transaction_id()
        today_date = self.get_current_date()

        with open('../data/all_transaction.csv', mode='a', newline='', encoding='utf-8') as file:
            data_to_write = [transaction_id, stud_obj.student_id, book_obj.book_id, today_date, trans_type]
            temp_books = csv.writer(file)
            temp_books.writerow(data_to_write)

        if trans_type == 'b':
            with open('../data/all_borrows.csv', mode='a', newline='', encoding='utf-8') as borrow_file:
                data_to_write = [transaction_id, stud_obj.student_id, book_obj.book_id, today_date]
                borrow_csv_writer = csv.writer(borrow_file)
                borrow_csv_writer.writerow(data_to_write)

        return transaction_id, today_date

    def create_transaction_id(self):

        num_of_zeros = 4
        returned_id = self.fetch_last_transaction_id()

        new_id = int(returned_id[2:]) + 1

        temp = new_id
        num_of_digits = 0

        while temp > 0:
            num_of_digits += 1
            temp //= 10

        new_id = 'tr' + '0' * (num_of_zeros - num_of_digits) + str(new_id)
        return new_id

    def get_all_borrowed_books(self, stud_obj):
        with open('../data/all_borrows.csv', mode='r', encoding='utf-8') as borrow_file:
            trans_file_reader = csv.reader(borrow_file)
            book_list = []

            for line in trans_file_reader:
                if line[1] == stud_obj.student_id:

                    with open('../data/books.csv', mode='r', encoding='utf-8') as book_file:
                        book_file_reader = csv.reader(book_file)

                        for book_line in book_file_reader:
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

        return book_list

