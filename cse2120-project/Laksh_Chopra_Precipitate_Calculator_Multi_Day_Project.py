# Laksh_Chopra_Precipitate_Calculator_Multi_Day_Project.py

"""
Title: Precipitate Calculator
Author: Laksh Chopra
Date-Created: 23/10/22
"""

### --- VARIABLES/DATA OF ELEMENTS --- ###
NEGATIVE_ELEMENTS = [
    # (NAME, CHARGE, MOLAR MASS)
    ('NH4', 1, 18.05),
    ('NO3', -1, 63.01),
    ('ClO3', -1, 83.45),
    ('ClO4', -1, 99.45),
    ('CH3COO', -1, 59.05),
    ('F', -1, 19.00),
    ('Cl', -1, 35.45),
    ('Br', -1, 79.90),
    ('I', -1, 126.90),
    ('SO4', -2, 96.07)
]

POSITIVE_ELEMENTS = [
    # (NAME, CHARGE, MOLAR MASS)
    ('Rb', 1, 85.47),
    ('Cs', 1, 132.91),
    ('Ag', 1, 107.87),
    ('Hg2', 2, 401.18),
    ('Li', 1, 6.94),
    ('Mg', 2, 24.31),
    ('Ca', 2, 40.08),
    ('Sr', 2, 87.62),
    ('Ba', 2, 137.33),
    ('Fe', 2, 55.85),
    ('Pb', 2, 207.2),
    ('Cu', 1, 63.55),
    ('Tl', 1, 204.48),
    ('Ra', 2, 226)
]



### --- SUBROUTINES --- ###
### INPUTS
def startScreen():
    """
    Welcome Text for the User
    :return: none
    """
    print("Welcome to the Precipitate Calculator!")
def inputPositiveInfo(LIST):
    """
    User inputs the information for the positive Ion and the program modifies
    the pre-existing (0) values into the charge and molar mass of the ion
    :param LIST: [str, float, float, int, float]
    :return: list
    """
    LIST.insert(0, (input("Please enter the positive reacting ion. (no charges): ")))
    LIST.insert(1, (float(input("What is the volume of the positive solution? (L): "))))
    LIST.insert(2, (float(input("What is the concentration of the positive solution? (mol/L): "))))
    global POSITIVE_ELEMENTS
    for ELEM in range(len(POSITIVE_ELEMENTS)):
        if POSITIVE_ELEMENTS[ELEM][0] == LIST[0]:
            LIST[3] = POSITIVE_ELEMENTS[ELEM][1]
            LIST[4] = POSITIVE_ELEMENTS[ELEM][2]
    return LIST
def inputNegativeInfo(LIST):
    """
    User inputs the information for the Negative Ion and the program modifies
    the pre-existing (0) values into the charge and molar mass of the ion
    :param LIST: [str, float, float, int, float]
    :return: list
    """
    LIST.insert(0, (input("Please enter the negative reacting ion. (no charges): ")))
    LIST.insert(1, (float(input("What is the volume of the negative solution? (L): "))))
    LIST.insert(2, (float(input("What is the concentration of the negative solution? (mol/L): "))))
    global NEGATIVE_ELEMENTS
    for ELEM in range(len(NEGATIVE_ELEMENTS)):
        if NEGATIVE_ELEMENTS[ELEM][0] == LIST[0]:
            LIST[3] = NEGATIVE_ELEMENTS[ELEM][1]
            LIST[4] = NEGATIVE_ELEMENTS[ELEM][2]
    return LIST
def playAgain():
    """
    User makes another calculation
    :return: boolean
    """
    AGAIN = input("Make another calculation? (Y/n): ")
    if AGAIN == "y" or AGAIN == "" or AGAIN == "Y":
        return True
    else:
        return False


### PROCESSING
def calculateIfPrecipitateFormed(POS_LIST, NEG_LIST):
    """
    Checks if the Two given ions will form a precipitate
    :param POS_LIST: list
    :param NEG_LIST: list
    :return: bool (True/False)
    """
    if NEG_LIST[0] == "ClO4":
        if POS_LIST[0] == "Rb" or POS_LIST[0] == "Cs":
            return True
    if NEG_LIST[0] == "CH3COO":
        if POS_LIST[0] == "Ag" or POS_LIST[0] == "Hg2":
            return True
    if NEG_LIST[0] == "F":
        if POS_LIST[0] == "Li" or POS_LIST[0] == "Mg" or POS_LIST[0] == "Ca" or POS_LIST[0] == "Sr" or POS_LIST[0] == "Ba" or POS_LIST[0] == "Fe" or POS_LIST[0] == "Hg2" or POS_LIST[0] == "Pb":
            return True
    if NEG_LIST[0] == "Cl" or NEG_LIST[0] == "Br" or NEG_LIST[0] == "I":
        if POS_LIST[0] == "Cu" or POS_LIST[0] == "Ag" or POS_LIST[0] == "Hg2" or POS_LIST[0] == "Pb" or POS_LIST[0] == "Tl":
            return True
    if NEG_LIST[0] == "SO4":
        if POS_LIST[0] == "Ca" or POS_LIST[0] == "Sr" or POS_LIST[0] == "Ba" or POS_LIST[0] == "Ag" or POS_LIST[0] == "Hg2" or POS_LIST[0] == "Pb" or POS_LIST[0] == "Ra":
            return True
    return False
