n,q = input().split()
n = int(n)
q = int(q)

ar = list(map(int,input().split()))

pre = [0]*n
pre[0] = ar[0]

for i in range(1,n):
    pre[i] = ar[i] + pre[i-1]


while q!= 0:
    l,r = map(int,input().split())
    l-=1
    r-=1
    if l == 0:
        sum_val = pre[r]
    else:
        sum_val = pre[r] - pre[l-1]
    print(sum_val)

q-=1