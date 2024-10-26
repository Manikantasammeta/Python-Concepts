from abc import ABC,abstractmethod
class A(ABC):
    def method1(self):
        print("method one")
    @abstractmethod
    def method2(self):
        print("ab method 2")
        print("i am mani")
    @abstractmethod
    def method3(self):
        print("ab method 3")


class B(A):
    def method2(self):
        pass
    def method3(self):
        pass

m=B()
m.method1()
m.method2()
m.method3()