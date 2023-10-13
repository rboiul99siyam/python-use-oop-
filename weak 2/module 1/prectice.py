# # class sample:
# #     price = 1000
# #     brand = "oppo"
# #     color = 'red'

# # my_phone =sample()
# # print(my_phone.brand,my_phone.color,my_phone.price)


# # class mathod:
# #     price = 1000
# #     brand = 'Oppo'
# #     color = 'red'

# #     def call(self):
# #         print("i Love python")
    
# #     def sand_massage(self,phone_number,sms):
# #         print(f"sanding your {phone_number} in sms : {sms}")

# # my_phone = mathod()
# # my_phone.call()

# # my_phone.sand_massage(1248923,"I love bangladesh")


# class instanec:
#     def __init__(self,buyer):
#         self.buyer = buyer
#         self.cart = []
#     def add_to_cart(self,item):
#         self.cart.append(item)
    


# bappa_raj = instanec("bappa raj")

# bappa_raj.add_to_cart('watach')
# bappa_raj.add_to_cart('shoe')
# print(bappa_raj.cart)


# Naika_sabana = instanec("sabana ")
# Naika_sabana.add_to_cart('lipstack')
# Naika_sabana.add_to_cart('shoes')

# print(Naika_sabana.cart)




# from time import *
# import pyautogui
# sleep(5)
# for i in range(10):
#     pyautogui.write('sorry bhai')
#     pyautogui.press('enter')


class shopping :
    def __init__(self,name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self,item,price,quantity):
        product = {'item':item,'price':price,'quantity':quantity}
        self.cart.append(product)


    def chackout(self,amount):
        total = 0
        for item in self.cart:
            total+=item['price'] * item['quantity']
            print("total :",total)
            if amount < total:
                print()


alan = shopping('alan')

alan.add_to_cart('alu',12,2)
print(alan.cart)