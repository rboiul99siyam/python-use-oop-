class Phone:
    manufucturby = "china sngsong company "
    def __init__(self,owener,phone,brand,price):
        self.owener = owener
        self.phone = phone
        self.brand = brand
        self.price = price

    def sand_sms(self,phone_number,sms):
        text = f'sand sms {phone_number} and :{sms}'
        return text



my_phone = Phone("ami kala chan","iphone","apple",12000)
print(my_phone.owener,my_phone.phone,my_phone.brand,my_phone.price)
print(my_phone.manufucturby)
her_phone = Phone("she amar jan","oppo","china brand",201220)
print(her_phone.owener,her_phone.phone,her_phone.brand,her_phone.price)


res = my_phone.sand_sms(2342,'i Love python')
print(res)


