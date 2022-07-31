class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def Perimeter(self):
       return (self.length * 2) + (self.width * 2)

    def Area(self):
        return (self.length * self.width)

    def display_Rec(self):
        print(f'the length of the rectangle is {self.length} ')
        print(f'the width of the rectangle is {self.width} ')
        print(f'the Perimeter of the rectangle is {self.Perimeter()} ')
        print(f'the Area of the rectangle is {self.Area()} ')
class Parallelepipede(Rectangle):

    def __init__(self, length, width , height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def Volume(self):
        return (self.length * self.width * self.height)

    def display_Para(self):
        print(f'the Voluum of the Parallelepipede is {self.Volume()} ')
