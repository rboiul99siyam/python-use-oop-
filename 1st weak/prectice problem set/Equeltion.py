a , b= input().split()
x = int(a)
y = int(b)


sumation  = 0
# print("power ,",pow(x,y))

for i in range(2,x+1,2):
    sumation += pow(x,i)
print(sumation)




    