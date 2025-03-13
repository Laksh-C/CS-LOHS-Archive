# g_black_jack.py
"""
title: Black Jack
Author: Laksh Chopra
Date-Created: 13/10/22
"""

from f_deck_of_cards import *

### --- FUNCTIONS --- ###

### --- INPUTS
def welcomeText():
    print("Welcome to Black Jack!")

def getInitialPlayerCards():
    DECK = makeDeck()
    DECK = shuffleDeck(DECK)
    HAND = []
    for i in range(2):
        HAND.append(drawTopCard(DECK))
    return HAND
### --- PROCESSING
def getCardsValue(HAND):
    pass

### --- OUTPUTS
def displayInitialPlayerCards(HAND):
    print("\nPlayer Cards: ")
    displayAllCards(HAND)
    #print(f"Player Cards: {VALUES[HAND[0][1]]} of {SUITS[HAND[0][0]]}")

### --- MAIN PROGRAM CODE --- ###
if __name__ == "__main__":
    welcomeText()
    PLAYER_HAND = getInitialPlayerCards()
    displayInitialPlayerCards(PLAYER_HAND)
    """
    deck = makeDeck()
    deck = shuffleDeck(deck)
    card = drawTopCard(deck)
    displayCard(card)
    """
