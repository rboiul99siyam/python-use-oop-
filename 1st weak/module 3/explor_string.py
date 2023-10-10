name = 'sakib khan '
name2 = " sakib khan "
name3 = """ sakib
 khan 
 number 
 one 
"""

# print(name3)

# name[0] = 'R'
# print(name)

print(name.upper())
print(name.title())
print(name.swapcase())
print(name.count('s'))
print(name.find('khan'))
print(name.index('han'))

if 'x' in name:
    print("ache")
else:
    print("nai")


str = '#'.join('head')
print(str)

str = 'Good morning'
print("Orgianal sring  : ",str)
new_string = str.replace('Good','Great')
print(new_string)