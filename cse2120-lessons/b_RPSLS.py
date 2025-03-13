# b_RPSLS.py

"""
title: Rock Paper Scissors Lizard Spock
author: Laksh Chopra
date-created: 05/10/22
"""

### --- LIBRARY IMPORTS --- ###
from random import randint

### --- INPUTS --- ###
def checkInt(NUM):
    '''
    Validate whether the string is an integer
    :param NUM: (str) number
    :return: (int) number
    '''
    if NUM.isnumeric():
        return int(NUM)
    else:
        print("Please enter a valid number. ")
        NEW_NUM = input("> ")
        return checkInt(NEW_NUM)
def menu():
    '''
    Displays users selection and user chooses their weapon
    :return: (int) menu item (weapon)
    '''
    global WEAPONS
    print(f"1: {WEAPONS[0]}")
    print(f"2: {WEAPONS[1]}")
    print(f"3: {WEAPONS[2]}")
    print(f"4: {WEAPONS[3]}")
    print(f"5: {WEAPONS[4]}")
    WEAPON = input("> ")
    WEAPON = checkInt(WEAPON)
    if WEAPON > 0 and WEAPON < 6:
        WEAPON = WEAPON - 1
        return WEAPON
    else:
        print("Please choose a valid option from the list. ")
        return menu()

def playAgain():
    '''
    User plays another round
    :return: (bool)
    '''
    AGAIN = input("Play again? (Y/n): ")
    if AGAIN == "N" or AGAIN == "n":
        return False
    else:
        return True

### --- PROCESSING --- ###
def computerChoice():
    '''
    Computer chooses a weapon
    :return: (int) weapon
    '''
    WEAPON = randint(0, 5)
    return WEAPON

def getWinner(PLAYER, COMPUTER, WEAPONS):
    '''
    Determine the winner of the round
    :param PLAYER: (int) Players weapon
    :param COMPUTER: (int) Computers weapon
    :return: (int) Winner of the round (0 = TIE; 1 = PLAYER; 2 = COMPUTER)
    '''
    if PLAYER == COMPUTER:
        return 0
    elif WEAPONS[COMPUTER] == WEAPONS[PLAYER - 1] or WEAPONS[COMPUTER]  == WEAPONS[PLAYER - 3]:
        return 2
    else:
        return 1

### --- OUTPUTS --- ###
def displayWinner(WINNER):
    '''
    Display the winner of the round
    :param WINNER: (int) Winner
    :return: (none)
    '''
    if WINNER == 0:
        print("You and the computer tied!")
    elif WINNER == 1:
        print("You Won!")
    else:
        print("The computer won...")

### --- MAIN PROGRAM CODE --- ###

if __name__ == "__main__":
    while True:
        ### --- INPUTS --- ###
        WEAPONS = ("Rock", "Paper", "Scissors", "Lizard", "Spock")
        USER = menu()
        COMP = computerChoice()
        
        ### --- PROCESSING --- ###
        WINNER = getWinner(USER, COMP, WEAPONS)

        ### --- OUTPUTS --- ###
        displayWinner(WINNER)

        if not playAgain():
            exit()
