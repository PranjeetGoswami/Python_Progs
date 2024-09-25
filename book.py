class Book:
    book_count = 0
    
    def __init__(self,title,author):
        self.title = title
        self.author = author
        Book.book_count += 1
        
    @classmethod
    def count_books(cls):
        return cls.book_count
    
book1 = Book("1984", "George Orwell")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")
book1 = Book("To kill a mockingbird", "Harper lee")

print(f"Total number of books {Book.count_books()}")