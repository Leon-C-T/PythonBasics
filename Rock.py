#!/usr/bin/env python3.8

import random

counter = 1
rock_c = 0
paper_c = 0
scissors_c = 0
rock_avg = 0
paper_avg = 0
scissors_avg = 0

print("A game of Rock, Paper, Scissors against the computer")
print("Enter y to exit ")
ex = 'y'
comp_selection = random.randint(1,3)

while (ex != 'n'):
    
    x = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
    print(comp_selection)
    if x == 1:
        if comp_selection == 3:
            print("Computer picked Scissors, You Win")
        elif comp_selection == 2:
            print("Computer picked Paper, You Lose")
        elif comp_selection == 1:
            print("Computer picked Rock, It's a Draw")
        rock_c = rock_c + 1

    elif x == 2:
        if comp_selection == 3 :
            print("Computer picked Scissors, You Lose")
        elif comp_selection == 2 :
            print("Computer picked Paper, It's a Draw")
        elif comp_selection == 1 :
            print("Computer picked Rock, You Win")
        paper_c = + 1
    
    elif x == 3:
        if comp_selection == 2:
            print("Computer picked Paper, You Win")
        elif comp_selection == 1:
            print("Computer picked Rock, You Lose")
        elif comp_selection == 3:
            print("Computer picked Scissors, It's a Draw")
        scissors_c = scissors_c + 1
    else:
        print("You have chosen an invalid input, please try again")  
    
    
    rock_avg = rock_c / counter 
    paper_avg = paper_c / counter
    scissors_avg = scissors_c / counter   
    counter = counter + 1

    if rock_avg >= (paper_avg or scissors_avg): #if the user picks rock more times than anything else
        comp_selection = 2 #set computer choice to paper
    elif paper_avg >= (rock_avg or scissors_avg): #if the user picks paper more times than anything else
        comp_selection = 3 #set computer choice to scissors
    elif scissors_avg >= (rock_avg or paper_avg): #if the user picks scissors more times than anything else
        comp_selection = 1 #set computer choice to rock
    elif counter == 15:
        comp_selection = random.randint(1,3)


    ex = input("Would you like to continue (y/n)?")          
        