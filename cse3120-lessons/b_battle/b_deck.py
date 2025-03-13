# b_deck.py in b_battle (folder)

"""
title: deck class
author: Laksh Chopra
date-created: 06/11/23
"""

from a_card import Card
from random import shuffle

class Deck:
    """
    Create a deck of 52 playing cards and interact with individual cards
    """

    def __init__(self):
        self.__DECK = []
        for i in range(1, 5):
            for j in range(1, 14):
                self.__DECK.append(Card(i, j))

    # --- MODIFIER --- #
    def shuffleDeck(self):
        """
        shuffles the cards in the deck
        :return:
        """
        shuffle(self.__DECK)

    def drawCard(self):
        """
        return the top card of the deck
        :return:
        """
        if len(self.__DECK) > 0:
            return self.__DECK.pop(0)

    # --- ACCESSOR --- #


if __name__ == "__main__":
    DECK = Deck()
    DECK.shuffleDeck()

    PLAYER_HAND = []
    for i in range(5):
        PLAYER_HAND.append(DECK.drawCard())

    print(PLAYER_HAND)



