from class1 import Rectangle
from class1 import Parallelepipede

while True:
    try:
        length = int(input('enter length : '))
        width = int(input('enter width : '))
    except ValueError:
        print('invalid input , --> need int')
        continue
    else:
        rec1 = Rectangle(length, width)
        rec1.display()
        print(rec1.perimeter)
        break

while True:
    try:
        length_para = int(input('enter length : '))
        width_para = int(input('enter width : '))
        height_para = int(input('enter height  : '))
    except ValueError:
        print('invalid input , --> need int')
        continue
    else:

        para1 = Parallelepipede(length_para, width_para, height_para)
        para1.display()
        break
