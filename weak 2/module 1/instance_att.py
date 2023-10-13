class Shop:
    Shopping_mall = "jamuna"

    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] # cart is intance attribute 
    
    def add_to_cart(self,item):
        self.cart.append(item)


bappa_raj = Shop("bappa-raj")

bappa_raj.add_to_cart("watch")
bappa_raj.add_to_cart("Menoy_bag")

print(bappa_raj.cart)

Naika_sabana = Shop("Sabana")

Naika_sabana.add_to_cart("LipStack")
Naika_sabana.add_to_cart("dress")
print(Naika_sabana.cart)




