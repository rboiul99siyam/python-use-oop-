from turtle import *
from time import *

sleep(5)

while True:
    forward(200)
    left(170)
    right(50)
    down(1000)
    if abs(pos()) < 1:
        break


