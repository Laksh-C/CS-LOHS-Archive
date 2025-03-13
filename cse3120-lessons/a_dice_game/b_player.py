# b_player.py in a_dice_game
"""
title: Player Class
author: laksh chopra
date-created: 10/31/2023
"""

from a_dice import Die

class Player:
    """
    The player for the game farkle
    """

    def __init__(self):
        self.DICE = [Die(6), Die(6), Die(6), Die(6), Die(6)]
        self.HELD_DICE = []
        self.SCORE = 0

    # --- MODIFIER METHODS (make changes)
    def addScore(self, CALCULATED_POINTS):
        self.SCORE = self.SCORE + CALCULATED_POINTS

    def rollDice(self):
        """
        rolls all dice in DICE
        :return: None
        """
        for die in self.DICE:
            die.rollDie()

    def holdDie(self):
        """
        User selects a die to save
        :return: None
        """
        print("Select a die to hold")
        self.displayDice()
        DIE = int(input("> ")) - 1
        self.HELD_DICE.append(self.DICE.pop(DIE))

        # Ask to hold more dice
        AGAIN = input("Hold More? (y/N): ")
        if AGAIN.upper() == "Y":
            return self.holdDie()

    # --- ACCESSOR METHODS (retrieve data from the object)
    def getScore(self):
        return self.SCORE

    def displayDice(self):
        """
        prints the dice values
        :return: None
        """
        for i in range(len(self.DICE)):
            print(f"Dice {i+1} rolled a {self.DICE[i].getDieNumber()}")

    def displayHeldDice(self):
        """
        print the held dice values
        :return: None
        """
        for i in range(len(self.HELD_DICE)):
            print(f"DICE {i+1} rolled a {self.HELD_DICE[i].getDieNumber()}")

if __name__ == "__main__":
    PLAYER_1 = Player()
    PLAYER_1.rollDice()
    PLAYER_1.holdDie()
    PLAYER_1.displayDice()
    print("Held Dice")
    PLAYER_1.displayHeldDice()
    POINTS = int(input("Score: "))
    PLAYER_1.addScore(POINTS)
    print(f"You have {PLAYER_1.getScore()} points.")
