# player.py in ship-captain-crew (folder)

import dice
from tabulate import tabulate
class Player:
    """
    Creates a player object
    """

    def __init__(self, NAME, HAND):
        """
        Creates the Player Object with two instantiated variables that are a default name as well as a HAND that is a list of 5 Die() Objects
        """
        # Instantiated Variables
        self.__NAME = NAME
        self.__ROLLING_HAND = HAND
        # Other Variables to be referenced Later but not needed for Instantiation
        self.__WIN_COUNT = 0
        self.__GOLD_COUNT = 0
        self.ROLLS_REMAINING = 2
        self.__HELD_HAND = []
        self.SHIP_INDEX = 0
        self.CAPTAIN_INDEX = 0
        self.CREW_INDEX = 0
        self.DISPLAY_SUMMARY_CHECK = True

    ### --- MODIFIER METHODS --- ###
    def rollHand(self):
        """
        Rolls each die within the Rolling hand of the player
        """
        for i in range(len(self.__ROLLING_HAND)):
            self.__ROLLING_HAND[i].rollDie()

    def resetHeldHand(self):
        """
        resets the held hand of the player to an empty list for the next round
        """
        self.__HELD_HAND = []

    def resetRollingHand(self):
        """
        resets the rolling hand of the player to a list of 5 die objects for the next round
        """
        self.__ROLLING_HAND = [dice.Die(), dice.Die(), dice.Die(), dice.Die(), dice.Die()]


    def inputName(self, NAME):
        """
        ovverrides the Player's name with the name that the User inputs
        """
        self.__NAME = NAME

    def updateWinCount(self):
        """
        Adds one win to the Player's Win Count
        """
        self.__WIN_COUNT = self.__WIN_COUNT + 1

    def holdDie(self, DIE_INDEX):
        """
        Pop's the selected die from the user's rolling_hand and appends it to their held hand
        return: self.__ROLLING_HAND: list(Die())
        """
        self.__HELD_HAND.append(self.__ROLLING_HAND[DIE_INDEX])
        self.__ROLLING_HAND.pop(DIE_INDEX)
        return self.__ROLLING_HAND

    def resetGold(self):
        """
        makes the self.__GOLD_COUNT variable equal to zero for the next round
        """
        self.__GOLD_COUNT = 0

    def resetRollCount(self):
        """
        resets the self.ROLLS_REMAINING to 2 rolls for the next round
        """
        self.ROLLS_REMAINING = 2

    ### --- ACCESSOR METHODS --- ###
    def __str__(self):
        """
        when printing the Player, it prints their name
        """
        return f"{self.__NAME}"
    def getRollingHand(self):
        """
        returns the rolling hand of the player
        """
        return self.__ROLLING_HAND

    def displayRollingHand(self):
        """
        formats the rolling hand into a list of 5 integers to be displayed in a tabulate table, it then prints the table
        """
        TABULATE_HAND = []
        for i in range(len(self.__ROLLING_HAND)):
            TABULATE_HAND.append(self.__ROLLING_HAND[i].getDieNumber())
        TABULATE_ROLLING_DATA = [["Die 1", "Die 2", "Die 3", "Die 4", "Die 5"], TABULATE_HAND]
        print(tabulate(TABULATE_ROLLING_DATA, tablefmt='fancy_grid'))

    def displayHeldHand(self):
        """
        formats the held hand into a list of 5 integers to be displayed in a tabulate table, it then prints the table
        """
        TABULATE_HAND = []
        for i in range(len(self.__HELD_HAND)):
            TABULATE_HAND.append(self.__HELD_HAND[i].getDieNumber())
        TABULATE_HELD_DATA = [["Die 1", "Die 2", "Die 3", "Die 4", "Die 5"], TABULATE_HAND]
        print(tabulate(TABULATE_HELD_DATA, tablefmt='fancy_grid'))

    def getWinCount(self):
        """
        returns the WinCount of the Player
        """
        return self.__WIN_COUNT

    def getGoldCount(self):
        """
        returns the Gold_Count of the Player
        """
        return self.__GOLD_COUNT

    def checkShipFound(self, HAND):
        """
        iterates through the rolling hand of the Player to see if any of the dice have rolled a 6 (Ship)
        """
        for i in range(len(HAND)):
            if 6 == HAND[i].getDieNumber():
                self.SHIP_INDEX = i
                return True
        return False

    def checkCaptainFound(self, HAND):
        """
        itereates through the rolling hand of the PLayer to see if any of the dice have rolled a 5 (Captain)
        """
        for i in range(len(HAND)):
            if 5 == HAND[i].getDieNumber():
                self.CAPTAIN_INDEX = i
                return True
        return False

    def checkCrewFound(self, HAND):
        """
        iterates through the rolling hand of the Player to see if any of the dice have rolled a 4 (Crew)
        """
        for i in range(len(HAND)):
            if 4 == HAND[i].getDieNumber():
                self.CREW_INDEX = i
                return True
        return False

    def countGold(self):
        """
        iterates through the rolling hand (which should only have 2 dice in it) and addes their totals together in the self.__GOLD_COUNT variable
        """
        self.__GOLD_COUNT
        for i in range(len(self.__ROLLING_HAND)):
            self.__GOLD_COUNT = self.__GOLD_COUNT + self.__ROLLING_HAND[i].getDieNumber()


# Creating 2 player objects to be referenced and used in the game.py file
PLAYER1 = Player("Player1",[dice.Die(), dice.Die(), dice.Die(), dice.Die(), dice.Die()])
PLAYER2 = Player("Player2", [dice.Die(), dice.Die(), dice.Die(), dice.Die(), dice.Die()])

if __name__ == "__main__":
    #testing
    print(PLAYER1)
    PLAYER1.rollHand()
    PLAYER1.displayRollingHand()
    PLAYER1.displayHeldHand()



