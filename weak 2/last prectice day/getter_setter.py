# class User:
#     def __init__(self,name ,age,salary) -> None:
#         self.name = name
#         self._age = age
#         self.__menoy = salary
    
#     # getter is a readonly
#     @property
#     def age(self):
#         return self._age

#     #getter 
#     @property
#     def salary(self):
#         return self.__menoy
    


#     @salary.setter
#     def salary(self,value):
#         self.__menoy +=value

#     def __repr__(self) -> str:
#         return f'{self.name} {self.age} {self.menoy}'

# Samu = User('Samu',21,12000)
# # print(Samu._age)
# # print(Samu.age()) # amar jokhn method use kori tokhn amader age()use korte hoy 
# print(Samu.age)
# print("Oldest salary : ",Samu.salary)

# Samu.salary = 5000
# print("Your current salary : ",Samu.salary)


class sampleClass1:

    def __init__(self,a):
        self.__a = a
    

    @property
    def getter(self):
        return self.__a*2
     
    def sal(self,a):

        if a>0 and a % 2 == 0:
            self.__a = a
        else:
            self.__a = 2

obj = sampleClass1(8)
print(obj.getter)
obj.set_a = 5
print(obj.set_a())