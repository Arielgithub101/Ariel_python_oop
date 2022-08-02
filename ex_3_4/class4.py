import math


class Circle:
    def __init__(self, a: int, b: int, r: int):
        self.a: int = a
        self.b: int = b
        self.r: int = r

    def area(self) -> None:
        print(f'the area of the circle is {2 * math.pi * (self.r ** 2)}')

    def perimeter(self) -> None:
        print(f'the Perimeter of the circle is {2 * math.pi * self.r}')

    def test_belongs(self, x: int, y: int) -> bool:
        d: float = math.sqrt(math.pow((x - self.a), 2) + math.pow((y - self.b), 2))
        return d < self.r
