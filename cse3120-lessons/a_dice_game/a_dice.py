# a_dice.py in a_dice_game
"""
title: dice class
author: Laksh Chopra
date-created: 10/31/2023
"""

from random import randint

class Die:
    """
    Create a die to roll for random numbers
    """

    def __init__(self, SIDES):
        """
        construct a die
        :param SIDES: int
        """
        self.DIE_MAX = SIDES
        self.DIE_NUMBER = 0

    def rollDie(self):
        """
        updating DIE_NUMBER with a new number
        :return: None
        """
        self.DIE_NUMBER = randint(1, self.DIE_MAX)

    def getDieNumber(self):
        """
        send DIE_NUMBER to the rest of the program
        :return: int
        """
        return self.DIE_NUMBER

if __name__ == "__main__":
    DIE_1 = Die(6)
    DIE_1.rollDie()
    print(DIE_1.getDieNumber())

    DIE_2 = Die(6)
    DIE_2.rollDie()
    print(DIE_2.getDieNumber())

    DICE = []
    for i in range(5):
        DICE.append(Die(6))
    for i in range(len(DICE)):
        DICE[i].rollDie()
        print(DICE[i].getDieNumber())













