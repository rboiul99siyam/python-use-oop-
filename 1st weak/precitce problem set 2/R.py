n = int(input())

x = list(map(int,input().split()))

mx = max(x)
mn = min(x)

# print("mx and mn",mx,mn)

mx_idx = x.index(mx)
mn_idx = x.index(mn)

# print("mx_idx and mn_idx ",mx_idx,mn_idx)

tmp = x[mx_idx]
x[mx_idx] = x[mn_idx]
x[mn_idx] = tmp

for i in range(n):
    if i == n -1:
        print(x[i],end="")
    else:
        print(x[i],end=" ")
print()