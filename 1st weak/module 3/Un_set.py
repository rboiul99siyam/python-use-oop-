""" 
list --->
set : unique items collection 
tuples ->

"""


number = [12,23,54,23,89,89,12,43,54]
print("index",number.index(12))
print("Orginal : ",number)
num_set = set(number)
print("set -> : ",num_set) 
num_set.add(100)
print("add : ",num_set)
num_set.remove(12)
print("remove : ",num_set)

A = {1,2,3}
b = {1,2,3,4,5}
print("common : ",A & b)

print("Uncommon ",A | b)

for i in num_set:
    print(i,end=" ")


if 0 in num_set:
    print("exits")

