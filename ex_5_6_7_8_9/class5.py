class Coputation:
    def __init__(self):
        pass

    def factorial(self, x:int) -> int:
        t = 0
        while x > 0:
            t *= x
            x -= 1
        return t
    def sum1(self, x:int) -> int:
        total = 0
        while x > 0:
            total += x
            x -= 1
        return total

    def testPrim(self, x:int) -> int:
        flag = 0
        if x <= 1: return False
        for i in range(1 , x+1):
            if x%i == 0:
                flag += 1
        return (flag == 2)

    def test_prims(self, x:int,y:int):
        pass
    def table_mult(self,x:int):
        for i in range(1,11):
            print(f'{i} x {x} = {i*x}')
    def all_tables_Mult(self):
        for i in range(1,11):
            print(f'the molt table of {i} is :')
            for j in range(1,11):
                print(f'{j} x {i} = {j*i}')
    def list_div(self,x:int) -> list:
        Ldiv = []
        for i in range(1, x + 1):
            if i % 2 == 0:
                Ldiv.append(i)
        return Ldiv