'''
The computer picks a random number between 1 and 100.
You enter guesses.
The program gives you hints until you guess it correctly.
Finally, it displays how many attempts you took.

'''

import random
n = random.randint(1, 100)
a=-1
guesses=0
while(a!=n):
    guesses+=1
    a=int(input("Guess the number: "))
    if(a>n):
        print("lower number please")
    elif(a<n):
        print("higher number please")
print(f" You have guessed the number {n} correctly in {guesses} attempts")
