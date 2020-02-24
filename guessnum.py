#!/usr/bin/env python3.8

import random
comp_guess = random.randint(0,100)

print("Try to guess a randomly generated number between 0-100")
y = 1
print(comp_guess)
x = int(input("What is your first guess?: ")) 
print ("Attempt ", y)
if (x > comp_guess):
    print("Guess Lower")
elif(x < comp_guess):
    print("Guess Higher")


if (x == comp_guess):
    print("Congratulations, You've guessed the number correctly")    
else:
    while x != comp_guess: 
        y = y+1
        x = int(input("You have guessed the number wrong, What is your next guess? ")) 
        print("Attempt ", y)   
        if (x > comp_guess):
            print("Guess Lower")
        elif(x < comp_guess):
            print("Guess Higher") 
    print("Congratulations, You've guessed the number correctly")
    
