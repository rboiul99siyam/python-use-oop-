
"""
    1.ekane amora je eta function ta declar korlam seta kintu amader parent class e chil but children declar korar por se setake override kore amader ke children class e diye diche 

"""
class Parson:
    def __init__(self,name,age,weight) -> None:
       self.name = name
       self.age = age
       self.weight = weight
    
    def eat(self): # parent class is an eat function 
        print("vat ,mach,gosto,korma ,polao")
    
    def excerise(self):
        print("I do not like exerise ")


class cricketer(Parson):
    def __init__(self, name, age, weight,team) -> None:
        self.team = team
        super().__init__(name, age, weight)
    
   
    def eat(self): # override function 
        print("vegatable ,fish,meat,pinatbar,khejur,ods,milk,and protin food etc")
    
    def excerise(self): # override function 
        print('I like a gym ,and regular exarise our fitness and good health ')
    
    """ overloading mathod  in below """
    def __add__(self,others):
        return self.age + others.age
    
    def __mul__(self,others):
        return self.weight * others.weight
    
    def __len__(self):
        return self.weight
    def __gt__(self,others):
        return self.age > others.age
    

    def __repr__(self) -> str:
        return f'{self.name} {self.age} {self.weight} {self.team}'

sakib  = cricketer('sakib',38,56,'bd')
musi = cricketer('musi',36,59,"BD")
# print(sakib)
# sakib.eat()
# sakib.excerise()

print(40+50) # duita int add 
print("sakib" + 'Rabik') # concat korlam 
print([12,23,34] + [15,20,98]) # two list cancat korlam
print(sakib + musi)
print(sakib * musi)
print(sakib < musi)
print(len(sakib))





