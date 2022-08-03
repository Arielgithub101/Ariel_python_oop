class Book:
    def __init__(self, title: str, author: str, price: int):
        self.title: str = title
        self.author: str = author
        self.price: int = price

    def view(self) -> None:
        print(f'the Author name is : {self.author}')
        print(f'the Title of the book is : {self.title}')
        print(f'the price of the book  is : {self.price}')
