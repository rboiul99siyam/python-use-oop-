class animal:
    def __init__(self,name) -> None:
        self.name = name
    
    def make_a_sound(self):
        print("animal making some sound ")
    
class cat(animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_a_sound(self):
        print('mewo mewo')


class dog(animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    

    def make_a_sound(self):
        print("ghew ghew")


class Tiger(animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_a_sound(self):
        print('halum halum')

done = cat('Real Don')
done.make_a_sound()

shpad = dog('shpad')
shpad.make_a_sound()

tiger_hasan = Tiger('Tiger')
tiger_hasan.make_a_sound()