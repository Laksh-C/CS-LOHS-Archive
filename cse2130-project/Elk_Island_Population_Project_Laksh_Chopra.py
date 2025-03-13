# Elk_Island_Population_Project_Laksh_Chopra.py

"""
title: Population Finder for Elk Island National Park
author: Laksh Chopra
date-created: Nov 29, 2022
"""

### --- LIBRARY IMPORTS --- ###
import sqlite3
import pathlib

### --- FUNCTIONS --- ###
### INPUTS
def menu():
    """
    Asks the User what they would like to do with the program
    :return: int
    """
    print("""
Please choose an option: 
    
    1. Search Population Growth.
    2. Search Population for a Specific Year.
    3. Add new year data.
    4. Exit.
    """)
    CHOICE = int(input("> "))
    if CHOICE < 1 or CHOICE > 4:
        print("Please choose a value FROM the list. ")
        return menu()
    return int(CHOICE)


def getFileContent(FILENAME):
    """
    Extracts the contents of the file into a 2D array and cleans (removes \n and splits by comma) the data
    :param FILENAME: str
    :return: list -> 2D array
    """
    FILE = open(FILENAME)
    TEXT_LIST = FILE.readlines()
    FILE.close()

    for i in range(len(TEXT_LIST)):
        # Splitting by quotation and comma
        if TEXT_LIST[i][-1] == "\n":
            TEXT_LIST[i] = TEXT_LIST[i][:-1]
        TEXT_LIST[i] = TEXT_LIST[i].split("\"")
        if len(TEXT_LIST[i]) == 1:
            TEXT_LIST[i][0] = TEXT_LIST[i][0].split(",")
        else:
            TEXT_LIST[i][0] = TEXT_LIST[i][0].split(",")
            TEXT_LIST[i][-1] = TEXT_LIST[i][-1][1:]
            TEXT_LIST[i][0].pop()
        #############################################
        '''Fixing the multi dimensional Array issue 
        (Since fixing the quotations and comma created
        a 2d array in each row, I appended the values
        of the 2D array to the second index of each
        row and then popped the first index at the end'''
        if len(TEXT_LIST[i]) == 1:
            for j in range(len(TEXT_LIST[i][0])):
                TEXT_LIST[i].insert(j+1, TEXT_LIST[i][0][j])
                #TEXT_LIST[i].append(TEXT_LIST[i][0][j])
            TEXT_LIST[i].pop(0)
        else:
            for j in range(len(TEXT_LIST[i][0])):
                TEXT_LIST[i].insert(j+1, TEXT_LIST[i][0][j])
            TEXT_LIST[i].pop(0)
        #############################################
        # Correcting None and non-numeric values and making all the species name lowercase
        for j in range(len(TEXT_LIST[i])):
            if TEXT_LIST[i][j].isnumeric():
                TEXT_LIST[i][j] = int(TEXT_LIST[i][j])
            if TEXT_LIST[i][j] == "NA":
                TEXT_LIST[i][j] = 0
    return TEXT_LIST

def getStartYear():
    """
    User enters the starting year for their calculation
    :return: int
    """
    START_YEAR = int(input("Start Year? "))
    return START_YEAR

def getEndYear():
    """
    User enters the end year for their calculation
    :return: int
    """
    END_YEAR = int(input("End Year? "))
    return END_YEAR

def getSpeciesChoice():
    """
    User chooses which species they would like to perform the calculation for
    :return: str
    """
    SPECIES_INPUT = int(input("Bison (1), Elk (2), Moose (3), Deer (4), All (5)? "))

    if SPECIES_INPUT == 1:
        return "Bison"
    elif SPECIES_INPUT == 2:
        return "Elk"
    elif SPECIES_INPUT == 3:
        return "Moose"
    elif SPECIES_INPUT == 4:
        return "Deer"
    elif SPECIES_INPUT == 5:
        return "All"
    elif SPECIES_INPUT < 1 or SPECIES_INPUT > 5:
        print("Please choose an option from the list.")
        return getSpeciesChoice()

