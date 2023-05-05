class Bookshelf:
    def __init__(self, name, author, price, publishing_year):
        self.name = name
        self.author = author
        self.price = price
        self.year = publishing_year
        
    def add_books(self):
        print("Book name:" + self.name)
        print("Book Author:" + self.author)
        print("Book Price:" + self.price)
        print("Book was published in:" + self.year)
        print("Book Added")
        
    def time(self):
        time_p = 2023 - int(self.year)
        print("The Book was published " + str(time_p) + " years ago.")
        
book1 = Bookshelf("Harry Potter", "J.K Rowling", "799" , "1999")
book1.add_books()
book1.time()

book2 = Bookshelf("Geronimo Stilton", "Geronimo Stilton", "499" , "2022")
book2.add_books()
book2.time()
        

        
