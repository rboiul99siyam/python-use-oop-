class Shop:

    cart = [] #cart is an class attribute 
    def __init__(self,buyer):
        self.buyer = buyer
    

    def add_to_cart(self,items):
        self.cart.append(items)

mehajeen = Shop("Mehajeen")
mehajeen.add_to_cart("shoes")
mehajeen.add_to_cart("LipStack")

print(mehajeen.cart)



Nisho = Shop("Nisho")
Nisho.add_to_cart('cap')
Nisho.add_to_cart('watch')
print(Nisho.cart)

    