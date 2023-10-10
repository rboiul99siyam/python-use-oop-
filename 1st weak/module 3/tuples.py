def multiple ():
    return 4,3,3
print("multiple return : ",multiple())

thing = 'pen','sunglass','phone','papaer','charger','mouse','laptob'
x = ['pen','sunglass','phone','papaer','charger','mouse','laptob']
# print(type(thing))
if 'phone' in thing:
    print("ache")
for item in x:
    print(item,end=" ")


x1 = ' '.join(thing[::-1])
print("\n",x1)





