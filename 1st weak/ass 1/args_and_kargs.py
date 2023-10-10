
# args 
# def args(num1,num2,num3,*numbers):
#     sum = 0
#     result = num1 + num2+num3
#     print("result : ",result)

#     for nums in numbers:
#         print(nums)
#     sum += nums
#     return sum
# total = args(10,20,30,40,50,60,70,80,90)
# print("total: ",total)

# kargs

def famous (fast_name,last_name,**addtion):
    name = fast_name + ' ' + last_name
    # print(name)
    print(addtion)
    return name
name = famous(title='Dr:',fast_name='Hiro',last_name='almo',addtion='Most pupolar singer of world ')
print(name)


