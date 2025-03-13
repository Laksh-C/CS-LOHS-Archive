# main.py

'''
Title: Cannon Operator
Author: Laksh Chopra
Date-Created: 09/27/22
'''

### --- LIBRARY IMPORTS --- ###
import math

### --- SUBROUTINES --- ###
### INPUTS
def getChoice():
    """
    Gets which scenario the user wants to do
    :return: CHOICE (int)
    """
    print("""
        Welcome to the Navy cannon distance calculator. 
        Find the total distance the cannonball travels away from the cannon.

        ____
        |   \\
        |    \\
        |     \\
        1. Horizontal to the water. 

           ___
          /   \\
         /     \\
        /       \\
        2. Parabolic to a level boat. 

          ___
         /   \\
        |     \\
        |      \\
                \\
        3. Parabolic to a smaller boat far away.

          ___
         /   \\
        |     \\
        |      
        4. Parabolic to a larger boat far away. 
    """)
    CHOICE = int(input("Please Enter the scenario number: "))
    if CHOICE > 0 and CHOICE < 5:
        return CHOICE
    else:
        return getChoice()

def getSpeed():
    """
    gets the speed of the cannonball from the user
    :return: float
    """
    SPEED = float(input("What is the speed of the cannonball (m/s)? "))
    return SPEED

def getHeight(CHOICE):
    """
    gets the height of the cannonball from the user
    :return: float
    """

    if CHOICE == 1:
        HEIGHT = float(input("What is the height of the cannon above the water (m)? "))
    elif CHOICE == 3:
        HEIGHT = float(input("What is the height of the cannon above the enemy ship (m)? "))
    else:
        HEIGHT = float(input("What is the height of the cannon below the enemy ship (m)? "))
    return HEIGHT

def getAngle():
    """
    gets the angle of the cannonball from the user
    :return: float
    """
    ANGLE = float(input("What is the angle of the cannonball when it leaves the cannon (degrees)? "))
    ANGLE = math.radians(ANGLE)
    return ANGLE

def playAgain():
    '''
    User makes another calculation
    :return: boolean
    '''
    AGAIN = input("Play again? (Y/n): ")
    if AGAIN == "y" or AGAIN == "" or AGAIN == "Y":
        return True
    else:
        return False

### PROCESSING
def calculateScenario1(SPEED, HEIGHT):
    """
    calculates the answer for scenario one and rounds to 2 decimal places
    :param SPEED: float
    :param HEIGHT: float
    :return: double (rounded to 2 decimal places)
    """
    TIME = math.sqrt(2*HEIGHT/9.81)
    DISTANCE = SPEED*TIME
    DISTANCE = round(DISTANCE, 2)
    return DISTANCE

def calculateScenario2(SPEED, ANGLE):
    """
    calculates the answer for scenario two and rounds to 2 decimal places
    :param SPEED: float
    :param ANGLE: float
    :return: double (rounded to 2 decimal places)
    """
    SPEED_HORIZONTAL = SPEED*math.cos(ANGLE)
    SPEED_VERTICAL = SPEED*math.sin(ANGLE)
    TIME = (SPEED_VERTICAL/9.81)*2
    DISTANCE = TIME*SPEED_HORIZONTAL
    DISTANCE = round(DISTANCE, 2)
    return DISTANCE

def calculateScenario3(SPEED, ANGLE, HEIGHT):
    '''
    This function is to calculate the distance the projectile travels in Scenario 3
    :param SPEED: float
    :param ANGLE: float
    :param HEIGHT: float
    :return: double (rounded to 2 decimal places)
    '''
    SPEED_VERTICAL = SPEED*math.sin(ANGLE)
    SPEED_HORIZONTAL = SPEED* math.cos(ANGLE)
    TIME_UP = SPEED_VERTICAL/9.81
    DISTANCE_PEAK = (SPEED_VERTICAL**2)/(2*9.81)
    TOTAL_HEIGHT = DISTANCE_PEAK+HEIGHT
    TIME_DOWN = math.sqrt(2*TOTAL_HEIGHT/9.81)
    TIME_TOTAL = TIME_UP + TIME_DOWN
    DISTANCE = SPEED_HORIZONTAL*TIME_TOTAL
    DISTANCE = round(DISTANCE, 2)
    return DISTANCE

def calculateScenario4(SPEED, ANGLE, HEIGHT):
    '''
    This function is to calculate the distance the projectile travels in Scenario 4
    :param SPEED: float
    :param ANGLE: float
    :param HEIGHT: float
    :return: double (rounded to 2 decimal places)
    '''
    SPEED_VERTICAL = SPEED*math.sin(ANGLE)
    SPEED_HORIZONTAL = SPEED* math.cos(ANGLE)
    TIME_UP = SPEED_VERTICAL/9.81
    DISTANCE_PEAK = (SPEED_VERTICAL**2)/(2*9.81)
    TOTAL_HEIGHT = DISTANCE_PEAK-HEIGHT
    TIME_DOWN = math.sqrt(2*TOTAL_HEIGHT/9.81)
    TIME_TOTAL = TIME_UP + TIME_DOWN
    DISTANCE = SPEED_HORIZONTAL*TIME_TOTAL
    DISTANCE = round(DISTANCE, 2)
    return DISTANCE

### OUTPUTS
def displayAnswer(DISTANCE):
    print(f"The total distance the cannonball travelled is: {DISTANCE}m.")

### --- MAIN PROGRAM CODE --- ###

if __name__ == "__main__":
    while True:
        ### INPUTS
        CHOICE = getChoice()

        if CHOICE == 1:
            SPEED = getSpeed()
            HEIGHT = getHeight(CHOICE)
        elif CHOICE == 2:
            SPEED = getSpeed()
            ANGLE = getAngle()
        elif CHOICE == 3:
            SPEED = getSpeed()
            ANGLE = getAngle()
            HEIGHT = getHeight(CHOICE)
        else:
            SPEED = getSpeed()
            ANGLE = getAngle()
            HEIGHT = getHeight(CHOICE)

        ### PROCESSING
        if CHOICE == 1:
            DISTANCE = calculateScenario1(SPEED, HEIGHT)
        elif CHOICE == 2:
            DISTANCE = calculateScenario2(SPEED, ANGLE)
        elif CHOICE == 3:
            DISTANCE = calculateScenario3(SPEED, ANGLE, HEIGHT)
        else:
            DISTANCE = calculateScenario4(SPEED, ANGLE, HEIGHT)

        ### OUTPUTS:
        displayAnswer(DISTANCE)

        if not playAgain():
            print("\nThank you for using our calculator! Enjoy your day. ")
            exit()
