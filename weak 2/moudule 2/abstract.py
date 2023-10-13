from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def eat(self):
        print("i need a fruit")
    @abstractmethod
    def move(self):
        pass

class manky(animal):

    def __init__(self,name) -> None:
        self.name = name
        super().__init__()
    
    def eat(self):
        print("hey nana, i am eating banana")
    def move(self):
        print('let,s go in the zoo')

layka = manky('layka')
print(layka.name)
layka.eat()
layka.move()