class Book:
    def __init__(self,
                 book_id,
                 book_name,
                 book_author,
                 book_publisher,
                 book_publish_date,
                 book_availability_status='True',
                 book_copies='1',
                 borrow_date=None):
        self.book_id = book_id
        self.book_name = book_name

        if len(book_author) != 0:
            self.book_author = book_author 
        else:
            self.book_author = 'Unknown'

        if len(book_publisher) != 0:
            self.book_publisher = book_publisher 
        else:
            self.book_publisher = 'Unknown'

        if len(book_publish_date) != 0:
            self.book_publish_date = book_publish_date 
        else:
            self.book_publish_date = 'Unknown'

        self.book_copies = book_copies
        if int(self.book_copies) > 0:
            book_availability_status = 'True'
        else:
            book_availability_status = 'False'

        self.book_availability_status = book_availability_status
        self.borrow_date = borrow_date

    def __str__(self):
        return (f"""
                    \t\t\tBook ID           : {self.book_id}
                    \t\t\tBook Name         : {self.book_name}
                    \t\t\tBook Author       : {self.book_author}
                    \t\t\tBook Publisher    : {self.book_publisher}
                    \t\t\tBook Publish Date : {self.book_publish_date}
                    \t\t\tBook Avail status : {self.book_availability_status}
                    \t\t\tBook Copies       : {self.book_copies}
                   """)
