import csv
import os

class Database:
    def __init__(self):
        pass

    def view_books(self):
        with open('../data/books.csv', mode='r') as file:
            csvFile = csv.reader(file)
            count = 1
            for lines in csvFile:
                self.print_it(lines)

                if count % 6 == 0:
                    input('Press enter to view more...')
                count += 1



    def print_it(self, data):
        print('-'*50)
        print('ID            : ', data[0])
        print('Name          : ', data[1])
        print('Author        : ', data[2])
        print('Publisher     : ', data[3])
        print('Publish Date  : ', data[4])
        print('Availability  : ', data[5])
        print('No. of Copies : ', data[6])


