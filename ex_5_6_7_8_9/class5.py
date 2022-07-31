class Coputation:
    def __init__(self):
        pass

    def Factorial(self, x):
        t = 0
        while x > 0:
            t *= x
            x -= 1
        return t
    def Sum1(self,x):
        total = 0
        while x > 0:
            total += x
            x -+ 1
        return total

    def testPrim(self,x):
        flag = 0
        if x <= 1: return False
        for i in range(1 , x+1):
            if x%i == 0:
                flag += 1
        return (flag == 2)

    def testPrims(self, x,y):
        pass
    def tableMult(self,x):
        for i in range(1,11):
            print(f'{i} x {x} = {i*x}')
    def allTablesMult(self):
        for i in range(1,11):
            print(f'the molt table of {i} is :')
            for j in range(1,11):
                print(f'{j} x {i} = {j*i}')
    def listDiv(self,x):
        Ldiv = []
        for i in range(1, x + 1):
            if i % 2 == 0:
                Ldiv.append(i)
        return Ldiv