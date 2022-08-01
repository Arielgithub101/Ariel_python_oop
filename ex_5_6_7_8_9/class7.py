class Geometry:
    def __init__(self):
        pass

    def distance(self,x1:int,y1:int,x2:int,y2:int) -> int:
        return (((x1 - x2)**2) + ((y1 - y2)**2)) ** 0.5
    def middle(self, x1:int,y1:int,x2:int,y2:int) -> tuple:
        x = (x1+x2)/2
        y = (y1+y2)/2
        return (x,y)
    def triangle_perimeter(self,a:int ,b:int ,c:int) -> int:
        return a+b+c
    def triangle_isoscel(self,a:int ,b:int ,c:int) -> bool:
        return (a == b or a == c or b == c)