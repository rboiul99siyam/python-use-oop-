class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdrow = 100
        self.max_withdrow = 100000
    
    def get_balance(self):
        return self.balance
    

    def deposit(self,amount):
        if amount < 0:
            print("Sorry,Your amount is Invlid")
        else:
            self.balance +=amount
            print(f"Your current balance: {self.get_balance()}")
    

    def Withdraw(self,amount):
        if amount < self.min_withdrow:
            print(f"Sorry,You can withdraw below : {self.min_withdrow}")
        elif amount > self.max_withdrow:
            print(f"Sorry we are unable to get the money to our bank:{self.max_withdrow} ")
        else:
            self.balance -=amount
            print(f'Here is Now menay withdrow: {amount} ')
            print(f'Here is Now menay withdrow: {self.get_balance()} ')


# brac = Bank(15000)
# brac.Withdraw(2300)
# # brac.Withdraw(100000000000)
# # res = brac.deposit(100)
# # print(res)
# brac.deposit(100)
# brac.deposit(200)
# print(brac.get_balance())


