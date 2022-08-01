class Rectangle:
    def __init__(self,length: int,width: int):
        self.length: int = length
        self.width: int = width

    @property
    def perimeter(self):
       return (self.length * 2) + (self.width * 2)

    @property
    def get_area(self):
        return self.length * self.width

    def display(self):
        print(f'the length of the rectangle is {self.length} ')
        print(f'the width of the rectangle is {self.width} ')
        print(f'the Perimeter of the rectangle is {self.perimeter} ')
        print(f'the Area of the rectangle is {self.get_area} ')
class Parallelepipede(Rectangle):

    def __init__(self, length: int, width: int , height: int):
        Rectangle.__init__(self, length, width)
        self.height: int = height

    def volume(self):
        return self.length * self.width * self.height

    def display(self):
        print(f'the Voluum of the Parallelepipede is {self.volume()} ')
