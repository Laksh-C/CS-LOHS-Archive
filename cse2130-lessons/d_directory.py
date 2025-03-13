# d_directory.py

"""
Title: Contacts Directory
Author: Laksh Chopra
date-created: 07/11/22
"""

### --- LIBRARY IMPORTS --- ###
import sqlite3
import pathlib

### --- VARIABLES --- ###
FILENAME = "d_contacts_directory.db"
FIRST_RUN = True
# TEST if the FILENAME already exists
if (pathlib.Path.cwd() / FILENAME).exists():
    FIRST_RUN = False

CONNECTION = sqlite3.connect(FILENAME)
CURSOR = CONNECTION.cursor()

### --- SUBROUTINES --- ###
### INPUTS
'''
def menu() -> int:
    """
    User selects how to interact with the database
    :return: int
    """
'''
def menu():
    """
    User selects how to interact with the database
    :return: int
    """
    print("""
    1. Search for a contact
    2. View all contacts
    3. Add contact
    4. Edit contact
    5. Delete contact
    6. EXIT
    """)
    CHOICE = int(input("> "))
    return CHOICE
def addContact():
    """
    User enters a new contact into a database
    :return:
    """
    global CURSOR, CONNECTION
    FIRST_NAME = input("First Name: ")
    LAST_NAME = input("Last Name: ")
    EMAIL = input("Email: ")
    INSTA = input("Instagram: ")

    NEW_CONTACT = [FIRST_NAME, LAST_NAME, EMAIL, INSTA]
    # Checks for empty strings and replaces them with None
    for i in range(len(NEW_CONTACT)):
        if NEW_CONTACT[i] == "":
            NEW_CONTACT[i] = None

    # add contact to database
    CURSOR.execute("""
        INSERT INTO
            contacts (
                first_name, 
                last_name, 
                email, 
                instagram
            )
        VALUES (
            ?, ?, ?, ?
        )
    ;""", NEW_CONTACT)

    CONNECTION.commit()

def searchContactName():
    """
    Ask for first name of contact
    :return: string
    """
    NAME = input("First Name: ")
    return NAME

def getContactId():
    """
    User selects an individual contact
    :return: int --> Primary Key
    """
    global CURSOR

    CONTACTS = CURSOR.execute("""
        SELECT
            id,
            first_name, 
            last_name
        FROM
            contacts
        ORDER BY
            first_name, 
            last_name
    ;""").fetchall()

    print("Please select a contact")
    for i in range(len(CONTACTS)):
        print(f"{i+1}. {CONTACTS[i][1]} {CONTACTS[i][2]}")

    ROW_INDEX = input("> ")
    ROW_INDEX = int(ROW_INDEX) - 1
    CONTACT_ID = CONTACTS[ROW_INDEX][0]
    return CONTACT_ID

def updateContact(ID):
    """
    Allows user to update an ID
    :param ID: int -> Primary Key
    :return: None
    """
    global CURSOR, CONNECTION
    # inputs
    CONTACT = CURSOR.execute("""
        SELECT
            first_name, 
            last_name, 
            email, 
            instagram
        FROM 
            contacts
        WHERE 
            id = ?
    ;""", [ID]).fetchone()
    print("Leave field blank for no changes")
    INFO = []
    INFO.append(input(f"First Name: ({CONTACT[0]}): "))
    INFO.append(input(f"Last Name: ({CONTACT[1]}): "))
    INFO.append(input(f"Email: ({CONTACT[2]}): "))
    INFO.append(input(f"Instagram: ({CONTACT[3]}): "))
    # processing
    for i in range(len(INFO)):
        if INFO[i] == "":
            INFO[i] = CONTACT[i]

    INFO.append(ID)
    CURSOR.execute("""
        UPDATE
            contacts
        SET
            first_name = ?, 
            last_name = ?, 
            email = ?, 
            instagram = ?
        WHERE
            id = ?
    ;""", INFO)

    # outputs
    CONNECTION.commit()
    print(f"{INFO[0]} successfully updated!")

### PROCESSING
def setup():
    """
    Creates the database table on FIRST_RUN
    :return:
    """
    global CURSOR, CONNECTION # CONNECTION only needs to be globaled when writing to the file.
    CURSOR.execute("""
        CREATE TABLE
            contacts (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL, 
                last_name TEXT, 
                email TEXT NOT NULL, 
                instagram TEXT
            )
    ;""")
    CONNECTION.commit()

def queryContactName(NAME):
    """
    Queries the database for the contact
    :param NAME: str
    :return: list --> Tuples
    """
    global CURSOR

    RESULTS = CURSOR.execute("""
        SELECT 
            first_name, 
            last_name, 
            email, 
            instagram
        FROM   
            contacts
        WHERE 
            first_name = ?
        ORDER BY 
            first_name, 
            last_name
    ;""", [NAME]).fetchall()

    return RESULTS

def deleteContact(CONTACT_ID):
    """
    Deletes a contact from the contacts database
    :param CONTACT_ID: int -> Primary Key
    :return: None
    """
    global CURSOR, CONNECTION

    CONTACT = CURSOR.execute("""
        SELECT
            first_name, 
            last_name
        FROM
            contacts
        WHERE 
            id = ?
    ;""", [CONTACT_ID]).fetchone()

    # DELETE
    CURSOR.execute("""
        DELETE FROM
            contacts
        WHERE 
            id = ?
    ;""", [CONTACT_ID])

    CONNECTION.commit()

    print("%s %s successfully deleted!" % CONTACT)
### OUTPUTS
def displayAllContacts():
    """
    Prints out all contacts nicely
    :return: None
    """
    global CURSOR
    CONTACTS = CURSOR.execute("""
        SELECT 
            first_name, 
            last_name
        FROM
            contacts
        ORDER BY
            first_name,
            last_name
            
    ;""").fetchall()

    print("All Contacts")
    print("------------")
    for contact in CONTACTS:
        print(contact[0], contact[1])
def displayResults(RESULTS):
    """
    Displays results nicely
    :param RESULTS: list --> tuples
    :return: None
    """
    for CONTACT in RESULTS:
        print(f"{CONTACT[0]} {CONTACT[1]} (email: {CONTACT[2]}) (instagram: {CONTACT[-1]})")

if __name__ == "__main__":
### --- MAIN PROGRAM CODE --- ###
    if FIRST_RUN:
        setup()
    while True:
        ### INPUTS
        CHOICE = menu()

        ### PROCESSING
        if CHOICE == 1:
            NAME = searchContactName()
            RESULTS = queryContactName(NAME)
        elif CHOICE == 3:
            addContact()
        elif CHOICE == 4:
            CONTACT = getContactId()
            updateContact(CONTACT)
        elif CHOICE == 5:
            CONTACT = getContactId()
            deleteContact(CONTACT)
        elif CHOICE == 6:
            exit()

        ### OUTPUTS
        if CHOICE == 2:
            displayAllContacts()
        elif CHOICE == 1:
            displayResults(RESULTS)