def getSingleYear():
    """
    User enters a single year to get population for said year
    :return: int
    """
    SINGLE_YEAR = int(input("Please enter the year for which you would like to find the population: "))

    return SINGLE_YEAR

def getLocation():
    """
    User enters whether they want to search North or South areas of park
    :return: str
    """
    LOCATION = input("Do you want to find the population in the North (N) area or the South (S) area?\nPlease enter 'N' or 'S': ")

    if LOCATION == 'N':
        return "North"
    else:
        return "South"

def getSpeciesSingleYear():
    """
    User enters which species they would like to search the population for in a specific year
    :return:
    """
    SPECIES_INPUT = int(input("Bison (1), Elk (2), Moose (3), Deer (4)? "))

    if SPECIES_INPUT == 1:
        return "Bison"
    elif SPECIES_INPUT == 2:
        return "Elk"
    elif SPECIES_INPUT == 3:
        return "Moose"
    elif SPECIES_INPUT == 4:
        return "Deer"
    elif SPECIES_INPUT < 1 or SPECIES_INPUT > 4:
        print("Please choose an option from the list.")
        return getSpeciesChoice()

def addNewEntry():
    """
    User enters a new row of data
    :return:
    """
    global CURSOR, CONNECTION
    print("\nPlease enter the desired values. Leave blank to skip.\nYOU MUST NOT SKIP THE FIRST 4 ENTRIES AS THEY ARE CRUCIAL TO THE PROGRAM...\n")

    POPULATION_AREA = int(input("* 1. Is this North (1), or South(2)? "))
    if POPULATION_AREA > 2 or POPULATION_AREA < 1:
        print("Please choose a valid option.")
        return addNewEntry()
    elif POPULATION_AREA == 1:
        POPULATION_AREA = "North"
    else:
        POPULATION_AREA = "South"
    POPULATION_YEAR = int(input("* 2. What is the population year? "))
    SPECIES_NAME = int(input("* 3. Bison (1), Elk (2), Moose (3), Deer (4)? "))
    if SPECIES_NAME == 1:
        SPECIES_NAME = "Bison"
    elif SPECIES_NAME == 2:
        SPECIES_NAME = "Elk"
    elif SPECIES_NAME == 3:
        SPECIES_NAME = "Moose"
    else:
        SPECIES_NAME = "Deer"
    FALL_POPULATION_ESTIMATE = int(input("* 4. What is the population Count? "))
    print("""
-----------------------------------------------
Data has been collected for the crucial columns.
-----------------------------------------------
    """)
    SURVEY_YEAR = input("What is the survey year: ")
    SURVEY_MONTH = input("What is the survey month: ")
    SURVEY_DAY = input("What is the survey day: ")
    UNKNOWN_AGE_AND_SEX_COUNT = input("What is the unknown age and sex count: ")
    ADULT_MALE_COUNT = input("What is the adult male count: ")
    ADULT_FEMALE_COUNT = input("What is the adult female count: ")
    ADULT_UNKNOWN_COUNT = input("What is the adult unknown count: ")
    YEARLING_COUNT = input("What is the yearling count: ")
    CALF_COUNT = input("What is the calf count: ")
    SURVEY_TOTAL = input("What is the survey total: ")
    SIGHT_ABILITY_CORRECTION_FACTOR = input("What is the sight ability correction factor: ")
    ADDITIONAL_CAPTIVE_COUNT = input("What is the additional captive count: ")
    ANIMALS_REMOVED_PRIOR_TO_SURVEY = input("What is the count of animals removed prior to survey: ")
    SURVEY_COMMENT = input("Are there any survey comments? ")
    ESTIMATE_METHOD = input("Which method was used to conduct the survey: ")

    NEW_ENTRY = [POPULATION_AREA, POPULATION_YEAR, SURVEY_YEAR, SURVEY_MONTH, SURVEY_DAY, SPECIES_NAME, UNKNOWN_AGE_AND_SEX_COUNT, ADULT_MALE_COUNT, ADULT_FEMALE_COUNT, ADULT_UNKNOWN_COUNT, YEARLING_COUNT, CALF_COUNT, SURVEY_TOTAL, SIGHT_ABILITY_CORRECTION_FACTOR, ADDITIONAL_CAPTIVE_COUNT, ANIMALS_REMOVED_PRIOR_TO_SURVEY, FALL_POPULATION_ESTIMATE, SURVEY_COMMENT, ESTIMATE_METHOD]

    for i in range(len(NEW_ENTRY)):
        if NEW_ENTRY[i] == "":
            NEW_ENTRY[i] = 0

    #NEW_ENTRY = [POPULATION_AREA, POPULATION_YEAR, SPECIES_NAME, FALL_POPULATION_ESTIMATE]

    CURSOR.execute("""
        INSERT INTO
            population_data (
                area_of_park,
                population_year, 
                survey_year, 
                survey_month, 
                survey_day, 
                species_name, 
                unknown_age_and_sex_count, 
                adult_male_count, 
                adult_female_count, 
                adult_unknown_count, 
                yearling_count, 
                calf_count,
                survey_total, 
                sight_ability_correction_factor,
                additional_captive_count, 
                animals_removed_prior_to_survey, 
                fall_population_estimate, 
                survey_comment, 
                estimate_method
            )
        VALUES (
            ?,
            ?,
            ?,
            ?, 
            ?, 
            ?,
            ?,
            ?,
            ?, 
            ?, 
            ?,
            ?,
            ?,
            ?, 
            ?, 
            ?,
            ?,
            ?,
            ?
        )
    ;""", NEW_ENTRY)

    CONNECTION.commit()

