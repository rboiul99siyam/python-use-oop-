

s = input()

cnt_l = 0
cnt_r = 0

ans = []
st = ""
cnt  = 0
for n in s:
    if n == 'L':
        cnt_l += 1
        st+=n
    if n == 'R':
        cnt_r += 1
        st+=n

    if cnt_l == cnt_r:
        ans.append(st)
        st=""
        cnt_l = 0
        cnt_r = 0
        cnt+=1



print(cnt)


for i in ans:
    print(i)


    

