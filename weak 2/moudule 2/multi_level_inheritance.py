class veicals:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price
    
    def move(self):
        pass
class Bus(veicals):
    def __init__(self, name, price,seat) -> None:
        self.seat = seat
        super().__init__(name, price)
class Big_Truck(veicals):
   def __init__(self, name, price,weight) -> None:
       self.weight = weight
       super().__init__(name, price)
    
class AcBus(Bus):
    def __init__(self, name, price, seat,tempareture) -> None:
        self.tempareture = tempareture
        super().__init__(name, price, seat)
    
    def __repr__(self) -> str:
        return f"{self.name} {self.price} {self.seat} {self.tempareture}"

green_line = AcBus('green line',500000,22,15)
print(green_line)
