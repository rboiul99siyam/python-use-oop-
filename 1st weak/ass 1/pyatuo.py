import pyautogui
from time import *

n = int(input("Enter Your Integar Numbar : "))
sleep(5)
for i in range(n):
    for j in range(i+1):
        pyautogui.write('# ',interval=0.25)
    pyautogui.press('enter')


     # 
     # # 
     # # # 
     # # # # 
     # # # # # 
     
    