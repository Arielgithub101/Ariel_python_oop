class Circle:
    def __init__(self,a ,b, r):
        self.a = a
        self.b = b
        self.r = r
    def Area(self):
        print(f'the area of the circle is {2 * 3.14 *(self.r ** 2)}')
    def Perimeter(self):
        print(f'the Perimeter of the circle is {2 * 3.14 * self.r}')
    def testBelongs(self):
        pass
    #לחזור לסעיך נק בתוך מעגל