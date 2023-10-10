""" 
1.basic function declar kora shikhlam 

"""

# define

# 1. function 
def doble_it(nums):
    result = nums * 2
    print(result)

doble_it(10)

# 2. function 
def manu_bar():
    print('Manu bar')
    print('check your balance ')
    print('desopt now')
    print('cash out now')

manu_bar()
print('----------------------')
print('Enter your Amaount Now : ')
n = int(input())
sum =n*3

print('sumation now : ',sum)

# 3.function 
def sumation (nums1,nums2):
    result = nums1 + nums2
    return result



n = int(input("nums 1 : "))
m = int(input("nums 2 :"))
total = sumation(n,m)
print("sumation function Now : ",total)