### PROCESSING
def setupPopulationTable(LIST):
    """
    CREATES a Table within the database
    :param LIST: list of large mammal data
    :return: none
    """
    global CONNECTION, CURSOR

    # Creates table and it's columns
    CURSOR.execute("""
        CREATE TABLE
            population_data (
                area_of_park TEXT NOT NULL,
                population_year INTEGER NOT NULL, 
                survey_year INTEGER, 
                survey_month INTEGER, 
                survey_day INTEGER, 
                species_name TEXT NOT NULL, 
                unknown_age_and_sex_count INTEGER, 
                adult_male_count INTEGER, 
                adult_female_count INTEGER, 
                adult_unknown_count INTEGER, 
                yearling_count INTEGER, 
                calf_count INTEGER,
                survey_total INTEGER, 
                sight_ability_correction_factor INTEGER,
                additional_captive_count INTEGER, 
                animals_removed_prior_to_survey INTEGER, 
                fall_population_estimate INTEGER NOT NULL, 
                survey_comment TEXT, 
                estimate_method TEXT
            )
    ;""")


    # iterates through each element in 2D array and adds it to the table
    for i in range(len(LIST)):
        CURSOR.execute("""
            INSERT INTO
                population_data
            VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
        ;""", LIST[i])

    CONNECTION.commit()

def getSpeciesPopulation(AREA, YEAR, SPECIES):
    """
    Queries the database to return the count of the population given the Area, Year, and Species Name
    :param AREA: str
    :param YEAR: int
    :param SPECIES: str
    :return:
    """
    global CURSOR
    SPECIES = f"%{SPECIES[1:]}"
    INPUT_INFO = [AREA, YEAR, SPECIES]

    POPULATION_COUNT = CURSOR.execute("""
        SELECT
            fall_population_estimate
        FROM
            population_data
        WHERE
            area_of_park = ?
        AND
            population_year = ?
        AND 
            species_name LIKE ?
    ;""", INPUT_INFO).fetchone()

    if POPULATION_COUNT == None:
        POPULATION_COUNT = (0, 0)

    return int(POPULATION_COUNT[0])

def searchSingleYear(SINGLE_YEAR, SPECIES_NAME, LOCATION):
    """
    Queries the database to find population for a specific year
    :param SINGLE_YEAR:
    :return: int
    """
    global CURSOR
    SPECIES_NAME = f"%{SPECIES_NAME[1:]}"

    SEARCH_PARAMETERS = [SINGLE_YEAR, SPECIES_NAME, LOCATION]

    POPULATION = CURSOR.execute("""
        SELECT
            fall_population_estimate
        FROM
            population_data
        WHERE
            population_year = ?
        AND
            species_name LIKE ?
        AND
            area_of_park = ?
    ;""", SEARCH_PARAMETERS).fetchone()

    if POPULATION == None:
        return "Information not found in database."
    else:
        return POPULATION[0]

