import math
from typing import List


class Coputation:
    def __init__(self):
        pass

    def factorial(self, x: int) -> int:
        t: int = 1
        while x > 0:
            t *= x
            x -= 1
        return t

    def sum1(self, x: int) -> int:
        total: int = 0
        while x > 0:
            total += x
            x -= 1
        return total

    def test_prim(self, x: int) -> int:
        counter: int = 0
        if x <= 1: return False
        for i in range(2, (x//2)):
            if x % i == 0:
                return False
        return True

    def test_prims(self, x: int, y: int) -> bool:
        counter: int = 0
        max_num: int = max(x, y)
        if x <= 1 or y <= 1:
            return False
        for i in range(1, max_num + 1):
            if x % i == 0 or y % i == 0:
                counter += 1
                if counter > 4: break
        return counter < 4

    def table_mult(self, x: int) -> None:
        for i in range(1, 11):
            print(f'{i} x {x} = {i * x}')

    def all_tables_Mult(self) -> None:
        for i in range(1, 11):
            print(f'the molt table of {i} is :')
            print(self.table_mult(i))

    def list_div(self, x: int) -> List[int]:
        ldiv: List[int] = []
        for i in range(1, x + 1):
            if x % i == 0:
                ldiv.append(i)
        return ldiv
