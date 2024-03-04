""" ## Card Game

The following script will create a deck of cards, shuffle it and display it in four columns
"""

import random

def createDeckOfCards():
    """ This function will return the deck of cards """
    suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack', 'Queen', 'King']
    return [(rank, suit) for rank in ranks for suit in suits]

def getCardName(card): #get full card name
    return f'{card[0]} of {card[1]}'

def displayCard(card):
    """ print the provided cards in four columns """
    i = 0

    while i < 52:
        print(f'{getCardName(card[i]):<20}{getCardName(card[i+1]):<20}{getCardName(card[i+2]):<20}{getCardName(card[i+3]):<20}')
        i += 4
        
def shuffleCard(card):
    """ this function will shuffle the provided list"""
    random.shuffle(card)

cards = createDeckOfCards()
shuffleCard(cards)
displayCard(cards)