def calculateGrowth(START_NORTH, START_SOUTH, END_NORTH, END_SOUTH, START_YEAR, END_YEAR):
    """
    Calculates the net population change for a specific species
    :param START_NORTH: int
    :param START_SOUTH: int
    :param END_NORTH: int
    :param END_SOUTH: int
    :param START_YEAR: int
    :param END_YEAR: int
    :return: int
    """
    NET_POPULATION_CHANGE = (END_NORTH + END_SOUTH) - (START_NORTH + START_SOUTH)
    NET_YEAR_DIFFERENCE = (END_YEAR - START_YEAR)

    GROWTH = NET_POPULATION_CHANGE/NET_YEAR_DIFFERENCE

    return int(GROWTH)

def calculateAllGrowth(GROWTH_BISON, GROWTH_ELK, GROWTH_MOOSE, GROWTH_DEER):
    """
    Calculates the net population change for all species
    :param GROWTH_BISON: int
    :param GROWTH_ELK: int
    :param GROWTH_MOOSE: int
    :param GROWTH_DEER: int
    :return: int
    """

    NET_ALL_POPULATION_CHANGE = (GROWTH_BISON + GROWTH_ELK + GROWTH_MOOSE + GROWTH_DEER)/4

    return int(NET_ALL_POPULATION_CHANGE)

### OUTPUTS
def displayGrowth(GROWTH, START_YEAR, END_YEAR, SPECIES_NAME):
    """
    Displays the Growth Nicely
    :param GROWTH: int
    :return: none
    """
    if SPECIES_NAME == "All":
        print(f"The growth rate of {SPECIES_NAME} large mammals between {START_YEAR} and {END_YEAR} is {GROWTH} Animals/year.")
    else:
        print(f"The growth rate of {SPECIES_NAME} between {START_YEAR} and {END_YEAR} is {GROWTH} {SPECIES_NAME}/year.")

def displaySingleYearPopulation(POPULATION, YEAR, SPECIES, LOCATION):
    """
    Displays the population for a specific year nicely
    :param POPULATION: int
    :param YEAR: int
    :param SPECIES: str
    :param LOCATION: str
    :return: none
    """
    if POPULATION == 'Information not found in database.':
        print(POPULATION)
    else:
        print(f"The population for {SPECIES} in the year {YEAR} in the {LOCATION}ern area of the park is: {POPULATION}")
def displayWelcomeText():
    """
    Prints a welcome text for the user
    :return: none
    """
    print("Welcome to the Elk Island National Park Large Mammal population database!")

### --- VARIABLES --- ###
DATABASE_FILE = "population_data.db"
FIRST_RUN = True

if (pathlib.Path.cwd() / DATABASE_FILE).exists():
    FIRST_RUN = False

CONNECTION = sqlite3.connect(DATABASE_FILE)
CURSOR = CONNECTION.cursor()

