# type.py in c_pokemon (folder)
"""
title: element types in Pokemon
author: Laksh Chopra
date-created: 20/11/23
"""

class Type:

    def __init__(self, NAME, SUPER_EFFECTIVE, NOT_VERY_EFFECTIVE):
        self.__NAME = NAME
        self.__SUPER_EFFECTIVE = SUPER_EFFECTIVE
        self.__NOT_VERY_EFFECTIVE = NOT_VERY_EFFECTIVE

    # ACCESSOR METHODS
    def getSuperEffective(self, TYPE):
        """
        Checks if the TYPE is super effective
        :param TYPE: str
        :return: bool
        """
        if TYPE in self.__SUPER_EFFECTIVE:
            return True
        else:
            return False

    def getNotVeryEffective(self, TYPE):
        """
        Checks if the TYPE is not very effective
        :param TYPE: str
        :return: bool
        """
        return TYPE in self.__NOT_VERY_EFFECTIVE

    def getName(self):
        return self.__NAME

FIRE = Type("Fire", ("Grass", "Ice", "Bug", "Steel"), ("Fire", "Water", "Rock", "Dragon"))
WATER = Type("Water", ("Fire", "Ground", "Rock"), ("Water", "Grass", "Dragon"))
GRASS = Type("Grass", ("Water", "Ground", "Rock"), ("Fire", "Grass", "Poison", "Flyer", "Bugs", "Dragon", "Steel"))
ELECTRIC = Type("Electric", ("Water", "Flying"), ("Grass", "Electric", "Ground", "Dragon"))
NORMAL = Type("Normal", (), ("Rock", "Ghost", "Steel"))

if __name__ == "__main__":
    print(FIRE.getSuperEffective(WATER.getName()))
    print(FIRE.getSuperEffective(GRASS.getName()))

    print(FIRE.getNotVeryEffective(WATER.getName()))
    print(FIRE.getNotVeryEffective(GRASS.getName()))