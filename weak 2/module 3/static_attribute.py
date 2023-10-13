class Shopping:
    cart = []
    orgin = 'china'
    def __init__(self,name,locality) -> None:
        
        self.name = name
        self.locality = locality
    
    def parchase(self,item,price,amount):
        reminder = amount - price
        print(f'item : {item}  price : {price}  amount : {amount} : {reminder}')
    
    @staticmethod
    def multuple(a,b):
        res = a*b
        print(res)
    @classmethod
    def hudai(self,item):
        print("hudai market jai shudu ac er batas khai ,",item)        
    


basu_na_dara = Shopping('basuo n dara ','Dkaka')
basu_na_dara.parchase('langui',500,1000)
Shopping.hudai('Langui')
Shopping.multuple(5,5)
basu_na_dara.multuple(30,10)
