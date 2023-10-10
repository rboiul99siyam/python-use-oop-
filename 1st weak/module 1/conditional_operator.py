""" 
conditional  opeator:
1.>,<,>=,=<,==,!=
2. not useful for python : ++,--,
3.+= ,-=,*=,/=
4.in,not,not in ,is ,is not

today learn a course :

nested if condition end  if end elif end else 

"""

num1 = int(input("please Enter Your number : "))
boss = 'head'
# if num1 > 5:
#     print('are kodom ali ami kinto tur cheye boro ')

# elif num1 == 3:
#     print('bhai part loyen na ami ekon ')
# else:
#     print('sorry bro gorib manus amar sathe jamela koris na ')

# if num1 >= 20:
#     print(f'ami {num1} er cheye boro ')
# # elif num1 <= 15:
# #     print(f'ami {num1} er cheye choto')
# elif num1 == 10:
#     print(f'ami {num1} er soman')
# else:
#     print("ami gorib")

""" nested if condition  """
if num1 == 10 and boss is not True:
    print("Tur boss khaichee loss")
else:
    print("false")
    if num1 >10 or boss is True:
        print("loss")