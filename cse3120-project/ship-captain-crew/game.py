# game.py in ship-captain-crew (folder)
"""
title: Game engine for Ship-Captain-Crew Game
author: Laksh Chopra
date-created: 06/12/23
"""
import player
from tabulate import tabulate

class Game:
    def __init__(self, PLAYER1:player.Player, PLAYER2:player.Player):
        """
        Creates the Game Object with two instantiated variables that are Player Objects
        """
        self.__PLAYER1 = PLAYER1
        self.__PLAYER2 = PLAYER2


    def setup(self):
        """
        prints welcome text
        """
        print("Welcome to Ship-Captain-Crew!")

    def run(self):
        # setting up initial variables
        PLAY_AGAIN = True
        # get name inputs for both players
        NAME1 = input("Enter Player 1 Name: ")
        self.__PLAYER1.inputName(NAME1)
        NAME2 = input("Enter Player 2 Name: ")
        self.__PLAYER2.inputName(NAME2)

        # loops for multiple rounds
        while PLAY_AGAIN == True:
            ###############################
            ### --- PLAYER 1'S TURN --- ###
            ###############################

            # displaying the initial roll of Player 1
            print(f"{self.__PLAYER1}'s Turn!")
            self.__PLAYER1.rollHand() #first roll
            print("---FIRST ROLL---")
            self.__PLAYER1.displayRollingHand()

            # series of if/else decisions that depict every possible combination of what can happen in the next 2 rolls.
            if self.__PLAYER1.checkShipFound(self.__PLAYER1.getRollingHand()):
                print("Ship is found!")
                self.__PLAYER1.holdDie(self.__PLAYER1.SHIP_INDEX)
                if self.__PLAYER1.checkCaptainFound(self.__PLAYER1.getRollingHand()):
                    print("Captain is found!")
                    self.__PLAYER1.holdDie(self.__PLAYER1.CAPTAIN_INDEX)
                    if self.__PLAYER1.checkCrewFound(self.__PLAYER1.getRollingHand()):
                        print("Crew is found!")
                        self.__PLAYER1.holdDie(self.__PLAYER1.CREW_INDEX)
                        #break out of loop
                    else:
                        print("HELD DICE:")
                        self.__PLAYER1.displayHeldHand()
                        input("Press enter to roll again:")
                        self.__PLAYER1.rollHand() #second roll
                        self.__PLAYER1.ROLLS_REMAINING = 1
                        print("---SECOND ROLL---")
                        self.__PLAYER1.displayRollingHand()
                        if self.__PLAYER1.checkCrewFound(self.__PLAYER1.getRollingHand()):
                            print("Crew is found!")
                            self.__PLAYER1.holdDie(self.__PLAYER1.CREW_INDEX)
                        else:
                            print("HELD DICE:")
                            self.__PLAYER1.displayHeldHand()
                            input("Press enter to roll again:")
                            self.__PLAYER1.rollHand()  # third roll
                            self.__PLAYER1.ROLLS_REMAINING = 0
                            print("---THIRD ROLL---")
                            self.__PLAYER1.displayRollingHand()
                            if self.__PLAYER1.checkCrewFound(self.__PLAYER1.getRollingHand()):
                                print("Crew is found!")
                                self.__PLAYER1.holdDie(self.__PLAYER1.CREW_INDEX)
                                #break out of loop
                            else:
                                print(f"{self.__PLAYER1} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                                self.__PLAYER1.DISPLAY_SUMMARY_CHECK = False
                else:
                    print("HELD DICE:")
                    self.__PLAYER1.displayHeldHand()
                    input("Press enter to roll again:")
                    self.__PLAYER1.rollHand()  # second roll
                    self.__PLAYER1.ROLLS_REMAINING = 1
                    print("---SECOND ROLL---")
                    self.__PLAYER1.displayRollingHand()
                    if self.__PLAYER1.checkCaptainFound(self.__PLAYER1.getRollingHand()):
                        print("Captain is found!")
                        self.__PLAYER1.holdDie(self.__PLAYER1.CAPTAIN_INDEX)
                        if self.__PLAYER1.checkCrewFound(self.__PLAYER1.getRollingHand()):
                            print("Crew is found!")
                            self.__PLAYER1.holdDie(self.__PLAYER1.CREW_INDEX)
                            # break out of loop
                        else:
                            print("HELD DICE:")
                            self.__PLAYER1.displayHeldHand()
                            input("Press enter to roll again:")
                            self.__PLAYER1.rollHand()  # third roll
                            self.__PLAYER1.ROLLS_REMAINING = 0
                            print("---THIRD ROLL---")
                            self.__PLAYER1.displayRollingHand()
                            if self.__PLAYER1.checkCrewFound(self.__PLAYER1.getRollingHand()):
                                print("Crew is found!")
                                self.__PLAYER1.holdDie(self.__PLAYER1.CREW_INDEX)
                            else:
                                print(f"{self.__PLAYER1} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                                self.__PLAYER1.DISPLAY_SUMMARY_CHECK = False
                    else:
                        print("HELD DICE:")
                        self.__PLAYER1.displayHeldHand()
                        input("Press enter to roll again:")
                        self.__PLAYER1.rollHand()  # third roll
                        self.__PLAYER1.ROLLS_REMAINING = 0
                        print("---THIRD ROLL---")
                        self.__PLAYER1.displayRollingHand()
                        if self.__PLAYER1.checkCaptainFound(self.__PLAYER1.getRollingHand()):
                            print("Captain is found!")
                            self.__PLAYER1.holdDie(self.__PLAYER1.CAPTAIN_INDEX)
                            if self.__PLAYER1.checkCrewFound(self.__PLAYER1.getRollingHand()):
                                print("Crew is found!")
                                self.__PLAYER1.holdDie(self.__PLAYER1.CREW_INDEX)
                                #break out of loop
                            else:
                                print(f"{self.__PLAYER1} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                                self.__PLAYER1.DISPLAY_SUMMARY_CHECK = False
                        else:
                            print(f"{self.__PLAYER1} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                            self.__PLAYER1.DISPLAY_SUMMARY_CHECK = False
            else:
                print("HELD DICE:")
                self.__PLAYER1.displayHeldHand()
                input("Press enter to roll again:")
                self.__PLAYER1.rollHand()  # second roll
                self.__PLAYER1.ROLLS_REMAINING = 1
                print("---SECOND ROLL---")
                self.__PLAYER1.displayRollingHand()
                if self.__PLAYER1.checkShipFound(self.__PLAYER1.getRollingHand()):
                    print("Ship is found!")
                    self.__PLAYER1.holdDie(self.__PLAYER1.SHIP_INDEX)
                    if self.__PLAYER1.checkCaptainFound(self.__PLAYER1.getRollingHand()):
                        print("Captain is found!")
                        self.__PLAYER1.holdDie(self.__PLAYER1.CAPTAIN_INDEX)
                        if self.__PLAYER1.checkCrewFound(self.__PLAYER1.getRollingHand()):
                            print("Crew is found!")
                            self.__PLAYER1.holdDie(self.__PLAYER1.CREW_INDEX)
                            #break out of loop
                        else:
                            print("HELD DICE:")
                            self.__PLAYER1.displayHeldHand()
                            input("Press enter to roll again:")
                            self.__PLAYER1.rollHand()  # third roll
                            self.__PLAYER1.ROLLS_REMAINING = 0
                            print("---THIRD ROLL---")
                            self.__PLAYER1.displayRollingHand()
                            if self.__PLAYER1.checkCrewFound(self.__PLAYER1.getRollingHand()):
                                print("Crew is found!")
                                self.__PLAYER1.holdDie(self.__PLAYER1.CREW_INDEX)
                                #break out of loop
                            else:
                                print(f"{self.__PLAYER1} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                                self.__PLAYER1.DISPLAY_SUMMARY_CHECK = False
                    else:
                        print("HELD DICE:")
                        self.__PLAYER1.displayHeldHand()
                        input("Press enter to roll again:")
                        self.__PLAYER1.rollHand()  # third roll
                        self.__PLAYER1.ROLLS_REMAINING = 0
                        print("---THIRD ROLL---")
                        self.__PLAYER1.displayRollingHand()
                        if self.__PLAYER1.checkCaptainFound(self.__PLAYER1.getRollingHand()):
                            print("Captain is found!")
                            self.__PLAYER1.holdDie(self.__PLAYER1.CAPTAIN_INDEX)
                            if self.__PLAYER1.checkCrewFound(self.__PLAYER1.getRollingHand()):
                                print("Crew is found!")
                                self.__PLAYER1.holdDie(self.__PLAYER1.CREW_INDEX)
                                #break out of loop
                            else:
                                print(f"{self.__PLAYER1} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                                self.__PLAYER1.DISPLAY_SUMMARY_CHECK = False
                        else:
                            print(f"{self.__PLAYER1} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                            self.__PLAYER1.DISPLAY_SUMMARY_CHECK = False
                else:
                    print("HELD DICE:")
                    self.__PLAYER1.displayHeldHand()
                    input("Press enter to roll again:")
                    self.__PLAYER1.rollHand()  # third roll
                    self.__PLAYER1.ROLLS_REMAINING = 0
                    print("---THIRD ROLL---")
                    self.__PLAYER1.displayRollingHand()
                    if self.__PLAYER1.checkShipFound(self.__PLAYER1.getRollingHand()):
                        print("Ship is found!")
                        self.__PLAYER1.holdDie(self.__PLAYER1.SHIP_INDEX)
                        if self.__PLAYER1.checkCaptainFound(self.__PLAYER1.getRollingHand()):
                            print("Captain is found!")
                            self.__PLAYER1.holdDie(self.__PLAYER1.CAPTAIN_INDEX)
                            if self.__PLAYER1.checkCrewFound(self.__PLAYER1.getRollingHand()):
                                print("Crew is found!")
                                self.__PLAYER1.holdDie(self.__PLAYER1.CREW_INDEX)
                                # break out of loop
                            else:
                                print(f"{self.__PLAYER1} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                                self.__PLAYER1.DISPLAY_SUMMARY_CHECK = False
                        else:
                            print(f"{self.__PLAYER1} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                            self.__PLAYER1.DISPLAY_SUMMARY_CHECK = False
                    else:
                        print(f"{self.__PLAYER1} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                        self.__PLAYER1.DISPLAY_SUMMARY_CHECK = False

            # displays a summary for the user if they have gathered all 3 of a Ship Captain and Crew
            if self.__PLAYER1.DISPLAY_SUMMARY_CHECK:
                print("""
    ###################            
    ###---SUMMARY---###
    ###################            
                """)
                print(f"{self.__PLAYER1}'s Held Dice:")
                self.__PLAYER1.displayHeldHand()
                print(f"{self.__PLAYER1}'s Available Dice to Roll:")
                self.__PLAYER1.displayRollingHand()
                print(f"Number of Rolls Remaining: {self.__PLAYER1.ROLLS_REMAINING}.")

            # Calccualtes their Gold
            if len(self.__PLAYER1.getRollingHand()) == 2:
                self.__PLAYER1.countGold()
            print(f"Total Gold Found: {self.__PLAYER1.getGoldCount()}")

            # Asks if they want to roll again for more gold
            if self.__PLAYER1.ROLLS_REMAINING == 0:
                print("You do not have the option to roll for any more gold as you have used up all 3 turns")
            elif self.__PLAYER1.ROLLS_REMAINING == 1:
                print("You currently have one roll remaining, would you like to roll to potentially get more gold?")
                CHOICE = input("(Y/n): ")
                if CHOICE == "Y" or CHOICE == "y":
                    self.__PLAYER1.rollHand()
                    self.__PLAYER1.ROLLS_REMAINING = 0
                    self.__PLAYER1.resetGold()
                    print('Your new roll:')
                    self.__PLAYER1.displayRollingHand()
                    self.__PLAYER1.countGold()
                    print(f"Your Final Gold Count is: {self.__PLAYER1.getGoldCount()}")
                else:
                    print(f"Your Final Gold Count is: {self.__PLAYER1.getGoldCount()}")
            elif self.__PLAYER1.ROLLS_REMAINING == 2:
                print("You currently have Two rolls remaining, would you like to roll to potentially get more gold?")
                CHOICE1 = input("(Y/n): ")
                if CHOICE1 == "Y" or CHOICE1 == "y":
                    self.__PLAYER1.rollHand()
                    self.__PLAYER1.ROLLS_REMAINING = 1
                    self.__PLAYER1.resetGold()
                    print('Your new roll:')
                    self.__PLAYER1.displayRollingHand()
                    self.__PLAYER1.countGold()
                    print(f"Your Current Gold Count is: {self.__PLAYER1.getGoldCount()}")
                    print("You currently have one roll remaining, would you like to roll to potentially get more gold?")
                    CHOICE2 = input("(Y/n): ")
                    if CHOICE2 == "Y" or CHOICE2 == "y":
                        self.__PLAYER1.rollHand()
                        self.__PLAYER1.ROLLS_REMAINING = 1
                        self.__PLAYER1.resetGold()
                        print('Your new roll:')
                        self.__PLAYER1.displayRollingHand()
                        self.__PLAYER1.countGold()
                        print(f"Your Final Gold Count is: {self.__PLAYER1.getGoldCount()}")
                    else:
                        print(f"Your Final Gold Count is: {self.__PLAYER1.getGoldCount()}")
                else:
                    print(f"Your Final Gold Count is: {self.__PLAYER1.getGoldCount()}")
            print(f"###---End of {self.__PLAYER1}'s Turn!---###")
            input(f"Press enter for {self.__PLAYER2}'s Turn")

            ###############################
            ### --- PLAYER 2'S TURN --- ###
            ###############################

            # displaying the initial roll of Player 2
            print(f"{self.__PLAYER2}'s Turn!")
            self.__PLAYER2.rollHand()  # first roll
            print("---FIRST ROLL---")
            self.__PLAYER2.displayRollingHand()

            # series of if/else statements that depict all possible combinations for the next 2 rolls
            if self.__PLAYER2.checkShipFound(self.__PLAYER2.getRollingHand()):
                print("Ship is found!")
                self.__PLAYER2.holdDie(self.__PLAYER2.SHIP_INDEX)
                if self.__PLAYER2.checkCaptainFound(self.__PLAYER2.getRollingHand()):
                    print("Captain is found!")
                    self.__PLAYER2.holdDie(self.__PLAYER2.CAPTAIN_INDEX)
                    if self.__PLAYER2.checkCrewFound(self.__PLAYER2.getRollingHand()):
                        print("Crew is found!")
                        self.__PLAYER2.holdDie(self.__PLAYER2.CREW_INDEX)
                        # break out of loop
                    else:
                        print("HELD DICE:")
                        self.__PLAYER2.displayHeldHand()
                        input("Press enter to roll again:")
                        self.__PLAYER2.rollHand()  # second roll
                        self.__PLAYER2.ROLLS_REMAINING = 1
                        print("---SECOND ROLL---")
                        self.__PLAYER2.displayRollingHand()
                        if self.__PLAYER2.checkCrewFound(self.__PLAYER2.getRollingHand()):
                            print("Crew is found!")
                            self.__PLAYER2.holdDie(self.__PLAYER2.CREW_INDEX)
                        else:
                            print("HELD DICE:")
                            self.__PLAYER2.displayHeldHand()
                            input("Press enter to roll again:")
                            self.__PLAYER2.rollHand()  # third roll
                            self.__PLAYER2.ROLLS_REMAINING = 0
                            print("---THIRD ROLL---")
                            self.__PLAYER2.displayRollingHand()
                            if self.__PLAYER2.checkCrewFound(self.__PLAYER2.getRollingHand()):
                                print("Crew is found!")
                                self.__PLAYER2.holdDie(self.__PLAYER2.CREW_INDEX)
                                # break out of loop
                            else:
                                print(
                                    f"{self.__PLAYER2} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                                self.__PLAYER2.DISPLAY_SUMMARY_CHECK = False
                else:
                    print("HELD DICE:")
                    self.__PLAYER2.displayHeldHand()
                    input("Press enter to roll again:")
                    self.__PLAYER2.rollHand()  # second roll
                    self.__PLAYER2.ROLLS_REMAINING = 1
                    print("---SECOND ROLL---")
                    self.__PLAYER2.displayRollingHand()
                    if self.__PLAYER2.checkCaptainFound(self.__PLAYER2.getRollingHand()):
                        print("Captain is found!")
                        self.__PLAYER2.holdDie(self.__PLAYER2.CAPTAIN_INDEX)
                        if self.__PLAYER2.checkCrewFound(self.__PLAYER2.getRollingHand()):
                            print("Crew is found!")
                            self.__PLAYER2.holdDie(self.__PLAYER2.CREW_INDEX)
                            # break out of loop
                        else:
                            print("HELD DICE:")
                            self.__PLAYER2.displayHeldHand()
                            input("Press enter to roll again:")
                            self.__PLAYER2.rollHand()  # third roll
                            self.__PLAYER2.ROLLS_REMAINING = 0
                            print("---THIRD ROLL---")
                            self.__PLAYER2.displayRollingHand()
                            if self.__PLAYER2.checkCrewFound(self.__PLAYER2.getRollingHand()):
                                print("Crew is found!")
                                self.__PLAYER2.holdDie(self.__PLAYER2.CREW_INDEX)
                            else:
                                print(
                                    f"{self.__PLAYER2} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                                self.__PLAYER2.DISPLAY_SUMMARY_CHECK = False
                    else:
                        print("HELD DICE:")
                        self.__PLAYER2.displayHeldHand()
                        input("Press enter to roll again:")
                        self.__PLAYER2.rollHand()  # third roll
                        self.__PLAYER2.ROLLS_REMAINING = 0
                        print("---THIRD ROLL---")
                        self.__PLAYER2.displayRollingHand()
                        if self.__PLAYER2.checkCaptainFound(self.__PLAYER2.getRollingHand()):
                            print("Captain is found!")
                            self.__PLAYER2.holdDie(self.__PLAYER2.CAPTAIN_INDEX)
                            if self.__PLAYER2.checkCrewFound(self.__PLAYER2.getRollingHand()):
                                print("Crew is found!")
                                self.__PLAYER2.holdDie(self.__PLAYER2.CREW_INDEX)
                                # break out of loop
                            else:
                                print(
                                    f"{self.__PLAYER2} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                                self.__PLAYER2.DISPLAY_SUMMARY_CHECK = False
                        else:
                            print(f"{self.__PLAYER2} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                            self.__PLAYER2.DISPLAY_SUMMARY_CHECK = False
            else:
                print("HELD DICE:")
                self.__PLAYER2.displayHeldHand()
                input("Press enter to roll again:")
                self.__PLAYER2.rollHand()  # second roll
                self.__PLAYER2.ROLLS_REMAINING = 1
                print("---SECOND ROLL---")
                self.__PLAYER2.displayRollingHand()
                if self.__PLAYER2.checkShipFound(self.__PLAYER2.getRollingHand()):
                    print("Ship is found!")
                    self.__PLAYER2.holdDie(self.__PLAYER2.SHIP_INDEX)
                    if self.__PLAYER2.checkCaptainFound(self.__PLAYER2.getRollingHand()):
                        print("Captain is found!")
                        self.__PLAYER2.holdDie(self.__PLAYER2.CAPTAIN_INDEX)
                        if self.__PLAYER2.checkCrewFound(self.__PLAYER2.getRollingHand()):
                            print("Crew is found!")
                            self.__PLAYER2.holdDie(self.__PLAYER2.CREW_INDEX)
                            # break out of loop
                        else:
                            print("HELD DICE:")
                            self.__PLAYER2.displayHeldHand()
                            input("Press enter to roll again:")
                            self.__PLAYER2.rollHand()  # third roll
                            self.__PLAYER2.ROLLS_REMAINING = 0
                            print("---THIRD ROLL---")
                            self.__PLAYER2.displayRollingHand()
                            if self.__PLAYER2.checkCrewFound(self.__PLAYER2.getRollingHand()):
                                print("Crew is found!")
                                self.__PLAYER2.holdDie(self.__PLAYER2.CREW_INDEX)
                                # break out of loop
                            else:
                                print(
                                    f"{self.__PLAYER2} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                                self.__PLAYER2.DISPLAY_SUMMARY_CHECK = False
                    else:
                        print("HELD DICE:")
                        self.__PLAYER2.displayHeldHand()
                        input("Press enter to roll again:")
                        self.__PLAYER2.rollHand()  # third roll
                        self.__PLAYER2.ROLLS_REMAINING = 0
                        print("---THIRD ROLL---")
                        self.__PLAYER2.displayRollingHand()
                        if self.__PLAYER2.checkCaptainFound(self.__PLAYER2.getRollingHand()):
                            print("Captain is found!")
                            self.__PLAYER2.holdDie(self.__PLAYER2.CAPTAIN_INDEX)
                            if self.__PLAYER2.checkCrewFound(self.__PLAYER2.getRollingHand()):
                                print("Crew is found!")
                                self.__PLAYER2.holdDie(self.__PLAYER2.CREW_INDEX)
                                # break out of loop
                            else:
                                print(
                                    f"{self.__PLAYER2} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                                self.__PLAYER2.DISPLAY_SUMMARY_CHECK = False
                        else:
                            print(f"{self.__PLAYER2} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                            self.__PLAYER2.DISPLAY_SUMMARY_CHECK = False
                else:
                    print("HELD DICE:")
                    self.__PLAYER2.displayHeldHand()
                    input("Press enter to roll again:")
                    self.__PLAYER2.rollHand()  # third roll
                    self.__PLAYER2.ROLLS_REMAINING = 0
                    print("---THIRD ROLL---")
                    self.__PLAYER2.displayRollingHand()
                    if self.__PLAYER2.checkShipFound(self.__PLAYER2.getRollingHand()):
                        print("Ship is found!")
                        self.__PLAYER2.holdDie(self.__PLAYER2.SHIP_INDEX)
                        if self.__PLAYER2.checkCaptainFound(self.__PLAYER2.getRollingHand()):
                            print("Captain is found!")
                            self.__PLAYER2.holdDie(self.__PLAYER2.CAPTAIN_INDEX)
                            if self.__PLAYER2.checkCrewFound(self.__PLAYER2.getRollingHand()):
                                print("Crew is found!")
                                self.__PLAYER2.holdDie(self.__PLAYER2.CREW_INDEX)
                                # break out of loop
                            else:
                                print(
                                    f"{self.__PLAYER2} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                                self.__PLAYER2.DISPLAY_SUMMARY_CHECK = False
                        else:
                            print(f"{self.__PLAYER2} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                            self.__PLAYER2.DISPLAY_SUMMARY_CHECK = False
                    else:
                        print(f"{self.__PLAYER2} was unable to roll a Ship, Captain, and Crew in 3 turns :(")
                        self.__PLAYER2.DISPLAY_SUMMARY_CHECK = False

            # if Player 2 was able to get all 3 ship captain and crew it displays them a summary
            if self.__PLAYER2.DISPLAY_SUMMARY_CHECK:
                print("""
    ###################            
    ###---SUMMARY---###
    ###################            
                """)
                print(f"{self.__PLAYER2}'s Held Dice:")
                self.__PLAYER2.displayHeldHand()
                print(f"{self.__PLAYER2}'s Available Dice to Roll:")
                self.__PLAYER2.displayRollingHand()
                print(f"Number of Rolls Remaining: {self.__PLAYER2.ROLLS_REMAINING}.")

            # displays their gold count assuming they gathered all ship captain and crew
            if len(self.__PLAYER2.getRollingHand()) == 2:
                self.__PLAYER2.countGold()
            print(f"Total Gold Found: {self.__PLAYER2.getGoldCount()}")

            # asks them to roll for more gold
            if self.__PLAYER2.ROLLS_REMAINING == 0:
                print("You do not have the option to roll for any more gold as you have used up all 3 turns")
            elif self.__PLAYER2.ROLLS_REMAINING == 1:
                print("You currently have one roll remaining, would you like to roll to potentially get more gold?")
                CHOICE = input("(Y/n): ")
                if CHOICE == "Y" or CHOICE == "y":
                    self.__PLAYER2.rollHand()
                    self.__PLAYER2.ROLLS_REMAINING = 0
                    self.__PLAYER2.resetGold()
                    print('Your new roll:')
                    self.__PLAYER2.displayRollingHand()
                    self.__PLAYER2.countGold()
                    print(f"Your Final Gold Count is: {self.__PLAYER2.getGoldCount()}")
                else:
                    print(f"Your Final Gold Count is: {self.__PLAYER2.getGoldCount()}")
            elif self.__PLAYER2.ROLLS_REMAINING == 2:
                print(
                    "You currently have Two rolls remaining, would you like to roll to potentially get more gold?")
                CHOICE1 = input("(Y/n): ")
                if CHOICE1 == "Y" or CHOICE1 == "y":
                    self.__PLAYER2.rollHand()
                    self.__PLAYER2.ROLLS_REMAINING = 1
                    self.__PLAYER2.resetGold()
                    print('Your new roll:')
                    self.__PLAYER2.displayRollingHand()
                    self.__PLAYER2.countGold()
                    print(f"Your Current Gold Count is: {self.__PLAYER2.getGoldCount()}")
                    print(
                        "You currently have one roll remaining, would you like to roll to potentially get more gold?")
                    CHOICE2 = input("(Y/n): ")
                    if CHOICE2 == "Y" or CHOICE2 == "y":
                        self.__PLAYER2.rollHand()
                        self.__PLAYER2.ROLLS_REMAINING = 1
                        self.__PLAYER2.resetGold()
                        print('Your new roll:')
                        self.__PLAYER2.displayRollingHand()
                        self.__PLAYER2.countGold()
                        print(f"Your Final Gold Count is: {self.__PLAYER2.getGoldCount()}")
                    else:
                        print(f"Your Final Gold Count is: {self.__PLAYER2.getGoldCount()}")
                else:
                    print(f"Your Final Gold Count is: {self.__PLAYER2.getGoldCount()}")
            print(f"###---End of {self.__PLAYER2}'s Turn!---###")

            ### END OF TURNS FOR BOTH PLAYERS###

            # determines the winner/tie between the two Players
            if self.__PLAYER1.getGoldCount() == self.__PLAYER2.getGoldCount():
                print("Both Players had the same amount of gold, it is a tie!")
            elif self.__PLAYER1.getGoldCount() > self.__PLAYER2.getGoldCount():
                print(f"{self.__PLAYER1} has won the round!")
                self.__PLAYER1.updateWinCount()
            else:
                print(f"{self.__PLAYER2} has won the round!")
                self.__PLAYER2.updateWinCount()

            # prints the win count chart in a tabulate table
            print(tabulate([[f"{self.__PLAYER1}'s Win Count", f"{self.__PLAYER2}'s Win Count"],[self.__PLAYER1.getWinCount(), self.__PLAYER2.getWinCount()]], tablefmt="fancy_grid"))

            # asks them to play again, if they do play again it resets all variables, otherwise it exits
            print("Enter 'Y' to play another round, enter 'n' to exit.")
            PLAY_AGAIN_INPUT = input("(Y/n): ")
            if PLAY_AGAIN_INPUT == "Y" or PLAY_AGAIN_INPUT == "y":
                self.__PLAYER1.resetRollingHand()
                self.__PLAYER1.resetHeldHand()
                self.__PLAYER1.resetGold()
                self.__PLAYER1.resetRollCount()
                self.__PLAYER1.DISPLAY_SUMMARY_CHECK = True
                self.__PLAYER2.resetRollingHand()
                self.__PLAYER2.resetHeldHand()
                self.__PLAYER2.resetGold()
                self.__PLAYER2.resetRollCount()
                self.__PLAYER1.DISPLAY_SUMMARY_CHECK = True
            else:
                print("Thank you for playing!")
                exit()

        ### This is logic/brainstorming for the main program code (the series of if/else decisions for the next two rolls
        """
              ### --- LOGIC FOR THE MAIN PROGRAM CODE (BRAINSTORMING) --- ###
              1.1) check if the ship is in the roll
                  - if the ship is in the roll
                      - hold the ship die 
                      2.1) check if the captain is in the roll
                          - if the captain is in the roll
                              - hold the captain die
                              3.1) check if the crew is in the roll
                                  - if the crew is in the roll
                                      - hold the crew die
                                      - break out of all loops (this is still only the INITIAL roll)
                                  - crew not in roll --> roll again --> 2ND ROLL (START LOOKING FROM CREW)
                              3.2) check if the crew is in the roll
                                  - if the crew is in the roll
                                      - hold the crew die
                                      - break out of all loops (this is still only the SECOND roll)
                                  - crew not in roll --> roll again --> 3RD ROLL (START LOOKING FROM CREW)
                              3.3) check if the crew is in the FINAL roll
                                  - if the crew is in the roll
                                      - hold the crew die
                                      - break out of all loops (this is the FINAL roll)
                                  - if the crew is not in the roll
                                      - LOSE
                          - captain not in roll --> roll again --> 2ND ROLL (START LOOKING FROM CAPTAIN)
                      2.2) check if the captain is in the roll
                          - if the captain is in the roll
                              - hold the captain die
                              3.2) check if the crew is in the roll
                                  - if the crew is in the roll
                                      - hold the crew die
                                      - break out of all loops (this is the SECOND roll)
                                  - if the crew is not in the roll
                                  3.3) - roll again
                                          - if the crew is in the roll
                                              - hold crew die
                                              - break out of all loops (this is the final roll)
                                          - if the crew is not in the roll
                                              - LOSE
                          - captain not in roll --> roll again --> 3RD ROLL (START LOOOKING FROM CAPTAIN)
                      2.3) check if the captain is in the FINAL roll
                          - if the captain is in the roll
                              - hold the captain die
                              3.3) check if the crew is in the roll
                                  - if the crew is in the roll 
                                      - hold the crew die
                                      - break out of all loops (THIRD ROLL)
                                  - if the crew is not in the roll
                                      - LOSE
                          - if the captain is not in the roll 
                              - LOSE
                  - ship not in roll --> roll again --> 2ND ROLL (START LOOKING FROM SHIP)
              1.2) check if the ship is in the roll
                  - if the ship is in the roll
                      - hold the ship die 
                      2.2) check if the captain is in the roll
                          - if the captain is in the roll
                              - hold the captain die
                              3.2) check if the crew is in the roll
                                  - if the crew is in the roll
                                      - hold the crew die
                                      - break out of all loops (this is SECOND roll)
                                  - if the crew is not in roll
                              3.3) check if the crew is in the FINAL roll
                                  - if the crew is in this rill
                                      - hold the crew die
                                      - break out of all loops (this is the THIRD roll)
                                  - if the crew is not in this roll
                                      - LOSE
                          - if the captain is not in the roll --> roll again --> THIRD ROLL
                      2.3) check if the captain is in the roll
                          - if the captain is in the roll
                              - hold the captain die
                              3.3) check if the crew is in the roll
                                  - if the crew is in the roll
                                      - hold the crew die
                                      - break out of all loops (this is the THIRD roll)
                                  - if the crew is not in the roll
                                      - LOSE
                          - if the captain is not in the roll
                              - LOSE
                      - if ship not in roll --> roll again --> THIRD AND FINAL ROLL
                  1.3) check if the ship is in the roll
                      - if the ship is in the roll
                          - hold the ship die
                          2.3) check if the captain is in the roll
                              - if the captain is in the roll
                                  - hold the captain die
                                  3.3) check if the crew is in the roll
                                      - if the crew is in the roll
                                          - hold the crew die
                                          - break out of all loops (this is the THIRD ROLL)
                                      - if the crew is not in the roll
                                          - lose
                              - if the captain is not in the roll
                                  - LOSE
                      - if the ship is not in the roll
                          - LOSE 
              """


if __name__ == "__main__":
    GAME = Game(player.PLAYER1, player.PLAYER2)
    GAME.setup()
    GAME.run()



