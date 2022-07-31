class Geometry:
    def __init__(self):
        pass

    def distance(self,x1,y1,x2,y2):
        return (((x1 - x2)**2) + ((y1 - y2)**2)) ** 0.5
    def middle(self, x1,y1,x2,y2):
        x = (x1+x2)/2
        y = (y1+y2)/2
        return (x,y)
    def trianglePerimeter(self,a ,b ,c):
        return a+b+c
    def triangleIsoscel(self,a ,b ,c):
        return (a == b or a == c or b == c)