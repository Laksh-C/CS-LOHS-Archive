# technique.py in pokemon (folder)
"""
title: Techinques that pokemon can use
author: Laksh Chopra
date-created: 22/11/23
"""

import type

class Technique:

    def __init__(self, NAME:str, TYPE:type, DAMAGE:int, POWER_POINTS:int):
        """
        :param NAME: str
        :param TYPE: Type()
        :param DAMAGE: int
        :param POWER_POINTS: int
        """
        self.__NAME = NAME
        self.__TYPE = TYPE
        self.__DAMAGE = DAMAGE
        self.__POWER_POINTS = POWER_POINTS
        self.__POWER_POINTS_USED = 0

    def __str__(self):
        return self.__NAME

    def getDamage(self):
        self.__POWER_POINTS_USED = self.__POWER_POINTS_USED + 1
        return self.__DAMAGE

    def getType(self):
        return self.__TYPE.getName()

    def isAvailable(self):
        if self.__POWER_POINTS_USED <= self.__POWER_POINTS:
            return True
        else:
            return False

    def getMaxPowerPoints(self):
        return self.__POWER_POINTS

    def getRemainingPowerPoints(self):
        return self.__POWER_POINTS - self.__POWER_POINTS_USED

TACKLE = Technique("Tackle", type.NORMAL, 40, 35)
EMBER = Technique("Ember", type.FIRE, 40, 20)
BUBBLE = Technique("Bubble", type.WATER, 40, 35)
THUNDERBOLT = Technique("Thunder Bolt", type.ELECTRIC, 50, 20)

if __name__ == "__main__":

    print(TACKLE.getDamage())
    print(TACKLE.getType())
    print(TACKLE.isAvailable())
    for i in range(35):
        TACKLE.getDamage()
    print(TACKLE.isAvailable())

