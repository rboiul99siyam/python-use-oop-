class Parson:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class cricketer(Parson):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)
    def __add__(self,ohthers):
        return self.age + ohthers.age
    def __mul__(self,others):
        return self.weight * others.weight

sakib = cricketer('sakib',43,65,70)
musi = cricketer('musi',34,56,65)
print(sakib + musi)
print(sakib * musi)
