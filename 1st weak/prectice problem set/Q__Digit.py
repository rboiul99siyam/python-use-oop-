
# def print_reverse_digit(n):
#     print_digit = n[::-1]
#     print(print_digit)


# t = int(input())
# for n in range(t):
#     n = input()
    
#     print_reverse_digit(n)



t = int(input())

while t != 0:
    n = int(input())
    while True:
        print(n%10,end=" ")
        n//=10
        if(n == 0):
            break
    print()
    t-=1

 