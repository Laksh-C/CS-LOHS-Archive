# c_game_engine.py
"""
title: The game engine for Farkle
author: Laksh Chopra
date-created 02/11/2023
"""

from b_player import Player

class Game:
    """
    Game class that has the rules of the game.
    """

    def __init__(self):
        self.PLAYER1 = Player()
        self.PLAYER2 = Player()

    def setup(self):
        print("Welcome to oversimplified Farkle")

    def run(self):
        """
        Where the majority of the game will happen. This section often loops
        :return:
        """
        while self.PLAYER1.getScore() < 10000 and self.PLAYER2.getScore() < 10000:
            # --- PLAYER 1 TURN --- #
            print("Player 1 Turn!")
            ROLL = 0
            while ROLL < 3 and len(self.PLAYER1.DICE) > 0:
                print(f"Roll {ROLL + 1}")
                self.PLAYER1.rollDice()
                self.PLAYER1.holdDie()
                ROLL = ROLL + 1
            print("Dice to Score")
            self.PLAYER1.displayHeldDice()
            TEMP_POINT = int(input("Player 1 Points: "))
            self.PLAYER1.addScore(TEMP_POINT)
            print(f"Player 1 has {self.PLAYER1.getScore()} points!")

            # --- PLAYER 2 TURN --- #
            print("Player 2 Turn!")
            ROLL = 0
            while ROLL < 3 and len(self.PLAYER2.DICE) > 0:
                print(f"Roll {ROLL + 1}")
                self.PLAYER2.rollDice()
                self.PLAYER2.holdDie()
                ROLL = ROLL + 1
            print("Dice to Score")
            self.PLAYER2.displayHeldDice()
            TEMP_POINT = int(input("Player 2 Points: "))
            self.PLAYER2.addScore(TEMP_POINT)
            print(f"Player 2 has {self.PLAYER2.getScore()} points!")
        if self.PLAYER1.getScore() > self.PLAYER2.getScore():
            print("Player 1 Wins")
        else:
            print("Player 2 Wins")

if __name__ == "__main__":
    GAME = Game()
    GAME.setup()
    GAME.run()

















