from typing import TextIO

d = {'d': 99,'d2':'j'}
print(type(d['d']))
print(type(d['d2']))



print('the {2} {0} {1}'.format('fox',4,[4,5,6,'ttt']))

print(' ')

d1 = {'k1':'bbb',
     'k2':[0,1,2,3],
     'k3':{'k_in':['a','b','c']}
     }
print(d1)

d2 = {'k4':44}
print(d2)
print(' ')
d1['k4'] = d2['k4']
print(d1)

# output (4+3) ^ 2 = 49


str = 'ariel'
print(str[2])
print(str[2:3])
li = [1,5,8,3,7,3,7]
li.sort()
print(li)
print('jhgfddfdfffffffffff')
d = {'a1':[1,2,{'a2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['a1'][2]['a2'][1]['tough'][2][0])

lis = [1,2,4,5,6,3,2,3,4,5,6,6,8]
myset = set(lis)
print(myset)
print('-----------')
for i in lis:
    myset.add(i)

print(myset , 'good')
x = 4
print(x**0.5)

spil = 'print only the words that start with s in this statment'
index_list = [x[0] for x in spil.split()]
print(index_list)



print(' ')
print(' ')

def func(*args,**kwargs):
    print(args)
    print(kwargs)
    return kwargs


result = func([1,2,3,4],123,(1,2,3),fff = 'fff',ff = 'ff',f = 'f')
print(' ')
print(result['fff'])




def tr(dic):
    if dic %2==0:
        return 'evan'


dic = {'d': 99,'d2':88,'d3': 8,'d4':4}
jj = list(map(tr,dic.values()))
print(jj)

names = ['alibab','shuly','blali']
print(list(map(lambda name:name[::-1] ,names)))

class Dog():
    def __init__(self,breed,age,color):
        self.breed = breed
        self.age = age
        self.color = color

    def print_info(self):
        print('''
        hello ist me you colling for???
        i was wondring to my self if you are ther...
         plesae dont go to the lite !!!
        ''')
        print(f'the dog info is {self.breed} and {self.age} ade {self.color}')




ali = Dog("sheperd",22,'black')
print(ali.print_info())
print(type(ali))
