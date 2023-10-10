# def name(x):
#     return x*2


name = lambda number1 ,number2,number3 : number1 + number2 + number3

square = lambda num1 : num1*num1
dobled_num = lambda num : num * 2
# print(dobled_num(5))
# print(square(9))
# print(name(2,2,3))

numbers = [11,6,3,9,12,32,87]
dobled_nums = map(lambda x : x * 2,numbers)
square_nums = map(lambda x : x * x ,numbers)
# print(numbers)
# print(list(dobled_nums))
# print(list(square_nums))


actors = [ 

    {'name ' : ' shakib0','age' : 44},
    {'name ' : ' rakib','age' : 64},
    {'name ' : ' akib','age' : 74},
    {'name ' : ' nakib','age' : 24},#->
    {'name ' : ' bekib','age' : 28},
    {'name ' : ' sikab','age' : 44}
]
 


# name = filter ( lambda peramitar : peramitar[] < ,jar upar function call korbo tar nanme actors)

jouinor =  filter(lambda actor : actor['age'] < 40,actors)
print(list(jouinor),'\n')