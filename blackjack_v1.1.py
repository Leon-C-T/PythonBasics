#!/usr/bin/env python3.8

import random

card_deck =  ['AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD', # Diamonds
              'AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH', # Hearts
              'AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS', # Spades
              'AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC'] # Clubs

def deal_func():                 ##### Function to deal a card and remove it from the deck of cards so it cannot be selected again #####
    x = random.choice(card_deck) #     Randomly picks a card from the deck
    card_deck.remove(x)          #     Removes the card from the deck of cards (card_deck)
    return x                     #     Returns the card back to wherever it was called
                                 

def card_map(n1):                ##### Function that maps Individual cards to an integer value e.g. all Aces = 1, All Jacks = 10 etc.. #####
    switcher = {
        'AD':1 , 'AH':1 , 'AS':1 , 'AC':1,
        '2D':2 , '2H':2 , '2S':2 , '2C':2,
        '3D':3 , '3H':3 , '3S':3 , '3C':3,
        '4D':4 , '4H':4 , '4S':4 , '4C':4,
        '5D':5 , '5H':5 , '5S':5 , '5C':5,
        '6D':6 , '6H':6 , '6S':6 , '6C':6,
        '7D':7 , '7H':7 , '7S':7 , '7C':7,
        '8D':8 , '8H':8 , '8S':8 , '8C':8,
        '9D':9 , '9H':9 , '9S':9 , '9C':9,
        'JD':10, 'JH':10, 'JS':10, 'JC':10,
        'QD':10, 'QH':10, 'QS':10, 'QC':10,
        'KD':10, 'KH':10, 'KS':10, 'KC':10,
        '10D':10,'10H':10,'10S':10, '10C':10
    }
    return switcher.get(n1)    # Returns back the value of a particular card

class attributes:               # A Class to hold and return values of a players particular hand.
    def __init__(self):    
        self.cards = []
        self.value = 0

    def current_cards(self):
        return self.cards
    
    def first_card(self):
        return self.cards[0]

    def hidden_card(self):
        return ', **Hidden**'

    def add_card(self):
        y = deal_func()
        self.cards.append(y)
        return y
    
    
    def total_value(self):       #test - RETURN OF VALUE WORKS
        return self.value
    
    def cards_value(self):       #test - VALUE OF CARDS TO MAP FUNCTION WORKS
        length = len(self.cards)
        self.value = 0
        for i in range(length):
            self.value = self.value + card_map(self.cards[i]) #test
        #self.value = self.value + card_map('9D') #test
        #print (self.value) #test
        #self.value = self.value + card_map('9H') #test
        
        #print (self.value) #test
        

#############################################                MAIN PROGRAM              #############################################



#############################################            1. INITIAL CARD DEAL          #############################################

print("Game of BlackJack 21 against the computer")
print("The Value of Ace in this game will be considered to be 1", '\n')
input("Press Enter to Continue")
player1 = attributes()      # Creates a Player 1 object
computer = attributes()     # Creates a computer object aka Dealer

input("Press Enter to deal your first card \n")                                                                ## Deal and show Player 1's First Card
player1.add_card()
print("Your Current Cards are: ", player1.current_cards())

computer.add_card()                                                                                         ## Deal and show Computers First Card
print("Computers' Current Cards are: ", computer.current_cards(), '\n')

input("Press Enter to deal your second card \n")                                                               ## Deal and show Player 1's Second Card
player1.add_card()
print("Your Current Cards are: ", player1.current_cards())

computer.add_card()                                                                                         ## Deal and show Computers Second Card
print("Computers' Current Cards are: ", "[ ", computer.first_card() , computer.hidden_card() , "]" , '\n')

# print (card_deck) #test - CARD DECK REMOVE FUNCTION WORKS
# print(player1.total_value()) #test
player1.cards_value()
computer.cards_value() 

# print("Your Current Cards are: ", player1.current_cards() , "With a Value of", player1.total_value(), '\n')



#############################################            2. HIT OR STAND          #############################################  

hit = True # To check if player want to take a card or not
bust = False # To Check if either player or computer has gone bust

while (hit == True):
    print("Would you like to Hit (Take a card) or Stand (Stop taking cards)?")
    key = input("Type h to 'Hit' or s to 'Stand': \n")
    key = key.lower()

    if key == 'h':  #IF HIT
        input("Press Enter to deal a card \n")                                   ## Deal Player 1 a Card
        player1.add_card()                              
        player1.cards_value()                                                 ## Checks current value of Player 1's cards

        if (player1.total_value() > 21):                                    ## If total value of Player 1's cards > 21
            print("Your Current Cards are: ", player1.current_cards() , "With a Value of", player1.total_value()) ## Displays player1's current cards and values
            # print("The value of your hand is greater than 21, YOU HAVE GONE BUST! ")                              ######## END
            hit = False                                                                                           ## Set while loop flag to false
            bust = True
        else:
            print("Your Current Cards are: ", player1.current_cards() , "With a Value of", player1.total_value(), '\n') ##Just prints current cards + value
        #break ## Included to prompt for Hit or Stand Again       

    if key == 's': #IF STAND
        hit = False   
            
    #else:
        #print("Invalid input \n")

print("Computers' Current Cards are: ", computer.current_cards(), "With a Value of", computer.total_value(),'\n')

while (computer.total_value() <= 16):       ##Continues running this code until the total value of the computer(Dealers) hand is 17 or more
        
            if computer.total_value() < 17: 
                input("Press Enter to see the computer deal a card \n")
                print("The computer has drawn another card")
                computer.add_card() 
                computer.cards_value()   
                print("Computers' Current Cards are: ", computer.current_cards(), "With a Value of", computer.total_value(),'\n') ## Displays computers current cards with value 
            if  computer.total_value() >= 17       ## If the total card value of the computer is < 17
                ## print("Computers' Current Cards are: ", computer.current_cards(), "With a Value of", computer.total_value(),'\n') 
                hit = False     ## Sets Hit Flag to false to break out
                if computer.total_value() > 21 and player1.total_value() <= 21:   ## Checks if the Computer total value is above 21 and Player1 total value is below 21
                    #print("The Computer has gone bust, You Win!") ######## END
                    bust = True
        
#############################################            3. End Conditions          #############################################  

if bust == True:        ## If either the computer or player has gone bust
    if player1.total_value() > 21:  ## Checks if Player has gone bust
        print("The value of your hand is greater than 21, YOU HAVE GONE BUST! ") ######## END
    if computer.total_value() > 21 and player1.total_value() <= 21:  ## Checks if computer has gone bust but player has not
        print("The Computer has gone bust, You Win!") ######## END
    
else:
    p1val = abs(player1.total_value()-21)    ## Calculates the absolute value of how close player 1 is to the value 21
    compval = abs(computer.total_value()-21)     ## Calculates the absolute value of how close the computers is to the value 21 

    if p1val < compval:                           ## If Player 1 is closer to 21 than Computer
        print("You are closer to 21 than the computer, You Win!")
    elif p1val > compval:                         ## If Computer is closer to 21 than Player 1
        print("The computer is closer to 21 than you are, You Lose!")
    elif p1val == compval == 21:                  ## If both the Computer and Player 1 have a hand of 21
        print("You and the computer both have a total hand value of 21 - You Draw!")
    else:                                         ## If both the Computer and Player 1 are the same distance away from 21
        print("You and the computer are the same distance away from 21 - You Draw!")