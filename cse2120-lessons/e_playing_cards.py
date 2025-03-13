# e_playing_cards.py
"""
Title: Playing Cards
Author: Laksh Chopra
Date-created: 12/10/22
"""

if __name__ == "__main__":
    CARDS = []
    for i in range(4):
        # creating the suits
        CARDS.append([])
        for j in range(13):
            # create the value of each card
            CARDS[i].append(j+1)
    print(CARDS)

    # The main problem of the above structure is that no one structure represents a single card.

    # solution: a data structure must represent a single card.
    CARDS = []
    for i in range(4):
        # suits of the card
        for j in range(13):
            # values for the card
            CARDS.append((i, j+1))

    print(CARDS)

    SUITS = {
        0: "Diamonds",
        1: "Clubs",
        2: "Hearts",
        3: "Spades"
    }

    VALUES = {
        1: "Ace",
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: "Jack",
        12: "Queen",
        13: "King"
    }

    print(CARDS[12])
    print(f"{VALUES[CARDS[12][1]]} of {SUITS[CARDS[12][0]]}")

    ONE_CARD = CARDS[15]
    print(f"{VALUES[ONE_CARD[1]]} of {SUITS[ONE_CARD[0]]}")