def calculateMassPositiveReactant(POS_LIST, NEG_LIST):
    """
    Calculates the mass of precipitate formed with the Positive Ion as the limiting reagent
    :param POS_LIST: list
    :param NEG_LIST: list
    :return: float (rounded to 2 decimal places)
    """
    COEFFICIENT = abs(NEG_LIST[3])
    MOLES = POS_LIST[1]*POS_LIST[2]
    MOLES_PRODUCED = MOLES/COEFFICIENT
    MOLAR_MASS_PRODUCT = (POS_LIST[-1]*abs(NEG_LIST[-2])) + (NEG_LIST[-1]*abs(POS_LIST[-2]))
    MASS_PRODUCED = MOLES_PRODUCED*MOLAR_MASS_PRODUCT
    MASS_PRODUCED = round(MASS_PRODUCED, 2)
    return MASS_PRODUCED
def calculateMassNegativeReactant(POS_LIST, NEG_LIST):
    """
    Calculates the mass of precipitate formed with the Negative Ion as the limiting reagent
    :param POS_LIST: list
    :param NEG_LIST: list
    :return: float (rounded to 2 decimal places)
    """
    COEFFICIENT = abs(POS_LIST[3])
    MOLES = NEG_LIST[1]*NEG_LIST[2]
    MOLES_PRODUCED = MOLES/COEFFICIENT
    MOLAR_MASS_PRODUCED = (POS_LIST[-1]*abs(NEG_LIST[-2])) + (NEG_LIST[-1]*abs(POS_LIST[-2]))
    MASS_PRODUCED = MOLES_PRODUCED*MOLAR_MASS_PRODUCED
    MASS_PRODUCED = round(MASS_PRODUCED, 2)
    return MASS_PRODUCED
def compareMasses(POS_MASS, NEG_MASS, POS_LIST, NEG_LIST):
    """
    Compares the two masses and selects one mass as the answer and selects the ion that would produce said mass as the limiting reactant
    :param POS_MASS: float (rounded to two decimal places)
    :param NEG_MASS: float (rounded to two decimal places)
    :return: ANSWER (float 2 decimal places), LIMITING_REAGENT(str)
    """
    if POS_MASS < NEG_MASS:
        LIMITING_REAGENT = POS_LIST[0]
        ANSWER = POS_MASS
    else:
        LIMITING_REAGENT = NEG_LIST[0]
        ANSWER = NEG_MASS
    return LIMITING_REAGENT, ANSWER


### OUTPUTS
def displayLimitingReagent(ANSWERS_LIST):
    """
    Displays the limiting reagent
    :param LIST: list ['limiting_reagnet', mass]
    :return: none
    """
    print(f"The limiting reagent is {ANSWERS_LIST[0]}.")
def displayMassProduced(POS_LIST, NEG_LIST, ANSWERS_LIST):
    """
    Displays the chemical compund and mass of precipitate produced
    :param POS_LIST: list
    :param NEG_LIST: list
    :param ANSWERS_LIST: list ['limiting_reagnet', mass]
    :return:
    """
    if POS_LIST[3] == 1 and abs(NEG_LIST[3]) == 1:
        PRECIPITATE_FORMULA = f"{POS_LIST[0]}{NEG_LIST[0]}"
    elif POS_LIST[3] == 1 and abs(NEG_LIST[3]) == 2:
        PRECIPITATE_FORMULA = f"{POS_LIST[0]}₂{NEG_LIST[0]}"
    elif POS_LIST[3] == 2 and abs(NEG_LIST[3]) == 1:
        PRECIPITATE_FORMULA = f"{POS_LIST[0]}{NEG_LIST[0]}₂"
    else:
        PRECIPITATE_FORMULA = f"{POS_LIST[0]}{abs(NEG_LIST[3])}{NEG_LIST[0]}{POS_LIST[3]}"
    print(f"The mass of {PRECIPITATE_FORMULA} is {ANSWERS_LIST[-1]} grams.")
### --- MAIN PROGRAM CODE --- ###

startScreen()
while True:
    ### VARIABLES (FOR STORING INPUTS)
    # Current format [charge, molar mass]
    POSITIVE_ION_INFO = [0, 0.00]
    NEGATIVE_ION_INFO = [0, 0.00]

    if __name__ == "__main__":
        ### INPUTS
        inputPositiveInfo(POSITIVE_ION_INFO)
        inputNegativeInfo(NEGATIVE_ION_INFO)

        ### PROCESSING
        '''
        I am finding the mass assuming the positive ion is the limiting reactant
        Then finding the mass assuming the negative ion is the limiting reactant
        Then comparing the masses and picking the smallest mass as the correct answer
        '''
        if not calculateIfPrecipitateFormed(POSITIVE_ION_INFO, NEGATIVE_ION_INFO):
            print("The two ions will not create a precipitate.")
            exit()
        else:
            POSITIVE_REACTANT_THEORETICAL_MASS = calculateMassPositiveReactant(POSITIVE_ION_INFO, NEGATIVE_ION_INFO)
            NEGATIVE_REACTANT_THEORETICAL_MASS = calculateMassNegativeReactant(POSITIVE_ION_INFO, NEGATIVE_ION_INFO)
            LIST_OF_REAGENT_AND_ANSWER = compareMasses(POSITIVE_REACTANT_THEORETICAL_MASS, NEGATIVE_REACTANT_THEORETICAL_MASS, POSITIVE_ION_INFO, NEGATIVE_ION_INFO)

        ### OUTPUTS
        displayLimitingReagent(LIST_OF_REAGENT_AND_ANSWER)
        displayMassProduced(POSITIVE_ION_INFO, NEGATIVE_ION_INFO, LIST_OF_REAGENT_AND_ANSWER)
        if not playAgain():
            print("\nThank you for using the Precipitate Calculator! Enjoy your day. ")
            exit()



