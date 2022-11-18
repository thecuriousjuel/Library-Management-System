class Book:
    def __init__(self,
                 book_id,
                 book_name,
                 book_author,
                 book_publisher,
                 book_publish_date,
                 book_availability_status,
                 book_copies):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.book_publisher = book_publisher
        self.book_publish_date = book_publish_date
        self.book_availability_status = book_availability_status
        self.book_copies = book_copies


    def __str__(self):
        return (f"""
            Book ID           : {self.book_id}
            Book Name         : {self.book_name}
            Book Author       : {self.book_author}
            Book Publisher    : {self.book_publisher}
            Book Publish Date : {self.book_publish_date}
                   """)


