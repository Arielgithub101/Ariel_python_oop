class Person:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'The person name is {self.name} and his age is {self.age}')
class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(self, name, age)
        self.section = section

    def displayStudent(self):
        print(f'The Student name is : {self.name}')
        print(f'The Student age is  : {self.age}')
        print(f'The Student section is :  {self.section}')