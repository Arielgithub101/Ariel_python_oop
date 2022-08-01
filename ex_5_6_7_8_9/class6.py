class Book:
    def __init__(self,Title:str,Author:str,Price:int ):
        self.Title:str = Title
        self.Author:str = Author
        self.Price:int = Price
    def view(self):
        print(f'the Author name is : {self.Author}')
        print(f'the Title of the book is : {self.Title}')
        print(f'the price of the book  is : {self.Price}')