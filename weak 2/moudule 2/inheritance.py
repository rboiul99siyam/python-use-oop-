
# inheritance --> based clase -->parent clase -->child class 

class Gadget:
    def __init__(self,brand,color,price,manufactureBy) -> None:
        self.brand = brand
        self.color = color
        self.price = price
        self.manufactureBy = manufactureBy
    def run(self):
        return f'Runing Loptob {self.brand} and Huge costomer in parchase '
    
class Loptob(Gadget):

    def __init__(self,brand,color,price,manufacture,ssd,momory) -> None:
        self.ssd = ssd
        self.momory = momory
        super().__init__(brand,color,price,manufacture)
    def __repr__(self) -> str:
        return f'Loptob : {self.brand} {self.color} {self.price} {self.manufactureBy} {self.momory} {self.ssd}'

    def coding(self):
        return f'{self.brand} is very good sarvice and Huge costomer Useable '
    

class Phone(Gadget):
    def  __init__(self,brand,color,price,manufacture,dual_sim) -> None:

        self.dual_sim = dual_sim
        super().__init__(brand,color,price,manufacture)

    def calling(self,phone_number,text):
        return f'sanding to sms {phone_number} with : {text}'
    
    def __repr__(self) -> str:
        return f'phone : {self.brand} {self.color} {self.price} {self.manufactureBy},{self.dual_sim}'

class commera(Gadget):
    def __init__(self,pixel) -> None:
        self.pixel = pixel
    

    def _camera_lins(self):
        pass

    

My_phone = Phone('apple','red',12299,'china',True)
# print(My_phone.brand,My_phone.color,My_phone.price,My_phone.manufactureBy,My_phone.dual_sim)

print(My_phone)

my_loptob = Loptob('Toshba','black',52000,'chila sngsoung lid',120,45)
print(my_loptob)


        