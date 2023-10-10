""" 
1.global variable 
2.local scope variable 
3.you can access global variable without using the gloal keyword
4.if you want modifiy global variable , you have to using global keyword 
"""

balance = 3000

def buy_things (item,price):
    global balance
    print("Previos balance value  : ",balance)
    balance -= price
    print("after balance buying  : ",balance)

total = buy_things('sanglass',1000)


