# e_grades.py

"""
Title: Average Calculator
Author: Laksh Chopra
date-created: 17/11/22
"""

### --- LIBRARY IMPORTS --- ###
import sqlite3
import pathlib

### --- VARIABLES --- ###
FILENAME = "e_grades.db"
FIRST_RUN = True
# TEST if the FILENAME already exists
if (pathlib.Path.cwd() / FILENAME).exists():
    FIRST_RUN = False

CONNECTION = sqlite3.connect(FILENAME)
CURSOR = CONNECTION.cursor()

### --- SUBROUTINES --- ###
### INPUTS
def menu():
    """
    User selects how to interact with the database
    :return: int
    """
    print("""
    1. Add Course Information
    2. Reset For New Calculation
    3. Update A Singular Grade
    4. View All Grades
    5. Delete a Certain Course
    6. Calculate Average
    7. EXIT
    """)
    CHOICE = int(input("> "))
    return CHOICE

def addCourseInfo():
    """
    User enters new Course Information into a database
    :return:
    """
    global CURSOR, CONNECTION
    COURSE_ID = input("Course Id: ")
    COURSE_CATEGORY = input("Course Category: ")
    GRADE = int(input("Grade in the course: "))

    NEW_COURSE = [COURSE_ID, COURSE_CATEGORY, GRADE]
    # Checks for empty strings and replaces them with None
    for i in range(len(NEW_COURSE)):
        if NEW_COURSE[i] == "":
            NEW_COURSE[i] = None

    # add contact to database
    CURSOR.execute("""
        INSERT INTO
            grades (
                course_id,
                course_category, 
                course_grade 
            )
        VALUES (
            ?, ?, ?
        )
    ;""", NEW_COURSE)

    CONNECTION.commit()

### PROCESSING
def setup():
    """
    Creates the database table on FIRST_RUN
    :return:
    """
    global CURSOR, CONNECTION # CONNECTION only needs to be globaled when writing to the file.
    CURSOR.execute("""
        CREATE TABLE
            grades (
                id INTEGER PRIMARY KEY,
                course_id TEXT NOT NULL, 
                course_category TEXT NOT NULL, 
                course_grade INTEGER
            )
    ;""")
    CONNECTION.commit()

### OUTPUTS

if __name__ == "__main__":
### --- MAIN PROGRAM CODE --- ###
    if FIRST_RUN:
        setup()
    while True:
        ### INPUTS
        CHOICE = menu()

        ### PROCESSING
        if CHOICE == 1:
            addCourseInfo()
        elif CHOICE == 2:
            pass
        elif CHOICE == 3:
            pass
        elif CHOICE == 4:
            pass
        elif CHOICE == 5:
            pass
        elif CHOICE == 6:
            pass
        else:
            exit()

        ### OUTPUTS

