# f_typechecker.py

"""
title: Pokemon Type Checker
author: Laksh Chopra
date-created: Nov 21, 2022
"""

### --- LIBRARY IMPORTS --- ###
import pathlib
import sqlite3

### --- FUNCTIONS --- ###

### INPUTS
def getFileContent(FILENAME):
    """
    Extracts the contents of the file into a 2D array
    :param FILENAME: str
    :return: list -> 2D array
    """
    FILE = open(FILENAME)
    TEXT_LIST = FILE.readlines()
    FILE.close()
    for i in range(len(TEXT_LIST)):
        if TEXT_LIST[i][-1] == "\n":
            TEXT_LIST[i] = TEXT_LIST[i][:-1]
        TEXT_LIST[i] = TEXT_LIST[i].split(",")
        for j in range(len(TEXT_LIST[i])):
            if TEXT_LIST[i][j].isnumeric():
                TEXT_LIST[i][j] = int(TEXT_LIST[i][j])
    return TEXT_LIST

def menu():
    """
    User chooses to search for strength or weakness
    :return:int
    """
    print("""
    Choose an option, 
    1. Search for a Pokemon Strength (super effective)
    2. Search for a Pokemon Weakness (not very effective)
    3. Exit
    """)
    CHOICE = input("> ")
    return int(CHOICE)

def getPokemonName():
    """
    User inputs pokemon name
    :return: str
    """
    return input("Pokemon Name: ")

### PROCESSING
def setupPokemon(LIST):
    """
    CREATE Tables within the database
    :param (LIST): list of pokemon
    :return:
    """
    global CONNECTION, CURSOR

    CURSOR.execute("""
        CREATE TABLE 
            pokemon (
                id INTEGER PRIMARY KEY, 
                name TEXT NOT NULL, 
                type_1 TEXT NOT NULL, 
                type_2 TEXT
            )
    ;""")

    for i in range(1, len(LIST)):
        LIST[i][2] = LIST[i][2].lower()
        LIST[i][3] = LIST[i][3].lower()
        CURSOR.execute("""
            INSERT INTO 
                pokemon
            VALUES (
                ?, ?, ?, ?
            )
        ;""", LIST[i][:4])

    CONNECTION.commit()

def setupStrongTypes(LIST):
    """
    Load and import pokemon strengths
    :param LIST: 2D Array
    :return: None
    """
    global CONNECTION, CURSOR

    for i in range(len(LIST)):
        for j in range(len(LIST[i])):
            if LIST[i][j] == "":
                LIST[i][j] = None

    CURSOR.execute("""
        CREATE TABLE
            strong (
                type TEXT PRIMARY KEY, 
                type_1 TEXT, 
                type_2 TEXT, 
                type_3 TEXT, 
                type_4 TEXT, 
                type_5 TEXT
            )
    ;""")

    for i in range(1, len(LIST)):
        CURSOR.execute("""
            INSERT INTO
                strong
            VALUES (
                ?, ?, ?, ?, ?, ?
            )
        ;""", LIST[i])

    CONNECTION.commit()

def setupWeakType(LIST):
    """
    Load and import pokemon strengths
    :param LIST: List: 2D Array
    :return: None
    """
    global CONNECTION, CURSOR

    for i in range(len(LIST)):
        for j in range(len(LIST[i])):
            if LIST[i][j] == "":
                LIST[i][j] = None

    CURSOR.execute("""
        CREATE TABLE
            weak (
                type TEXT PRIMARY KEY, 
                weak_1 TEXT,
                weak_2 TEXT,
                weak_3 TEXT,
                weak_4 TEXT,
                weak_5 TEXT
            )
    ;""")

    for i in range(1, len(LIST)):
        CURSOR.execute("""
            INSERT INTO
                weak
            VALUES (
                ?, ?, ?, ?, ?, ?
            )
        ;""", LIST[i])

        CONNECTION.commit()

def getPokemonStrengths(POKEMON):
    """
    Queries the database for the pokemon type strengths
    :param POKEMON: str
    :return: list -> list of pokemon types
    """
    global CURSOR
    TYPE1STRONG = CURSOR.execute("""
        SELECT
            strong.type_1, 
            strong.type_2,
            type_3, 
            type_4, 
            type_5
        FROM 
            pokemon
        JOIN
            strong
        ON
            strong.type = pokemon.type_1
        WHERE
            name = ?
    ;""", [POKEMON])
    print(TYPE1STRONG).fetchone()


    TYPE2STRONG = CURSOR.execute("""
        SELECT
            strong.type_1, 
            strong.type_2, 
            type_3, 
            type_4, 
            type_5
        FROM
            pokemon
        JOIN
            strong
        ON
            strong.type = pokemon.type_2
        WHERE
            name = ?
    ;""", [POKEMON]).fetchone()
    print(TYPE2STRONG)

    STRENGTHS = []
    for i in range(len(TYPE1STRONG)):
        if TYPE1STRONG[i] is not None:
            STRENGTHS.append(TYPE1STRONG[i])
    if TYPE2STRONG is not None:
        for i in range(len(TYPE2STRONG)):
            if TYPE2STRONG[i] is not None and TYPE2STRONG[i] not in STRENGTHS:
                STRENGTHS.append(TYPE2STRONG[i])

    return STRENGTHS

### OUTPUTS
def displayPokemonStrengths(NAME, RESULTS):
    """
    Displays the Pokemon's strengths nicely
    :param NAME: str
    :param Results: list
    :return: None
    """

    if len(RESULTS) > 0:
        RESULTS = ", ".join(RESULTS)
        print(f"{NAME} is strong against the following types: {RESULTS}.")
    else:
        print(f"{NAME} was not found or is not strong against any types.")


### --- VARIABLES --- ###
DATABASE_FILE = "pokemon.db"

FIRST_RUN = True

if (pathlib.Path.cwd() / DATABASE_FILE).exists():
    FIRST_RUN = False

CONNECTION = sqlite3.connect(DATABASE_FILE)
CURSOR = CONNECTION.cursor()

if __name__ == "__main__":
    ### --- MAIN PROGRAM CODE --- ###
    ### INPUTS
    if FIRST_RUN:
        CONTENT = getFileContent("pokemon_no_mega.csv")
        setupPokemon(CONTENT)
        TYPES = getFileContent("pokemon_type_strong.csv")
        setupStrongTypes(TYPES)
        WEAK = getFileContent("pokemon_type_weak.csv")
        setupWeakType(WEAK)

    while True:
        CHOICE = menu()
        ### PROCESSING
        if CHOICE == 1:
            POKEMON = getPokemonName()
            LIST_RESULTS = getPokemonStrengths(POKEMON)
        elif CHOICE == 2:
            pass
        else:
            print("Goodbye!")
            exit()
        ### OUTPUTS
        displayPokemonStrengths(POKEMON, LIST_RESULTS)
