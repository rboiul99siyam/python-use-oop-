class calcolator:
    brand = "Casio Ms94"
    def add (self , num1,num2):
        res = num1 + num2
        return res
    def dudect(self,num1,num2):
        res = num1 - num2
        return res
    
    def divide(self ,num1,num2):
        res = num1 / num2
        return res
    def multiple (self,num1,num2):
        res = num1 * num2
        return res
    def reminder (self,num1,num2):
        res = num1 % num2
        return res
    
    


my_calcolar = calcolator()

print(my_calcolar.brand)

addition = my_calcolar.add(12,23)
print("additon of two number : ",addition)


dudection = my_calcolar.dudect(20,12)
print("deduction of two number : ",dudection)


dividation = my_calcolar.divide(21,10)
print("divide of two number : ",dividation)


multiplacation = my_calcolar.multiple(23 ,20)
print("Multipatactio of two number : ",multiplacation)


remaind = my_calcolar.reminder(21,10)
print("Remaider of two number : ",remaind)




