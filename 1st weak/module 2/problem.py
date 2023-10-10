""" def solve(a,b):
    return a**b
result = solve(2,4)
print(result)

def display_parson (** keywords):
    for key,value in keywords.items():
        print(f"{key} : {value}" )

display_parson(name = "Amir khan ",Age = "45")

numbers = [7,8,5,4,3,2,4]
print(numbers[::-1])

numbers =[22,19,19,14,33]
numbers.sort()
print(numbers) """


""" numbers = [12,23,43,53,69,87]

i = 0
j = len(numbers) - 1
while i<j:
    tmp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = tmp
    i+=1
    j-=1
print("Swap trcks , ",numbers) """

# function use kore amar swap trecks use korbo 

""" def swap_trcks (numbers):

    i = 0
    j = len(numbers)-1
    tmp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = tmp
    return numbers

newlist = [12,43,54,8 ,87]

swap_tc = swap_trcks(newlist)
print("Element swap : ",swap_tc) """

""" def swap_two_poss(numbers,pos1,pos2):
    numbers[pos1] , numbers[pos2] = numbers[pos2] ,numbers[pos1]

    return numbers

numbers = [1,2,3,5,6]
po1 = 1
po2 = 3
swap_frd = swap_two_poss(numbers,po1-1,po2-1)
print(swap_frd)
 """

""" n = [10, 20, 30]

length = len(n)
print("This list of len",length) """
""" 
test_list = [1, 6, 3, 5, 3, 4]
n = 1
for i in test_list:
    if(i == n):
        print('True')
        break
else:
    print('false') """


# num = [1,23,44,556,]
# num.clear()
# print(num)

""" test_list = [4, 5, 6, 7, 8, 9]
print(test_list[::-1]) """

str1 = "Jemes"
f1 =str1[0]
ls1 =len(str1)
md = int(ls1/2)
res1 = f1 +  str1[md]
res = f1 + str1[ls1-1]


# mid = (f1 + ls1)/2


print(res,res1)



