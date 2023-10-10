""" 

int t;
cin>>t;
while(t--)
{
  int a,b;
  cin>>a>>b;
  sum = 0;
  

}
"""


def print_sum_odd(x,y):
    sumOdd = 0
    
    mx = max(x,y)
    mn = min(x,y)

    for i in range(mn+1,mx):
        if(i % 2 != 0):
            sumOdd +=i

    print(sumOdd)        



t = int(input())
while t!=0:
    a,b = input().split()
    x = int(a)
    y = int(b)
    print_sum_odd(x,y)
        
    t-=1    