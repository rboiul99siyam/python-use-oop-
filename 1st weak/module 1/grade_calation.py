nums = int(input("Your Exam  grade : "))

if nums >= 80 and nums <=100:
    print("Your Exam Grade A+ , marks ",nums)
elif nums >=70 and nums <= 79:
    print("Your Exam Grade A, marks",nums)
elif nums >=60 and nums <= 69:
    print("Your Exam Grade A-, marks" ,nums)
elif nums>= 50 and nums<=59:
    print("Your Exam Grade B, marks",nums)
elif nums>=40 and nums<=49:
    print("Your Exam Grade C ,marks",nums)
elif nums>=33 and nums<=40:
    print("Your Exam Grade D,marks",nums)
else:
    print("Your Fail")