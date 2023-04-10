class Parent():
    def __init__(self, Name, age):
        self.__name = Name
        self._age = age

class Child(Parent):
    def __init__(self, Name, age):
        super().__init__(Name, age)

    def funcA(self):
        print(self._age)

a = Child("jacon", 34)
a.funcA()