
n = int(input())
x = list(map(int, input().split()))

cnt = 0
mn = 1e12
flag = True

for i in range(n):
    if x[i] % 2 == 1:
        flag = False
        print('0')
        break

if flag:
    for i in range(n):
        cnt = 1
        x[i]//=2
        while True:
            if x[i] % 2 != 0:
                break
            else:
                x[i] //= 2
                cnt += 1

        mn = min(mn, cnt)

    print(mn)


