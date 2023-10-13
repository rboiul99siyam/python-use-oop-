
import math
import time
def timer(fun):
    def inner(*args,**kargs):
        print('timer start ')
        fun(*args,**kargs)
        print('timer end')
    return inner

# timer()()
@timer
def get_factoral(n):
    print("factoryal start")
    start  = time.time()
    res = math.factorial(n)
    print(f'total res fact : {res}')
    end = time.time()

    print(f"total time your code : {end-start}")

n = int(input("Enter Your Int value Now : "))
get_factoral(n)