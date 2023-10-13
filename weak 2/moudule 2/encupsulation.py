class Bank:
    def __init__(self,holder_name,initial_desopit) -> None:
        self.holder_name = holder_name # public 
        self.__balance = initial_desopit # private
        self._branch = 'Dhaka Bangladesh '

    

    def deposit(self,amount):
        self.__balance+=amount
    
    def _get_balance_check(self):
        return self.__balance
    def Withdow(self ,amount):
       if amount < self.__balance:
        self.__balance -= amount
        print(f'your current amount Now : {self.__balance}' )
       else:
          print("Sorry ,Your account not abileable menoy ")

Hero_alom = Bank("hero alom",1000)
print(Hero_alom.holder_name)
Hero_alom.deposit(5000)
Hero_alom.Withdow(44000)
Hero_alom._get_balance_check()
print(Hero_alom._branch)