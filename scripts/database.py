import csv


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
        print('Method : fetch_id')
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
            print('Student Saved successfully')
            print('ID    : ', stud_obj.student_id)
            print('Name  : ', stud_obj.student_name)
            print('Batch : ', stud_obj.student_batch)
