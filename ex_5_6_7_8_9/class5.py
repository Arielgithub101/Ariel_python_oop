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
        flag: int = 0
        if x <= 1: return False
        for i in range(1, x + 1):
            if x % i == 0:
                flag += 1
                if flag > 2: break
        return (flag == 2)

    def test_prims(self, x: int, y: int) -> bool:
        flag: int = 0
        max_num: int = max(x, y)
        if x or y <= 1: return False
        for i in range(1, max_num + 1):
            if x % i == 0 and y % i == 0:
                flag += 1
                if flag > 2: break
        return (flag == 2)

    def table_mult(self, x: int) -> None:
        for i in range(1, 11):
            print(f'{i} x {x} = {i * x}')

    def all_tables_Mult(self) -> None:
        for i in range(1, 11):
            print(f'the molt table of {i} is :')
            print(self.table_mult(i))

    def list_div(self, x: int) -> List[int]:
        ldiv = []
        for i in range(1, x + 1):
            if x % i == 0:
                ldiv.append(i)
        return ldiv
