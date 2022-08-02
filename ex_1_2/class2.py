class Person:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def display(self) -> None:
        print(f'The person name is {self.name} and his age is {self.age}')


class Student(Person):
    def __init__(self, name: str, age: int, section: str):
        super().__init__(self, name, age)
        self.section: str = section

    def display(self) -> None:
        print(f'The Student name is : {self.name}')
        print(f'The Student age is  : {self.age}')
        print(f'The Student section is :  {self.section}')
