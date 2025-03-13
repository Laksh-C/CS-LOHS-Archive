# game.py in c_pokemon
"""
title: The turn order of the pokemon battle
author: Laksh Chopra
date-created: 24/11/2023
"""

import pokemon


class Game:

    def __init__(self, ACTIVE_POKEMON:pokemon.Pokemon, DEFENDING_POKEMON:pokemon.Pokemon):
        self.__AP = ACTIVE_POKEMON
        self.__DP = DEFENDING_POKEMON

    def run(self):
        while True:
            # --- TURN --- #
            print(f"{self.__AP}'s Trainer choose a technique!")
            ACTIVE_TECHNIQUE = self.__AP.selectTechnique()

            print(f"{self.__DP}'s Trainer choose a technique!")
            DEFENDING_TECHNIQUE = self.__DP.selectTechnique()

            # calculate damage done to defending pokemon
            self.__DP.takeDamage(ACTIVE_TECHNIQUE.getDamage(), ACTIVE_TECHNIQUE.getType())

            # calculate damage done to active pokemon
            if not self.__DP.isFainted():
                self.__AP.takeDamage(DEFENDING_TECHNIQUE.getDamage(), DEFENDING_TECHNIQUE.getType())

            if self.__AP.isFainted():
                print(f"{self.__AP} fainted!")
                print(f"{self.__DP}'s trainer wins!")
                exit()
            else:
                print(f"{self.__AP}'s Health: {self.__AP.getHealth()}")

            if self.__DP.isFainted():
                print(f"{self.__DP} fainted!")
                print(f"{self.__AP}'s trainer wins!")
                exit()
            else:
                print(f"{self.__DP}'s Health: {self.__DP.getHealth()}")

if __name__ == "__main__":
    GAME = Game(pokemon.SQUIRTLE, pokemon.CHARMANDER)
    GAME.run()


