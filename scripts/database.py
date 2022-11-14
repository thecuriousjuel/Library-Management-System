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
                    print('1. Press enter to view more...')
                    print('2. Press other key to exit')
                    print('-' * 50)
                    inp = input('->')
                    if len(inp) != 0:
                        break
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

    def authenticate(self, stud_obj, user_type):
        status = False
        if user_type == 'S':
            with open('../data/students.csv', mode='r') as file:
                csv_file = csv.reader(file)
                for lines in csv_file:
                    if lines[0] == stud_obj.student_id and lines[2] == stud_obj.student_password:
                        status = dict(student_id=lines[0],
                                      student_name=lines[1],
                                      student_batch=lines[3])

                        break

        return status
