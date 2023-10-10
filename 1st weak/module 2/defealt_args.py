""" 
1. defealt agrs janbo 
2. multiple variable niye janbo 

"""

def sum (num1,nums2):
    result = num1 + nums2
    return result
total = sum(20,30)
print('total sum ,',total)

def args(num1,num2,*numbers):
    sum = 0
    result = num1 + num2
    print('result ,', result)
    for nums in numbers:
       print(nums)
    sum += nums
    return sum 

total = args(10,20,30,40,50)
print('total agrs ,',total)
