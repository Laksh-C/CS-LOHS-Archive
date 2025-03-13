# main.py
'''
title: Time Management Program
author: Laksh Chopra
date-created: Dec. 20, 2022
'''

from flask import Flask, render_template, request, redirect
from pathlib import Path
import sqlite3

### --- GLOBAL VARIABLES --- ###
DB_NAME = "data.db"
FIRST_RUN = True
if (Path.cwd() / DB_NAME).exists():
    FIRST_RUN = False

### --- FLASK --- ###
app = Flask(__name__) # makes the flask object

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Renders the home page
    :return: html
    """
    return render_template("index.html")

@app.route('/to-do-date-select', methods=['GET', 'POST'])
def dateSelectPage():
    """
    Renders the home page and gets the date input from user
    :return: html
    """
    if request.form:
        DATE_INPUT = request.form.get("date")
        DATE = parseDate(DATE_INPUT)
        DAY = DATE[0]
        MONTH = DATE[1]
        YEAR = DATE[2]
        DAY = int(DAY)
        YEAR = int(YEAR)
        print(DATE)
        return redirect(f"/{DAY}/{MONTH}/{YEAR}")
    return render_template('date-select.html')

@app.route('/<DAY>/<MONTH>/<YEAR>', methods=['GET', 'POST'])
def toDoPage(DAY, MONTH, YEAR):
    """
    renders the to-do page and gets task inputs from user
    :param DAY: int
    :param MONTH: str
    :param YEAR: int
    :return: html
    """
    if request.form:
        TASK = request.form.get("task")
        print(TASK, DAY, MONTH, YEAR)
        createTask(TASK, DAY, MONTH, YEAR)
    QUERY_TASKS = getAllTasks(DAY, MONTH, YEAR)
    print(QUERY_TASKS)
    return render_template('to-do.html', day=DAY, month=MONTH, year=YEAR, tasks=QUERY_TASKS)

@app.route('/delete/<TASK>/<DAY>/<MONTH>/<YEAR>', methods=['GET', 'POST'])
def deleteTaskPage(TASK, DAY, MONTH, YEAR):
    """
    Deletes the desired task
    :param TASK: str
    :param DAY: int
    :param MONTH: str
    :param YEAR: int
    :return: redirect
    """
    deleteTask(TASK, DAY, MONTH, YEAR)
    return redirect(f"/{DAY}/{MONTH}/{YEAR}")


### --- SQLITE --- ###
def createTable():
    global DB_NAME
    CONNECTION = sqlite3.connect(DB_NAME)
    CURSOR = CONNECTION.cursor()
    CURSOR.execute("""
        CREATE TABLE
            tasks (
                task_name TEXT NOT NULL, 
                task_day INTEGER NOT NULL, 
                task_month TEXT NOT NULL, 
                task_year INTEGER NOT NULL
            )
    ;""")
    CONNECTION.commit()
    CONNECTION.close()

def createTask(TASK, DAY, MONTH, YEAR):
    """
    adds the task to the sql database
    :param TASK: str
    :param DAY: int
    :param MONTH: str
    :param YEAR: int
    :return: sql
    """
    global DB_NAME
    CONNECTION = sqlite3.connect(DB_NAME)
    CURSOR = CONNECTION.cursor()
    CURSOR.execute("""
        INSERT INTO
            tasks
        VALUES (
            ?, ?, ?, ?
        )
    ;""", [TASK, DAY, MONTH, YEAR])
    CONNECTION.commit()
    CONNECTION.close()

def getAllTasks(DAY, MONTH, YEAR):
    """
    Queries all the tasks to be displayed nicely
    :param DAY: int
    :param MONTH: str
    :param YEAR: int
    :return: 2D array
    """
    global DB_NAME
    CONNECTION = sqlite3.connect(DB_NAME)
    CURSOR = CONNECTION.cursor()
    TASKS = CURSOR.execute("""
        SELECT 
            *
        FROM
            tasks
        WHERE
            task_day = ?
        AND
            task_month = ?
        AND 
            task_year = ?
    ;""", [DAY, MONTH, YEAR]).fetchall()
    CONNECTION.close()
    return TASKS

def deleteTask(TASK, DAY, MONTH, YEAR):
    """
    Deletes a certain task
    :param TASK: str
    :param DAY: int
    :param MONTH: str
    :param YEAR: int
    :return: none
    """
    global DB_NAME
    CONNECTION = sqlite3.connect(DB_NAME)
    CURSOR = CONNECTION.cursor()
    CURSOR.execute("""
        DELETE FROM
            tasks
        WHERE 
            task_name = ?
        AND 
            task_day = ?
        AND
            task_month = ?
        AND 
            task_year = ?
    ;""", [TASK, DAY, MONTH, YEAR])
    CONNECTION.commit()
    CONNECTION.close()
def parseDate(DATE):
    """
    parsing the date into 3 distinct variables
    :param DATE: yyyy-mm-dd
    :return: integer variables
    """
    print(DATE)
    DAY = DATE[8:]
    if DAY[0] == '0':
        DAY = DATE[-1]
    DAY = int(DAY)
    MONTH = DATE[5:7]
    if MONTH[0] == '0':
        MONTH = DATE[6]
    MONTH = int(MONTH)
    YEAR = int(DATE[:4])
    MONTH_TO_TEXT = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    MONTH = MONTH_TO_TEXT[MONTH]
    DATE = [DAY, MONTH, YEAR]
    return DATE

### --- MAIN PROGRAM CODE --- ###
if __name__ == "__main__":
    if FIRST_RUN:
        createTable()
    app.run(debug=True)

