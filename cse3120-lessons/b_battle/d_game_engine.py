# d_gamg_engine.py in b_battle (folder)
"""
title: Game engine of battle
author: Laksh Chopra
date-created 08/11/2023
"""

from b_deck import Deck
from c_player import Player
from a_card import Card

class Game:
    """
    runs the main program code
    """

    def __init__(self):
        self.__PLAYER1 = Player(input("Player 1 Name: "))
        self.__PLAYER2 = Player(input("Player 2 Name: "))
        self.__DECK = Deck()

    def setup(self):
        self.__DECK.shuffleDeck()
        for i in range(26):
            self.__PLAYER1.takeCard(self.__DECK.drawCard())
            self.__PLAYER2.takeCard(self.__DECK.drawCard())

    def run(self):
        while self.__PLAYER1.isHandEmpty() == False and self.__PLAYER2.isHandEmpty() == False:
            self.__TABLE = []
            self.__TABLE.append(self.__PLAYER1.giveCard())
            self.__TABLE.append(self.__PLAYER2.giveCard())

            print(self.__TABLE)
            print(self.__PLAYER1)
            print("------------")
            print(self.__PLAYER2)
            #print(len(self.__TABLE))
            #print(self.__TABLE[0].getCardValue())
            #print(self.__TABLE[1].getCardValue())

            if self.__TABLE[0].getCardValue() > self.__TABLE[1].getCardValue():
                print(f"{self.__PLAYER1} wins!")
                #for i in range(len(self.__TABLE)):
                self.__PLAYER1.takeCard(self.__TABLE.drawCard())
            else:
                print(f"{self.__PLAYER2} wins!")
                #for i in range(len(self.__TABLE)):
                self.__PLAYER2.takeCard(self.__TABLE.drawCard())




if __name__ == "__main__":
    GAME = Game()
    GAME.setup()
    GAME.run()