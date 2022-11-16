import csv
import os

class Database:
    def __init__(self):
        pass

    def view_books(self):
        with open('../data/books.csv', mode='r') as file:
            csv_file = csv.reader(file)
            count = 1
            for lines in csv_file:
                self.print_it(lines)

                if count % 6 == 0:
                    print('-' * 50)
                    print('Press enter to view more...')
                    print('Press other key to exit')
                    print('-' * 50)
                    inp = input('->')
                    if len(inp) != 0:
                        break
                count += 1

    def view_and_select_books(self):
        with open('../data/books.csv', mode='r') as file:
            csv_file = csv.reader(file)
            count = 1
            for lines in csv_file:
                self.print_it(lines)

                if count % 6 == 0:
                    print('-' * 50)
                    print('Provide accurate book id.')
                    print('Press enter to view more...')
                    print('-' * 50)
                    inp = input('->')
                    if len(inp) != 0:
                        return inp
                count += 1

    def print_it(self, data):
        print('-' * 50)
        print('ID            : ', data[0])
        print('Name          : ', data[1])
        print('Author        : ', data[2])
        print('Publisher     : ', data[3])
        print('Publish Date  : ', data[4])
        print('Availability  : ', data[5])
        print('No. of Copies : ', data[6])

    def authenticate(self, stud_obj):
        status = False
        with open('../data/students.csv', mode='r', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            for lines in csv_file:
                if lines[0] == stud_obj.student_id and lines[2] == stud_obj.student_password:
                    status = True
                    stud_obj.student_name = lines[1]
                    stud_obj.student_batch = lines[3]
                    break

        return status

    def fetch_last_id(self):
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

    def borrow_book(self, book_id):
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

        return success

    def return_book(self, book_id):
        with open('../data/books.csv', mode='r', encoding='utf-8') as file:
            books = csv.reader(file)
            success = False
            book_id = '13'

            with open('../data/temp.csv', mode='a', newline='', encoding='utf-8') as temp_file:
                for book in books:
                    if book[0] == book_id:
                        book[6] = int(book[6]) + 1
                        success = book

                    temp_books = csv.writer(temp_file)
                    temp_books.writerow(book)

        os.remove('../data/books.csv')
        os.rename('../data/temp.csv', '../data/books.csv')

        return success