if __name__ == "__main__":
    ### --- MAIN PROGRAM CODE --- ###
    ### INPUTS
    if FIRST_RUN:
        CONTENT = getFileContent("Elk_Island_NP_Grassland_Forest_Ungulate_Population_1906-2017_data_reg.csv")
        setupPopulationTable(CONTENT)

    displayWelcomeText()

    while True:
        CHOICE = menu()
        if CHOICE == 1:
            START_YEAR = getStartYear()
            END_YEAR = getEndYear()
            SPECIES_CHOICE = getSpeciesChoice()
        elif CHOICE == 2:
                SINGLE_YEAR = getSingleYear()
                SPECIES_CHOICE = getSpeciesSingleYear()
                LOCATION = getLocation()
        elif CHOICE == 3:
            addNewEntry()
        else:
            print("Thank you for using the database!")
            exit()
    ### PROCESSING
        if CHOICE == 1:
            START_NORTH_POPULATION = getSpeciesPopulation('North', START_YEAR, SPECIES_CHOICE)
            START_SOUTH_POPULATION = getSpeciesPopulation('South', START_YEAR, SPECIES_CHOICE)
            END_NORTH_POPULATION = getSpeciesPopulation('North', END_YEAR, SPECIES_CHOICE)
            END_SOUTH_POPULATION = getSpeciesPopulation('South', END_YEAR, SPECIES_CHOICE)
            GROWTH = calculateGrowth(START_NORTH_POPULATION, START_SOUTH_POPULATION, END_NORTH_POPULATION, END_SOUTH_POPULATION, START_YEAR, END_YEAR)

            if SPECIES_CHOICE == "All":
                # Calculating End Net Growth
                END_BISON_NORTH = searchSingleYear(END_YEAR, "Bison", "North")
                END_ELK_NORTH = searchSingleYear(END_YEAR, "Elk", "North")
                END_MOOSE_NORTH = searchSingleYear(END_YEAR, "Moose", "North")
                END_DEER_NORTH = searchSingleYear(END_YEAR, "Deer", "North")
                END_BISON_SOUTH = searchSingleYear(END_YEAR, "Bison", "South")
                END_ELK_SOUTH = searchSingleYear(END_YEAR, "Elk", "South")
                END_MOOSE_SOUTH = searchSingleYear(END_YEAR, "Moose", "South")
                END_DEER_SOUTH = searchSingleYear(END_YEAR, "Deer", "South")
                ALL_NET_END = [END_BISON_NORTH, END_ELK_NORTH, END_MOOSE_NORTH, END_DEER_NORTH, END_BISON_SOUTH, END_ELK_SOUTH, END_MOOSE_SOUTH, END_DEER_SOUTH]
                # Cleaning up null values
                for i in range(len(ALL_NET_END)):
                    if ALL_NET_END[i] == "Information not found in database.":
                        ALL_NET_END[i] = 0
                ALL_NET_END = int(sum(ALL_NET_END))


                # Calculating Start Net Growth
                START_BISON_NORTH = searchSingleYear(START_YEAR, "Bison", "North")
                START_ELK_NORTH = searchSingleYear(START_YEAR, "Elk", "North")
                START_MOOSE_NORTH = searchSingleYear(START_YEAR, "Moose", "North")
                START_DEER_NORTH = searchSingleYear(START_YEAR, "Deer", "North")
                START_BISON_SOUTH = searchSingleYear(START_YEAR, "Bison", "South")
                START_ELK_SOUTH = searchSingleYear(START_YEAR, "Elk", "South")
                START_MOOSE_SOUTH = searchSingleYear(START_YEAR, "Moose", "South")
                START_DEER_SOUTH = searchSingleYear(START_YEAR, "Deer", "South")
                ALL_NET_START = [START_BISON_NORTH, START_ELK_NORTH, START_MOOSE_NORTH, START_DEER_NORTH, START_BISON_SOUTH, START_ELK_SOUTH, START_MOOSE_SOUTH, START_DEER_SOUTH]
                # Cleaning up null values
                for i in range(len(ALL_NET_START)):
                    if ALL_NET_START[i] == "Information not found in database.":
                        ALL_NET_START[i] = 0
                ALL_NET_START = int(sum(ALL_NET_START))

                # Calculate Difference in Growth for All
                ALL_GROWTH = int((ALL_NET_END-ALL_NET_START)/(END_YEAR-START_YEAR))
        elif CHOICE == 2:
            SINGLE_YEAR_POPULATION = searchSingleYear(SINGLE_YEAR, SPECIES_CHOICE, LOCATION)

    ### OUTPUTS
        if CHOICE == 1 and SPECIES_CHOICE == "All":
            displayGrowth(ALL_GROWTH, START_YEAR, END_YEAR, SPECIES_CHOICE)
        elif CHOICE == 1:
            displayGrowth(GROWTH, START_YEAR, END_YEAR, SPECIES_CHOICE)
        elif CHOICE == 2:
            displaySingleYearPopulation(SINGLE_YEAR_POPULATION, SINGLE_YEAR, SPECIES_CHOICE, LOCATION)
        elif CHOICE == 3:
            print("Data successfully inputted!")


