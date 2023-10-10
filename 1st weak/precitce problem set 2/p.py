
n = int(input())
rev = []
x = []
x = list(map(int,input().split()))
rev = x[::-1]

if x == rev:
    print("YES")
else:
    print("NO")