# c_player.py in b_battle (folder)
"""
title: Player Class
author: Laksh Chopra
date-created: 08/11/2023
"""

class Player:
    """
    Player class for the game Battler
    """

    def __init__(self, NAME):
        self.__NAME = NAME
        self.__HAND = []

    # --- MODIFIER --- #
    def takeCard(self, CARD):
        """
        adds a card to the hand
        :param CARD: object - Card
        :return:
        """
        self.__HAND.append(CARD)

    def giveCard(self):
        """
        take the top card from the hand
        :return:
        """
        if len(self.__HAND) > 0:
            return self.__HAND.pop(0)

    # ___ ACCESSOR --- #
    def __str__(self):
        return self.__NAME

    def isHandEmpty(self):
        if len(self.__HAND) > 0:
            return False
        else:
            return True

if __name__ == "__main__":
    from b_deck import Deck

    DECK = Deck()
    DECK.shuffleDeck()

    PLAYER1 = Player("Laksh")
    PLAYER2 = Player("Bot")

    for i in range(26):
        PLAYER1.takeCard(DECK.drawCard())
        PLAYER2.takeCard(DECK.drawCard())

    print(PLAYER1.isHandEmpty())

    TABLE = []
    TABLE.append(PLAYER1.giveCard())
    TABLE.append(PLAYER2.giveCard())
    print(TABLE)











