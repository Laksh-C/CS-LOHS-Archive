# f_decks_of_cards.py
"""
Title: Deck of Cards Functions
Author: Laksh Chopra
Date-Created: 13/10/22
"""

### --- LIBRARY IMPORTS --- ###
from random import randrange, shuffle
### --- FUNCTIONS --- ###

### --- INPUTS

### --- PROCESSING
def makeDeck():
    """
    Create a 52 card deck
    :return: list (tuples)
    """
    DECK = []
    for i in range(1, 5):
        for j in range(1, 14): # ending value is exclusive
            DECK.append((j, i))
    return DECK

def shuffleDeck(DECK):
    """
    Shuffles the cards in the Deck
    :param DECK: list (tuples --> int)
    :return: DECK
    """
    SHUFFLE_DECK = []
    for i in range(len(DECK)):
        SHUFFLE_DECK.append(DECK.pop(randrange(len(DECK))))
    return SHUFFLE_DECK
    # return shuffle(DECK)

def drawTopCard(DECK):
    """
    Draw the top card from the deck
    :param DECK: list (tuples --> int)
    :return: tuple(int)
    """
    CARD = DECK.pop(0)
    return CARD

### --- OUTPUTS
def displayCard(CARD):
    """
    prints out one card nicely
    :param CARD: tuple (int)
    :return: None
    """
    global VALUES, SUITS
    if CARD[0] in VALUES: # checks if the value is in the key for VALUES:
        print(f"{VALUES[CARD[0]]} of {SUITS[CARD[1]]}")
    else:
        print(f"{CARD[0]} of {SUITS[CARD[1]]}")

### --- VARIABLES --- ###
SUITS = {
        1: "Diamonds",
        2: "Clubs",
        3: "Hearts",
        4: "Spades",
    }

VALUES = {
        1: "Ace",
        11: "Jack",
        12: "Queen",
        13: "King"
    }

def displayAllCards(CARDS):
    """
    Nicely Print all Cards in a list
    :param CARDS: list (tuples --> int)
    :return: None
    """
    global VALUES, SUITS
    DECK_READ = ""
    for CARD in CARDS:
        if CARD[0] in VALUES:
            DECK_READ = DECK_READ + f"{VALUES[CARD[0]]} of {SUITS[CARD[1]]}, "
        else:
            DECK_READ = DECK_READ + f"{CARD[0]} of {SUITS[CARD[1]]}, "
    DECK_READ = DECK_READ[0:-2]
    print(DECK_READ)

### --- MAIN PROGRAM CODE --- ###
if __name__ == "__main__":
    MY_DECK = makeDeck()
    print(MY_DECK)
    MY_DECK = shuffleDeck(MY_DECK)
    print(MY_DECK)
    HAND = []
    HAND.append(drawTopCard(MY_DECK))
    print(HAND)
    displayCard((5, 3))
    displayCard((12, 1))
    # RESET the deck and hands
    MY_DECK = makeDeck()
    MY_DECK = shuffleDeck(MY_DECK)
    HAND = []
    displayAllCards(MY_DECK)