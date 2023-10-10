""" with open ('massage.txt','w') as file:
    file.write('I Love Python !') """

# with open ('massage.txt','a')as file:
#     file.write('i love python !\n')
with open ('massage.txt','r')as file:
   text = file.read()
   print(text)