from typing import Tuple


class Geometry:
    def __init__(self):
        pass

    def distance(self, p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
        x1, y1 = p1
        x2, y2 = p2
        return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

    def middle(self, p1: Tuple[int, int], p2: Tuple[int, int]) -> Tuple[int, int]:
        x1, y1 = p1
        x2, y2 = p2
        x: int = (x1 + x2) // 2
        y: int = (y1 + y2) // 2
        return x, y

    def triangle_perimeter(self, a: int, b: int, c: int) -> int:
        return a + b + c

    def triangle_isoscel(self, a: int, b: int, c: int) -> bool:
        return a == b or a == c or b == c
