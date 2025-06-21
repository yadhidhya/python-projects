# snake, water and gun game project

'''
let's assume 1 as snake
            -1 as water
             0 as gun
'''

import random
computer = random.choice([-1,0,1])
youstr=input("enter your choice: ")
youdict={"s":-1,"w":0,"g":1}
reversedict={-1:"snake",0:"water",1:"gun"}
you=youdict[youstr]
print(f"your choice is {reversedict[you]}\ncomputer's choice is {reversedict[computer]}")

if you == computer:
    print("it's a draw")
else:
    if (you == 1 and computer == -1):
        print("you win")
    elif (you==1 and computer==0):
        print("computer win")
    elif (you==-1 and computer==1):
        print("computer win")
    elif (you==-1 and computer==0):
        print("you win")
    elif(you==0 and computer==1):
        print("you win")
    elif(you==0 and computer==-1):
        print("computer win")
    else:
        print("something went wrong")