# # # number = 10
# # # number = 20
# # # print(number + number)

# # number1 = 10
# # print(number1)
# # number1 = 20
# # number1 = 30
# # print(number1)
# # number1 = 'hellp world'
# # print(number1)

# # num = "2"
# # num1 = 'hello world'
# # print(num + num1)

# # v = 10
# # n = '10'
# # x = 10.00
# # print(type(10))
# # print(type(n))
# # print(type(x))


# n = 5
# x = 2
# c =5%2
# d = 'hello world'
# print(n,x,c,d)


# name = input("What is your name ? ")
# print("Welcome to python ,",name,"!")

# from time import * 
# import pyautogui
# number1 = input("please intger an please enter press ")
# number1 = int(number1)
# number2 = input("please intger an please enter press ")
# number2 = int(number2)


# for i in range(1):
#     pyautogui.write("ekon asbe ajke sera cayacobi tar name holo number1 number2",interval=0.25)
#     pyautogui.press('enter')

# sleep(5)


# print("number1 + number2",number1 + number2,)
# print("number1 - number2",number1 - number2,)
# print("number1 * number2",number1 * number2,)
# print("number1 / number2",number1 / number2,)
# print("number1 // number2",number1 // number2,)
# print("number1 % number2",number1 % number2,)



# num = [10,20,30,40,50,60,70,80,90]
# num[0]=100
# print(num)

# serce = ['ban','af','in','sr','bu','pk','ne']

# print('number of contries of saarc : ',len(serce))

# x = 'in' not in  serce
# print(x)

# saarc = ['bangladesh','india','pakistan','sir-lanka','afganistan','butan','nepal']

# country = input("Enter the name of country : ")

# if country in saarc:
#     print(country,'is member of saarc')
# else:
#    print(country,"is not member of saarc ")

# print("program tarminate")

# year = int(input("Please interger an please enter prass : "))

# if year % 100 != 0 and year % 4 == 0:
#     print(year,'is leap year')
# elif year % 100 == 0 and year % 400 == 0:
#     print(year,"is leap year")
# else:
#     print(year,'is not leap year')

import turtle

# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.shape('turtle')
# turtle.exitonclick()
n = turtle.Screen()
start = turtle.Turtle()


for _ in range(3):
    start.forward(100)
    start.left(120)
turtle.exitonclick()
