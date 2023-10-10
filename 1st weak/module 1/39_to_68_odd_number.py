nums = int(input("Odd number count 1 to 20 :: "))
cnt = 0
for nums in range(1,nums,2):
    # if nums % 2 == 1:
    cnt+=1
    print("Odd number  : ",nums)
print("count a odd value : ",cnt)