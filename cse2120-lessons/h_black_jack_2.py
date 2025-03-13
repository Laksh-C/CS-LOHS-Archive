# h_black_jack_2.py
"""
Title: Black Jack - Zhang Version
Author: Laksh Chopra
Date-Created 17/10/22
"""

from f_deck_of_cards import *

### --- FUNCTIONS --- ###

### INPUTS
def playerAction():
    """
    Player chooses to draw another card or stay
    :return: int
    """
    global PLAYER_HAND
    displayAllCards(PLAYER_HAND)
    print("""
    1. Hit Me!
    2. Stay
    """)
    CHOICE = int(input("> "))
    if CHOICE < 1 or CHOICE > 2:
        print("Please enter a valid option")
        return playerAction()
    else:
        return CHOICE

### PROCESSING
def gameSetup():
    """
    Shuffles the deck and deals the starting cards to the players
    :return: none
    """
    global DECK, PLAYER_HAND, DEALER_HAND, PLAYER_POINTS, DEALER_POINTS, PLAYER_STAY, DEALER_STAY
    DECK = makeDeck()
    DECK = shuffleDeck(DECK)
    PLAYER_HAND = []
    DEALER_HAND = []
    for i in range(2):
        PLAYER_HAND.append(drawTopCard(DECK))
        DEALER_HAND.append(drawTopCard(DECK))
    PLAYER_POINTS = 0
    DEALER_POINTS = 0
    PLAYER_STAY = False
    DEALER_STAY = False


def calcPoints(HAND):
    """
    Total points for the given hand
    :param HAND: list (tuples) --> int
    :return: int --> total points
    """
    # solve the Ace problem
    POINTS = 0
    ACES = 0
    for card in HAND:
        if card[0] == 1:
            POINTS = POINTS + 11
            ACES = ACES + 1
        elif card[0] > 9:
            POINTS = POINTS + 10
        else:
            POINTS = POINTS + card[0]
    while POINTS > 21 and ACES > 0:
        POINTS = POINTS - 10
        ACES = ACES - 1

    return POINTS

def calcWinner(PLAYER1, PLAYER2):
    """
    Test which player wins
    :param: PLAYER1: int --> Player Points
    :param: PLAYER2: int --> Dealer points
    :return: int --> 0 (no winner), 1 (player 1), 2 (player 2)
    """
    if PLAYER1 < 22 and PLAYER2 > 21:
        return 1
    elif PLAYER1 > 21 and PLAYER2 < 2:
        return 2
    elif PLAYER1 > 21 and PLAYER2 > 21:
        return 0
    elif PLAYER1 == PLAYER2:
        return 0
    elif PLAYER1 > PLAYER2:
        return 1
    else:
        return 2
def resetDeck():
    """
    Resets the deck to starting configuration
    :return:
    """
    pass
### OUTPUTS
def displayAllHands():
    """
    Displays the Dealer's and Player's Cards
    :return: None
    """
    global PLAYER_HAND ,DEALER_HAND
    print("Dealer")
    displayAllCards(DEALER_HAND)
    print("Player")
    displayAllCards(PLAYER_HAND)

### --- VARIABLES --- ###
DECK = []

PLAYER_HAND = []
DEALER_HAND = []

PLAYER_WIN = 0
DEALER_WIN = 0

PLAYER_POINTS = 0
DEALER_POINTS = 0

PLAYER_STAY = False
DEALER_STAY = False


if __name__ == "__main__":
    ### --- MAIN PROGRAM CODE --- ###
    while PLAYER_WIN < 3 and DEALER_WIN < 3:
        gameSetup()
        # player turn
        while not PLAYER_STAY and PLAYER_POINTS < 22:
            ACTION = playerAction()
            if ACTION == 1:
                PLAYER_HAND.append(drawTopCard(DECK))
                PLAYER_POINTS = calcPoints(PLAYER_HAND)
            else:
                PLAYER_STAY = True
            displayAllCards(PLAYER_HAND)
            print(PLAYER_STAY)
        # dealer turn
            while not DEALER_STAY and DEALER_POINTS < 21:
                DEALER_POINTS = calcPoints(DEALER_HAND)
                if DEALER_POINTS < 16:
                    DEALER_HAND.append(drawTopCard(DECK))
                else:
                    DEALER_STAY = True
            displayAllCards(DEALER_HAND)
            # Determine WInner
            WINNER = calcWinner(PLAYER_POINTS, DEALER_POINTS)
            if WINNER == 1:
                PLAYER_WIN = PLAYER_WIN + 1
            else:
                DEALER_WIN = DEALER_WIN + 1

            if WINNER == 1:
                print("Player wins the round.")
            else:
                print("Dealer wins the round.")
    if DEALER_WIN > PLAYER_WIN:
        print("Dealer wins the game")
    else:
        print("Player wins the game")
