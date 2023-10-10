""" 
def fibo(n)
{
  if( n == 0 || n == 1)
  {
  return 1
  }

}

int n;
cin>>n
fibo(n)
"""


def fibo(n):
    if n == 1 or n == 2:
        return [0,1]
    
    fibo_sq = [0,1]

    for i in range(2,n):
        ans = fibo_sq [-1 ]+fibo_sq[-2]
        fibo_sq.append(ans)
    return fibo_sq
n = int(input())

fb = fibo(n)
for num in fb:
    print(num,end=' ')






    
    
