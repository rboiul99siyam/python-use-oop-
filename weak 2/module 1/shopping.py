class Shoping:

    def __init__(self,name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self,item,price ,quantity):
        product = {'item' : item,'price':price,'quantity':quantity}
        self.cart.append(product)
    

    def remove_item(self,item):
        for item in self.cart:
            self.cart.remove(item)
            print("Removed item : ",item)
            
            


    def chackout(self,amount):
        total = 0
        for item in self.cart:
            # print(item)
            total+=item['price'] * item['quantity']
        print("tatal: ",total)
        if amount < total:
                print(f"Please provide {total - amount} more menay ")
        else:
             extra = amount - total
             print(f'Here is items and extra menay {extra}')


    
Alan = Shoping('Masud')
Alan.add_to_cart('alu',50,1)
# Alan.add_to_cart('dim',5,12)
# Alan.add_to_cart('kaca moric',120,1)
# Alan.add_to_cart('murgi',160,2)

print(Alan.cart)
Alan.chackout(670)
# Alan.chackout(470)

# Alan.remove_item('quantity')

