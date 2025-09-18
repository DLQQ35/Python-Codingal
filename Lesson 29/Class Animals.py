from abc import ABC,abstractmethod

class animal(ABC):
    def move(self):
        pass
class humans(animal):
    def move(self):
        print("I can walk and run.")
class dogs(animal):
    def move(self):
        print("I can bark.")
class snakes(animal):
    def move(self):
        print("I can crawl.")
class lions(animal):
    def move(self):
        print("I can roar.")

a = humans()
a.move()

b = dogs()
b.move()

c = snakes()
c.move()

d = lions()
d.move()