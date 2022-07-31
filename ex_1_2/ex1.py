from class1 import Rectangle
from class1 import Parallelepipede

length = int(input('enter length : '))
width = int(input('enter width : '))
Rec1 = Rectangle(length,width)
Rec1.display_Rec()

length_para = int(input('enter length : '))
width_para = int(input('enter width : '))
height_para = int(input('enter height  : '))
Para1 = Parallelepipede(length_para,width_para,height_para)
print(f'the volum is {Para1.display_Para()}')