# main.py
'''
title: Flask web app for contacts
author: Laksh Chopra
date-created: DEC. 5, 2022
'''

from flask import Flask, render_template, request, redirect
from pathlib import Path
import sqlite3

### --- GLOBAL VARIABLES --- ###
DB_NAME = "flask.db"
FIRST_RUN = True
if (Path.cwd() / DB_NAME).exists():
    FIRST_RUN = False

### --- FLASK --- ###
app = Flask(__name__)  # makes the flask object

@app.route('/', methods=['GET', 'POST'])
def index():
    ALERT = ""
    if request.form:
        FIRST_NAME = request.form.get("first_name")
        LAST_NAME = request.form.get("last_name")
        EMAIL = request.form.get("email")
        print(FIRST_NAME, LAST_NAME, EMAIL)
        if EMAIL != "" and FIRST_NAME != "":
            if getOneContact(EMAIL) is None:
                createContact(FIRST_NAME, LAST_NAME, EMAIL)
                ALERT = "Successfully added a new contact"
            else:
                ALERT = "A contact with the given email already exists"
        else:
            ALERT = "Please fill in the required fields: First Name and Email."
    QUERY_CONTACTS = getAllContacts()
    return render_template("index.html", alert=ALERT, contacts=QUERY_CONTACTS)

@app.route('/delete/<ID>')
def deleteContactPage(ID):
    deleteContact(ID)
    return redirect('/')

### --- SQLITE --- ###
def createTable():
    global DB_NAME
    CONNECTION = sqlite3.connect(DB_NAME)
    CURSOR = CONNECTION.cursor()
    CURSOR.execute("""
        CREATE TABLE
            contacts (
                first_name TEXT NOT NULL, 
                last_name TEXT, 
                email TEXT PRIMARY KEY
            )
    ;""")
    CONNECTION.commit()
    CONNECTION.close()

def createContact(FIRST_NAME, LAST_NAME, EMAIL):
    global DB_NAME
    CONNECTION = sqlite3.connect(DB_NAME)
    CURSOR = CONNECTION.cursor()
    CURSOR.execute("""
        INSERT INTO 
            contacts
        VALUES (
            ?, ?, ?
        )
    ;""", [FIRST_NAME, LAST_NAME, EMAIL])
    CONNECTION.commit()
    CONNECTION.close

### PROCESSING
def deleteContact(EMAIL):
    global DB_NAME
    CONNECTION = sqlite3.connect(DB_NAME)
    CURSOR = CONNECTION.cursor()
    CURSOR.execute("""
        DELETE FROM
            contacts
        WHERE 
            email = ?
    ;""", [EMAIL])
    CONNECTION.commit()
    CONNECTION.close()

### OUTPUTS
def getOneContact(EMAIL):
    global DB_NAME
    CONNECTION = sqlite3.connect(DB_NAME)
    CURSOR = CONNECTION.cursor()
    CONTACT = CURSOR.execute("""
        SELECT
            *
        FROM
            contacts
        WHERE
            email = ?
    ;""", [EMAIL]).fetchone()
    CONNECTION.close()
    return CONTACT

def getAllContacts():
    global DB_NAME
    CONNECTION = sqlite3.connect(DB_NAME)
    CURSOR = CONNECTION.cursor()
    CONTACTS = CURSOR.execute("""
        SELECT
            *
        FROM
            contacts
        ORDER BY 
            first_name
    ;""").fetchall()
    CONNECTION.close()
    return CONTACTS


if __name__ == "__main__":
    if FIRST_RUN:
        createTable()
    app.run(debug=True)
