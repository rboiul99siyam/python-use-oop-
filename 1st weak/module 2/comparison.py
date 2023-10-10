numbers = [43,55,12,65,76]

odds = []

for nums in numbers:
    if nums % 2 == 1 and nums % 5 == 0:
        odds.append(nums)

print(" odd  number , ",odds)


players = ['sakib','musfik']
run =  [32,43,54]

run_comb =[]
for player in players :
    print(player)
    for runs in run:
        print(player,runs)
        run_comb.append([player,runs])
print(run_comb)
