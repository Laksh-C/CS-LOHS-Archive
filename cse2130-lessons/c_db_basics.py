# c_db_basics.py

"""
Title: Database Basics
Author: Laksh Chopra
date-created: 04/11/22
"""

import sqlite3

### --- VARIABLES --- ###
FILENAME = 'c_contacts.db' # alternative extension is .sqlite

CONNECTION = sqlite3.connect(FILENAME)
CURSOR = CONNECTION.cursor()

# CREATE the database table

CURSOR.execute("""
    CREATE TABLE
        contacts (
            id INTEGER PRIMARY KEY, 
            first_name TEXT NOT NULL, 
            email TEXT
        )   
;""")

CONNECTION.commit() # writes the changes validated in the CURSOR.execute() into the file

# CREATE ROWS of data
CURSOR.execute("""
    INSERT INTO
        contacts
    VALUES (
        1, 
        "Laksh", 
        "l.chopra@share.epsb.ca"
        )
;""")

CURSOR.execute("""
    INSERT INTO
        contacts(
            first_name, 
            email
        )
    VALUES (
        "Alice", 
        "a.wong@share.epsb.ca"
        )
;""")

CONNECTION.commit()

# READ Data from the table

USERS = CURSOR.execute("""
    SELECT
        *
    FROM
        contacts
;""").fetchall()

print(USERS)