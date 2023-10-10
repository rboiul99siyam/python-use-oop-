""" 
1. multiple agrs 
2. kargs peramitar 

"""
def full_name(fast,last):
    result = fast + ' ' + last
    return result

name = full_name('alo','vaji')
print(name)


def famous_name(fast,last,**addtion):
    name = fast + ' ' + last 
    print("keys  , ",addtion)
    return name
name = famous_name(title='Dr:',fast='hero',last='alom ',addtion='saheb',title1='mia')
print(name)

a = 4765
b = 4670
result = a - b
mul = result * 5.88
print(mul)

result1 = 110
mul1 = result1 * 5.88
print(mul1)