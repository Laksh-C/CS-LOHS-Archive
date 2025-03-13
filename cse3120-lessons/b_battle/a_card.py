# a_card.py in b_battle (folder)

"""
title: card class
author: Laksh Chopra
date-created: 06/11/23
"""

class Card:
    """
    Single playing card
    """

    SUITS = {
        1: "Diamonds",
        2: "Clubs",
        3: "Hearts",
        4: "Spades"
    }

    FACES = {
        1: "Ace",
        11: "Jack",
        12: "Queen",
        13: "King"
    }

    def __init__(self, SUIT, VALUE):
        """
        Constructs a Card
        :param SUIT:
        :param VALUE:
        """
        self.__SUIT = SUIT
        self.__VALUE = VALUE

    # --- MODIFIER --- #

    # --- ACCESSOR --- #
    def getCardValue(self):
        return self.__VALUE

    def getCardSuit(self):
        return self.__SUIT

    def __str__(self):
        if self.__VALUE > 1 and self.__VALUE < 11:
            return f"{self.__VALUE} of {Card.SUITS[self.__SUIT]}"
        else:
            return f"{Card.FACES[self.__VALUE]} of {Card.SUITS[self.__SUIT]}"

    def __repr__ (self):
        return f"<--{self.__str__()}--->"


if __name__ == "__main__":
    CARD = Card(1, 12)
    print(CARD)
    print(CARD.getCardValue(), CARD.getCardSuit())

    DECK = []
    for i in range(1, 5):
        for j in range(1, 14):
            DECK.append(Card(i, j))
    print(DECK[0].getCardValue())
    print(DECK)