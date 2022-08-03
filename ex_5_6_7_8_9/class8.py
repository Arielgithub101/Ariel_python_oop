from typing import List


class myString(str):
    def __new__(cls, content):
        return str.__new__(cls, content)

    def append(self, x: str) -> None:
        print('in')
        self = self + x
        print(self)

    # def pop(self) -> None:
    #     size: int = len(self.content)
    #     self.content = self.content[:size - 1]

    def printMe(self):
        print(self)
