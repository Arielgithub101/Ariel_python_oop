class Circle:
    def __init__(self,a: int ,b:int, r:int):
        self.a:int = a
        self.b:int = b
        self.r:int = r
    def area(self):
        print(f'the area of the circle is {2 * 3.14 *(self.r ** 2)}')
    def perimeter(self):
        print(f'the Perimeter of the circle is {2 * 3.14 * self.r}')
    def testBelongs(self):
        pass
    #לחזור לסעיך נק בתוך מעגל