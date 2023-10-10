from math import *
from turtle import *
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
    # print(x)


colors = ['red','green','blue','orange','yellow']

t = turtle.circle(80)
print(t)
# result = ceil(44.444)
# result1 = floor(44.444)
# print(result)