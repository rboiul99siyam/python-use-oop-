class User:
    def __init__(self,name,age,money) -> None:
        self._name = name
        self._age = age
        self.__money = money
    
    @property
    def age(self):
        return self._age
    
    @property
    def salary(self):
        return self.__money
    
    @salary.setter
    def salary(self,value):
        if value<0:
            print("Negitve is not valid ")
        else:
            self.__money +=value

Samsu = User('Sumsu',21,15000)
print(Samsu.age)
print(Samsu.salary)
Samsu.salary = 5000
print(Samsu.salary)