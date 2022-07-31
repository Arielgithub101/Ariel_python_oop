class Book:
    def __init__(self,Title,Author,Price ):
        self.Title = Title
        self.Author = Author
        self.Price = Price
    def View(self):
        print(f'the Author name is : {self.Author}')
        print(f'the Title of the book is : {self.Title}')
        print(f'the price of the book  is : {self.Price}')