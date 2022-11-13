import csv
import os

class Database:
    def __init__(self):
        pass

    def view_books(self):
        with open('../data/books.csv', mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                self.print_it(lines)


    def print_it(self, data):
        print('Book ID     : ', data[0])
        print('Book Name   : ', data[1])
        print('Book Author : ', data[2])

