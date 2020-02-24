#!/usr/bin/env python3.8

import random


print("A game of Rock, Paper, Scissors against the computer")
print("Enter y to exit ")
ex = 'y'

while (ex != 'n'):
    comp_selection = random.randint(1,3)
    x = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
    print(comp_selection)
    if x == 1:
        if comp_selection == 3:
            print("Computer picked Scissors, You Win")
        elif comp_selection == 2:
            print("Computer picked Paper, You Lose")
        elif comp_selection == 1:
            print("Computer picked Rock, It's a Draw")
    elif x == 2:
        if comp_selection == 3 :
            print("Computer picked Scissors, You Lose")
        elif comp_selection == 2 :
            print("Computer picked Paper, It's a Draw")
        elif comp_selection == 1 :
            print("Computer picked Rock, You Win")
    elif x == 3:
        if comp_selection == 3:
            print("Computer picked Paper, You Win")
        elif comp_selection == 1:
            print("Computer picked Rock, You Lose")
        elif comp_selection == 3:
            print("Computer picked Scissors, It's a Draw")
    else:
        print("You have chosen an invalid input, please try again")   
    ex = input("Would you like to continue (y/n)?")          
        