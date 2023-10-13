class Phone:
    priec = 10200
    brand = 'oppo'
    color = 'red'

    def call(self):
        print("I love python ")
    
    def sand_massage(self,Phone_number , sms):
        text = f'Sending sms to : {Phone_number} and massage : {sms} '
        return text

my_phone = Phone()

print(my_phone.brand)
my_phone.call()

res = my_phone.sand_massage(1020494339,"Missy ,I forget miss You ")
print(res)
