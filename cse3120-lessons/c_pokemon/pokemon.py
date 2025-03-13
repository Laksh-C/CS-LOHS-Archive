# pokemon.py in pokemon
"""
title: Pokemon object
author: Laksh Chopra
date-created 22/11/23
"""

import type
import technique

class Pokemon:

    def __init__(self, NAME, TYPES, LEVEL, TECHNIQUES, HEALTH):
        self.__NAME = NAME
        self.__TYPES = TYPES
        self.__LEVEL = LEVEL
        self.__TECHNIQUES = TECHNIQUES
        self.__HEALTH = HEALTH
        self.__EXPERIENCE = 0
        self.__FAINTED = False

    # Modifier Methods
    def addXP(self, POINTS):
        self.__EXPERIENCE = self.__EXPERIENCE + POINTS
        # check for next level

    def takeDamage(self, DAMAGE, TECHNIQUE_TYPE):
        TOTAL_DAMAGE = DAMAGE
        for TYPE in self.__TYPES:
            if TYPE.getSuperEffective(TECHNIQUE_TYPE):
                TOTAL_DAMAGE = 2 * TOTAL_DAMAGE
            elif TYPE.getNotVeryEffective(TECHNIQUE_TYPE):
                TOTAL_DAMAGE = TOTAL_DAMAGE // 2

        self.__HEALTH = self.__HEALTH - TOTAL_DAMAGE
        # check if health reaches 0
        if self.__HEALTH <= 0:
            self.__HEALTH = 0
            self.__FAINTED = True

    def healHealth(self, HEALING):
        self.__HEALTH = self.__HEALTH + HEALING
        # we should also have a max health that the self.__HEALTH does not doesn't exceed


    # Accessor Methods
    def __str__(self):
        return self.__NAME

    def selectTechnique(self):
        """
        The user to select a technique for the pokemon to use
        :return: Technique()
        """
        for i in range(len(self.__TECHNIQUES)):
            print(f"{i+1} {self.__TECHNIQUES[i]} ({self.__TECHNIQUES[i].getRemainingPowerPoints()}/{self.__TECHNIQUES[i].getMaxPowerPoints()})")

        SELECT = int(input("> ")) - 1
        return self.__TECHNIQUES[SELECT]

    def getHealth(self):
        return self.__HEALTH

    def isFainted(self):
        return self.__FAINTED


PIKACHU = Pokemon("Pikachu", [type.ELECTRIC], 3, [technique.THUNDERBOLT, technique.TACKLE], 60)
SQUIRTLE = Pokemon("Squirtle", [type.WATER], 5, [technique.TACKLE, technique.BUBBLE], 80)
CHARMANDER = Pokemon("Charmander", [type.FIRE], 5, [technique.EMBER], 60)

if __name__ == "__main__":
    for i in range(5):
        TECHNIQUE = PIKACHU.selectTechnique()
        print(TECHNIQUE.getDamage())
        PIKACHU.takeDamage(TECHNIQUE.getDamage(), TECHNIQUE.getType())
        print(PIKACHU.getHealth())