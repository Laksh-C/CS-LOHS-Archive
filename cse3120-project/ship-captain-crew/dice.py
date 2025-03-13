# dice.py in ship-captain-crew (folder)
"""
title: class for the Die object
author: Laksh Chopra
date-created: 04/12/23
"""

from random import randint

class Die:
    """
    Create a 6 sided die
    """
    def __init__(self):
        """
        Construct a die
        :return: None
        """
        self.__DIE_NUMBER = 0

    ###--- MODIFIER METHODS ---###
    def rollDie(self):
        """
        Updates the DIE_NUMBER with a new number
        :return: None
        """
        self.__DIE_NUMBER = randint(1, 6)

    ###--- ACCESSOR METHODS ---###
    def __repr__(self):
        return f"{self.__DIE_NUMBER}"

    def getDieNumber(self):
        """
        send DIE_NUMBER to the rest of the program
        :return: int
        """
        return self.__DIE_NUMBER


if __name__ == "__main__":
    #Testing to see if the Die object can be successfully created
    DIE = Die()
    DIE.rollDie()
    print(DIE.getDieNumber())

    DICE = []
    for i in range(5):
        DICE.append(Die())
    for i in range(len(DICE)):
        DICE[i].rollDie()
        print(DICE[i].getDieNumber())

    print(type(DICE[1]))
    DICE2 = [DIE.getDieNumber()]
    print("hello", DICE2)
    print(type(DICE2[0]))

    print(DICE)