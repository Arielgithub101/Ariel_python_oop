class Rectangle:
    def __init__(self,length: int,width: int):
        self.length: int = length
        self.width: int = width

    @property
    def perimeter(self) -> int:
       return (self.length * 2) + (self.width * 2)

    @property
    def area(self) -> int:
        return self.length * self.width

    def display(self) -> None:
        print(f'the length of the rectangle is {self.length} ')
        print(f'the width of the rectangle is {self.width} ')
        print(f'the Perimeter of the rectangle is {self.perimeter} ')
        print(f'the Area of the rectangle is {self.area} ')
class Parallelepipede(Rectangle):

    def __init__(self, length: int, width: int , height: int):
        super().__init__(self, length, width)
        self.height: int = height
    @property
    def volume(self) -> int:
        return self.length * self.width * self.height

    def display(self) -> None:
        print(f'the Voluum of the Parallelepipede is {self.volume} ')
