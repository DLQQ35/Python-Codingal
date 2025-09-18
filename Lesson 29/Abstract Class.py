from abc import ABC,abstractmethod

class ABsclass(ABC):
    def print(self,x):
        print("The passed value is:",x)
    @abstractmethod
    def task(self):
        print("We are inside ABsclass.")
class test_class(ABsclass):
    def task(self):
        print("We are inside 'test_class'.")
obj = test_class()
obj.task()
obj.print(100)