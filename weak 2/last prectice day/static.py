""" class Libary:
    def __init__(self,book_name,book_id) -> None:
        self.book_name = book_name
        self.book_id = book_id
    
    @staticmethod
    def multiple(a,b):
        print(a * b)
    
    @classmethod
    def poper(self,a,b):
        res = a + b
        print(res)
    def __repr__(self) -> str:
        return f'{self.book_name} {self.book_id}'

book_shop = Libary('python',12)

Libary.multiple(3,5)
Libary.poper(4,3)
print(book_shop) """


class Myclass:
    def __init__(self,value):
        self.value = value
    
    @classmethod
    def class_method(self,insatance):
        insatance.value = insatance.value + 1
    
    @staticmethod
    def class_static(value1,value2):
        res = value1 * value2
        print("static : ",res)

# obj = Myclass(6)
# Myclass.class_method(obj)
# print(obj.value)
obj = Myclass(5)
Myclass.class_method(obj)
Myclass.class_static(10,10)
print(obj.value)