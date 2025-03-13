# b_high_score.py

"""
title: High Score Tracker
Author: Laksh Chopra
Date-created: 01/11/22
"""

### --- VARIABLES --- ###
FILENAME = "b_score.txt"

### --- SUBROUTINES --- ###
### INPUTS
def getFile():
    """
    Check if the save file exists and creates a default file if it doesn't
    :return: Object --> return the file as read-only
    """
    global FILENAME
    try:
        FILE = open(FILENAME, "x")
        # Create default scores
        START_SCORE = []
        for i in range(10):
            START_SCORE.append("AAA 0")
        TEXT = ','.join(START_SCORE)
        FILE.write(TEXT)
        FILE.close()
        # open file as read-only
        FILE = open(FILENAME)
        return FILE
    except FileExistsError:
        FILE = open(FILENAME)
        return FILE

def readFile(FILE_OBJ):
    """
    Reads and processes the file data into an array
    :param FILE_OBJ: object
    :return: list --> str
    """
    TEXT = FILE_OBJ.read()
    SCORE_ARRAY = TEXT.split(",")
    FILE_OBJ.close()
    return SCORE_ARRAY

def menu():
    """
    User selects whether to view or add new scores
    :return: int
    """
    print("""
    1. View High Scores
    2. Add High Score
    3. Exit
    """)
    CHOICE = int(input("> "))
    return CHOICE

def askNewScore():
    """
    asks users for a new high score
    :return: int
    """
    SCORE = input("What is the new score? ")
    try:
        SCORE = int(SCORE)
        return SCORE
    except ValueError:
        print("Enter a valid number!")
        return askNewScore()

def askName():
    """
    User inputs name to be saved
    :return: str
    """
    NAME = input("What is your name? ")
    NAME = NAME.upper()
    if len(NAME) > 3:
        NAME = NAME[:3]
    return NAME

### PROCESSING
def checkNewScore(NEW_SCORE, SCORE_LIST):
    """
    Compare the NEW_SCORE to all scores in the Array to see if it is higher.
    :param NEW_SCORE: int
    :param SCORE_LIST: list --> Str
    :return: bool
    """
    # Manipulate the data in SCORE_LIST
    SCORE_LIST_2D = []
    for i in range(len(SCORE_LIST)):
        SCORE_LIST_2D.append(SCORE_LIST[i].split())
        SCORE_LIST_2D[-1][1] = int(SCORE_LIST_2D[-1][1])
    # Compare NEW_SCORE to high scores
    for i in range(len(SCORE_LIST_2D)):
        if NEW_SCORE >= SCORE_LIST_2D[i][1]:
            return True
    return False

def updateHighScore(NEW_SCORE, NEW_NAME, SCORE_ARRAY):
    """
    Insert the new score into the appropriate spot and remove the lowest value
    :param NEW_SCORE: int
    :param NEW_NAME: str
    :param SCORE_ARRAY: list --> str
    :return: list --> str
    """
    SCORE_ARRAY_2D = []
    for i in range(len(SCORE_ARRAY)):
        SCORE_ARRAY_2D.append(SCORE_ARRAY[i].split())
        SCORE_ARRAY_2D[-1][1] = int(SCORE_ARRAY_2D[-1][1])

    # searching for i position to insert score
    for i in range(len(SCORE_ARRAY_2D)):
        if NEW_SCORE >= SCORE_ARRAY_2D[i][1]:
            SCORE_ARRAY.insert(i, NEW_NAME + " " + str(NEW_SCORE))
            SCORE_ARRAY.pop()
            break
    return SCORE_ARRAY
"""
    for i in range(len(SCORE_ARRAY_2D)):
        if NEW_SCORE >= SCORE_ARRAY_2D[i][1]:
            SCORE_ARRAY.insert(i, NEW_NAME + " " + str(NEW_SCORE))
            SCORE_ARRAY.pop()
            return SCORE_ARRAY
"""
### OUTPUTS
def viewScores(SCORE_LIST):
    """
    Displays all scores
    :param SCORE_LIST: list --> str
    :return: none
    """
    print("HIGH SCORES!")
    for i in range(len(SCORE_LIST)):
        print(f"{i+1}. {SCORE_LIST[i]}")

def saveNewScores(SCORE_ARRAY):
    """
    Save the array into the file
    :param SCORE_ARRAY: list --> str
    :return: none
    """
    global FILENAME
    FILE = open(FILENAME, "w")
    TEXT = ",".join(SCORE_ARRAY)
    FILE.write(TEXT)
    FILE.close()


if __name__ == "__main__":
    ### --- MAIN PROGRAM CODE --- ###
    ### INPUTS
    FILE_R = getFile()
    SCORES = readFile(FILE_R)

    while True:
        CHOICE = menu()
        ### PROCESSING
        if CHOICE == 1:
            viewScores(SCORES)
        elif CHOICE == 2:
            NEW_SCORE = askNewScore()
            if checkNewScore(NEW_SCORE, SCORES):
                print("High Score Found!")
                NAME = askName()
                SCORES = updateHighScore(NEW_SCORE, NAME, SCORES)
                # print(SCORES)
            else:
                print("Better luck next time!")
        else:
            saveNewScores(SCORES)
            exit()