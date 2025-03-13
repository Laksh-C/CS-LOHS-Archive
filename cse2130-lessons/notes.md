// notes.md
# CSE2130 - Files and File Structures Notes
Files are used in programs to store data. That data iss often processed by the program to create information usable by the program or user. The main advantage to incorporating files into a program is *data persistence*, which means the data lasts beyond the running of the program. 

Files can be used to store settings information for the program which can be more easily edited using an external editor; it can also be used to store data created by the program for future use. Therefore, files can act as both inputs and outputs to the program similar to user inputs or outputs. 

Another major advantage to implementing files is that those files can have structures that validate data being inputted. Therefore, the file ensures the integrity of the data. *Data Integrity* is the degree of reliability of the data set (Data Bases). 

## CRUD in Text Files
1. Create a text file in python. To create a file, the files must be opened with write permissions.
    ```python
    FILE = open("filename.ext", "x") # x indicates that the file is  being opened in write mode. 
    ```
    The above function will return a *FileExistsError* if the file already exists. An alternative method is to use the write plus setting:
    ```python
    FILE = open("filename.ext", "w") # w indicates that the file is opened with write settings that will overwrite all of the existing data.
    ```
   **NOTE**: The program will look for the file relative to its location from the program file. 
   If information needs to be added to the end of the text file, use the "a" settings (append). 
    ```python
    FILE = open("filename.ext", "a") # a indicates that the file is being opened and the text is being added to the end of the file. 
    ```
2. Writing to a file requires the ```.write(String)``` dot function. Once the file is open, new content can be written into the file. 
   ```python
   FILE = open("filename.ext", "w")
   FILE.write("Hello World")
   FILE.close()
   ```
   **NOTE**: the ```.close()``` dot functions acts as both save and close.
   **NOTE**: Multiple .write() functions can be written **before** closing the file without deleting newly written content.
3. Reading a file will extract the text into a list to manipulate. 
      ```python
      FILE = open("filename.ext") # opens the file as read-only
      FILE = open("filename.ext", "r") # opens the file as read-only
      CONTENT = FILE.read()
      FILE.close()
      print(CONTENT)
      ```
      After the file is opened as read-only, the content can be saved as a string using the ```.read()``` dot function. To separate each line in the file ```.readlines()``` will create a node in a list for each line in the text.
4. Updating a file requires reading the file to extract the text, and then overwriting the file with the next. 
5. Deleting the content of a file uses the write argument, "w" and saves a blank string. For deleting the file, the os library can remove the file.
   ```python
   import os 
   os.remove("filename.ext")
   ```

# SQLite Files
## SQLite and Python
SQLite is a library that implements a small, fast, self-contained, highly reliable, full-featured, SQL database engine. **SQL** stands for *Structured Query Language* and is often pronounced *sequel*, making SQLite pronounced as "SQ-Lite" or "Sequel Lite". While many structures o the query language are similar, there are many deviations between SQL, SQLite, and other database structures. 

Databases are tables with column rules

Databases create, update, store, and generally manage data. It can also summarize the data for reporting information. Information is the *interpretation* of data for a specific shareholder. 

Databases use **transactions** to manipulate data. A transaction is a group of tasks, that is the smallest possible, that manipulates data or retrieves information. An example of a transaction is withdrawing money from a bank account. 

Databases provide several advantages than using traditional text or spreadsheet files to store data: 
1. **Concurrency** where multiple entities can interact with the data at once. Entities, in this case can be users, computer programs or other databases. An *integrated database* can have multiple applications accessing the same database.
2. **Atomicity** is the property that states that a transaction performs all tasks to complete the transaction, or it reverts so that no tasks are complete within the transaction. 
3. **Consistency** is where a transaction cannot fundamentally change the structure of the database (i.e. There is a set number of columns with specific data types within the columns. A transaction cannot change the number of columns or the data types within them.)
4. **Isolation** is where multiple transactions can occur in parallel, but do not affect each other.
5. **Durability** is where the data stored in the database can survive system failures.

All of these characteristics contribute to data *integrity* by ensuring *data validation* and *verification* with each transaction. 

Databases often use an SQL system to manage the database file. (DBMS - Database Management System)

### Setup SQLite3 in Python3
Python is a wrapper to the SQL interface. Therefore, python can interpret SQL statements, but those statements can also be interpreted by other programs. 

```python
import sqlite3

FILENAME = "databaseName.db" # an alternative extension is .sqlite

# connect python to the database. If the database file does not exist, it will create the file.
CONNECTION = sqlite3.connect(FILENAME)

# Cursor is the object that executes SQL commands
CURSOR = CONNECTION.cursor()
```

On first run, the database file is empty and tables must be created within the database. 

### CREATE a Table in the database
```python
# can be written in a single line but not recommended
CURSOR.execute(
   """
   CREATE TABLE student (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        personal_email TEXT, 
   )
   ;"""
)
CONNECTION.commit() # Validates and saves the changes to the file
```

Tables need a *primary key*, which is a unique identifier of each row of data. Each table can have only one primary key and no two rows can share the same value for a primary key. In general, primary keys are integers but can be more complex when linking multiple tables together.

Each column must identify the datatype that will appear in that particular column. Common data types in sqlite include TEXT, INTEGER, REAL NUMERIC, and BLOB. 

NOT NULL is a column property that indicates that the cell cannot be blank. 

UNIQUE is a column property that indicates that the cell cannot contain a value that is already found within the column. (i.e. it cannot repeat a value).
* You can't make a row unique because row is the actual inputted data

NOTE: Tables within a database cannot have the same name. 

### CREATE data into a Table
```python
CURSOR.execute("""
    INSERT INTO
        student
    VALUES (
        1, 
        "Michael", 
        "Zhang", 
        "Michael.Zhang@epsb.ca"
    )
;""")

CONNECTION.commit()
```
NOTE: CURSOR.execute() adds the transaction to the queue, but CONNECTION.commit() validates and saves the changes.

ASIDE: If data being entered into the table is arranged in an order that does not match the column order, the order of the data must be specified. Also, if the primary key column is omitted and the primary key is an integer value, then the table will automatically assign a primary key that is one-higher than the highest primary key. 
```python
CURSOR.execute("""
    INSERT INTO
        student (
            last_name, 
            first_name
        )
    VALUES (
        "Zhang", 
        "Michael"
    )
;""")

CONNECTION.commit()
```

#### CREATE data in a Table using Python variables
The SQL commands are strings in python. Therefore, using python techniques to insert variables into a string is possible. However, it is not recommended. Thus, the following code block should be avoided.

```python
INFO = ("Alice", "Wong", "alice.wong@epsb.ca")

CURSOR.execute(f"""
    INSERT INTO
        student (
            first_name,
            last_name,
            email
        )
     VALUES (
        {INFO[0]},
        {INFO[1]},
        {INFO[2]}
     )
;""")

CONNECTION.commit()
```

The above method of inserting variables is susceptible to SQL injection attacks that can alter data, or destroy data. Instead, SQLite has an alternative method of introducing variables into the SQL command. 

```python
INFO = ("Alice", "Wong", "alice.wong@epsb.ca")

CURSOR.execute('''
    INSERT INTO
        student (
            first_name, 
            last_name, 
            email
        )
     VALUES (
        ?, ?, ?
     )
;''', INFO)
CONNECTION.commit()
```
NOTE: In the above example the order of the data in INFO is the order that will be entered into the table

This method only applies to adding values (i.e., you cannot select columns using this method). Furthermore, the values must be entered as a tuple or a list (even if it is only one value). **The values will replace the question marks in the order they appear.**

### READ Data in a Table
There are two methods of reading data in a table, returning the first row that matches the search criteria or returning all rows that match the search criteria.

```python
FIRST_MATCH = CURSOR.execute("""
    SELECT
        id, 
        first_name, 
        last_name,
        email
    FROM
        student
;""").fetchone()

print(FIRST_MATCH) # (1, "Michael", "Zhang", "Mic...")

ALL_MATCHES = CURSOR.execute("""
    SELECT
        first_name, 
        last_name
    FROM
        student
;""").fetchall()
print(ALL_MATCHES) # [("Michael", "Zhang"), "Alice", "Wong"), ...]
```
NOTE: You can choose the order in which data is read

When selecting columns, if all columns are required, an asterisk (*) is used

### SORT Data in a Query 
Sorting data in a query allows for the results to be returned in a specific order based on a column or series of columns. Ordering the data is more frequently the last part of the SQL query. 

```python
print(CURSOR.execute("""
    Select
        *
    FROM
        student
     ORDER BY
        first_name ASC
        
;""").fetchall())
```
To chain multiple columns in a sort, separate identified columns with commas (i.e. last_name ASC, first_name DESC)

### FILTER Data in a Query
Filtering allows for a partial return of the database data based upon conditions written into the query. 
```python
print(CURSOR.execute("""
    SELECT
        * 
    FROM 
        student
    WHERE 
        first_name = "Laksh"
;""").fetchall())
```

NOTE: Filtering data goes **BEFORE** sorting data.

SQLite uses all the same conditional operations with python (i.e. >, <, !=, etc.) *except* equals, which uses only one equal sign, not two. SQLite also uses common logical operators such as OR, AND, and NOT.
```python
print(CURSOR.execute("""
    SELECT
        *
    FROM
        student
    WHERE
        first_name = "Laksh"
    AND
        id > 5
;""").fetchall())
```

SQLite can also filter from multiple values within a list
```python
print(CURSOR.execute("""
    SELECT 
        *
    FROM
        student
    WHERE 
        first_name in ("Michael", "Alice")
;""").fetchall())
```

ASIDE: The Query results can also be limited to a set number of rows.
```python
print(CURSOR.execute("""
    SELECT
        * 
    FROM 
        student
    ORDER BY
        last_name
    LIMIT
        2
;""").fetchall())
# prints the first 2 rows of the query
```

#### Filtering data using partial matches
Partial matches are also called *fuzzy searches* or *fuzzy matches* where only part of the data needs to match the search criteria. 

To specify the search pattern, the following characters are allowed:
* Case sensitivity will remain for all specific characters
* "_" to indicate a single character space that can be any character 
* "%" to indicate zero or more characters

An example of using partial matches is "___2%" which will match CSE2110, SST2170, and MAT2791, but will not match CSE1120. 

### UPDATE Data in a Table
**BE CAUTIONS** when updating existing information. If the update selects multiple rows, each row will receive the new information. In general, when updating a single row, use the Primary key to guarantee returning only one value. 

```python
CURSOR.execute("""
    UPDATE
        student
    SET
        first_name = "Mike"
    WHERE
        id = 2
;""")
CONNECTION.commit()
```

### DELETE Data in a table
```python
CURSOR.execute("""
    DELETE FROM
        student
    WHERE
        id = 2
;""")

CONNECTION.commit
```
Similar to updating data in a table, use the primary key whenever possible to ensure deleting an exact row. 

#### Delete a table
To delete a table, the entire table, including its title, will no longer be in the database. Therefore, any code directly relating to the table name will output an error. To delete a table, use the following command: 
```python
CURSOR.execute("""
    DROP TABLE
        student
;""")

CONNECTION.commit()
```

# Normalization (IB)
*Normalization* adjusts the data within a table into a standard configuration so that SQL Queries can more easily process information. Normalization contributes to the overall integrity of the data. The normalization rules are developed by *Edgar Codd*, who came up with the first three rules of normalization. 

## First Normalization Form (1NF)
Every field in the table cannot be empty. (Another way of saying this is that all cells in the table must be filled). 

NOTE: Null cells usually do not count for 1NF. However, there is no formal rule against them. IB does not count NULL as a filled cell. 

Separate tables into multiple tables using the primary key to link the rows together. 

## Second Normalization Form (2NF)
Every column of data must be related to the primary key. The *Primary Key* is a unique value within a column. Unique values, which is also a column setting, unique values are ones where a column does not have a repeated value. 

NOTE: While there can be many columns set to enforce unique values, only one column (or set of columns) is considered the primary key. 

## Third Normalization Form (3NF)
Every column does not have secondary relational data separate from the primary key. (In other words, one column cannot depend on the information of another column that is not part of the primary key). 

* All tables in 2NF and 3NF have a primary key.
  * Primary keys can also be a composition of two or more columns. Then the key is called a primary *composite* key.
  * Foreign key is a column of primary keys from another table. The foreign key is used to create references to other tables.

## Joining Tables
With normalized tables separating data, there are many instances where a query will need data from two or more tables. Instead of performing multiple queries sequentially (for example, query a student, then use the student's id as a foreign key to query the course name that the student is taking), tables can be joined together using the foreign key column to return rows in the table where the foreign key is the primary key. Therefore, one query can return results from multiple tables. It is possible to join any number of tables together. 

```python
# use the student table from above.

CURSOR.execute("""
    CREATE TABLE
        course (
            course_id TEXT PRIMARY KEY, 
            course_name TEXT NOT NULL
        )
;""")

CURSOR.execute("""
    CREATE TABLE
        student_schedule (
            student_id INTEGER, 
            course_id TEXT, 
            course_room INTEGER, 
            PRIMARY KEY (student_id, course_id)
        )
;""")

# ASSUME data has been added to all tables

## Joining of Tables

ROWS = CURSOR.execute("""
    SELECT
        student.first_name, 
        student.last_name, 
        course.course_name, 
        student_schedule.course_room
    FROM
        student_schedule
    JOIN
        student
    ON
        student_schedule.student_id = student.id
    JOIN
        course
    ON
        student_schedule.course_id = course.course_id
    WHERE
        student_schedule.student_id = 1458662
;""").fetchall()

```

## Additional IB Notes
### Terminology
* __Data Definition Language (DDL)__ is a language that can create, modify, and manage the structure of databases. (Examples include MSSQL, MySQL, and SQLITE)
* __Relational Database Management System (RDBMS)__ is a database management system that allows users to identify and access data _in relation_ to another piece of data in the database. SQLite is a RDBMS as it allows multiple tables together.
* __Secondary Key__ is an additional column within a table that enforces unique values that can be used to identify a single row.
* __Candidate Key__ is any column that can be used to identify a single row. Candidate keys are not composites of multiple columns. Primary and secondary keys are candidate keys (assuming that the primary key is not composite)
* __Referential Integrity__ is where tables within a database refer to each other using primary keys within each table. When designing data storage, tables are joined by only using foreign keys. 
* __Simple vs. Complex Queries__ A simple query accesses a small number of tables within a small number of filters (often one table and one filter). Complex queries access multiple tables, often with joins, and often use multiple filters. Complex queries may also use subqueries. 
* __Data Matching__ is the process of comparing two separate tabels/databases for the purpose of verification and/or validation. For example, two tables can be comapred to identify duplicate data.
* __Data Mining__ is the process of analyzing datasets to identify anomalies or patterns that may predict future outcomes. <-- Machine Learning and AI

### Schema
A database schema defines how data is organized within a relational database; this is inclusive of logical constraints such as table names, fields, data types, and the relationship between entities. 
* __Conceptual schemas__, which offer a big-picture view of what the system will contain, how it will be organized, and which business rules are involved. These are often created in the planning process and are represented by UML tables. 
* __Logical schemas__, which are clearly defined schema objects of information, such as table names, filed names, entity relationships, and integrity constraints. SQL commands are written as logical schemas.
* __Physical schemas__ provide the technnical information such as where the data is being stored.

### Data Dictionaries
When designing databases, data dictionaries formalize what the expected data is within each table column. Data dictionaries include the metadata of the column.

| Data Table ||||
| --- | --- | --- | --- |
| __id__ | __first_name__ | __last_name__ | dept_id |
| 1234567 | Laksh | Chopra | 344 |

| Data Dictionary |||
| --- | --- | --- |
| _column_ | __data_type__ | __description__ |
| id | integer | primary key of the table |
| first_name | text/varchar(32) | first name of the employee |
| last_name | text/varchar(32) | last name of the employee. It can not be empty |
| dept_id | integer | employee department (foreign key) |

### Relationship Types (in databases)
When referencing data between tables, there are three main relationships between entities. 
1. __one-to-one__, where one row in one table will relate to none, or one row in the referenced table. (This relationship normally enforces a business rule).
2. __one-to-many__, where one row in one table will relate to none, one, or many rows in the referenced table. (This is the most common entity relation). 
3. __many-to-many__, where rows in both tables can relate to none, one, or many rows in the other table. 

### Derived Columns
Often called _generated columns_ or _computed columns_, derived columns are columns with a table that is calculated from data found in other columns.

```python
CURSOR.execute("""
    CREATE TABLE
        contacts (
            id INTEGER PRIMARY KEY, 
            first_name TEXT NOT NULL, 
            last_name TEXT NOT NULL, 
            full_name TEXT GENERATED ALWAYS AS (
                first_name || " " || last_name
            ),
            email TEXT
        )
;""")
# NOTE: || concatenates two strings in sql. int/real use regular mathematical operations. REAL is used instead of FLOAT

CURSOR.execute("""
    INSERT INTO
        contacts (
            first_name, 
            last_name, 
            email
        )
     VALUES (
        "Laksh"
        "Chopra"
        "lakshc18@gmail.com"
     )
;""")

print(CURSOR.execute("""
    SELECT
        full_name
    FROM
        contacts
;""").fetchone())
# Prints "Laksh Chopra"
```

### Additional Database Models
* **Relational Database** - Databases that store data in one or more tables so that column data *relates* to row data. Most databases like SQLite, MySQL, and MS SQL are relational Databases. 
* **Object-Oriented Databases** - Databases that not only store data, but can perform specific actions on data housed in a digital object. (Object-oriented programming is explored in CS30). An example of an Object-oriented database model is the python library SQLAlchemy. 
* **Network Databases** - Databases, often relational databases, that include data ownership. Therefore, specific data within the database can have none, one, or many owners, which can have varying levels of access to the data. (A rudimentary example is a Google Sheet because Google Sheets allows permissions for individual fields).
* **Spacial Databases** - Databases, often relational databases, that include geometric data and actions within the database. An example is a database that stores geographical locations and can produce a map. 
* **Multi-dimensional Databases** - Databases that include multiple database models used in *data warehousing* and *online analytical processing* such as data mining. 

### Data Warehousing
A __data warehouse__ is an enterprise system that aggregates data from different sources into a single, central consistent data store. This data can be stored in a structured or semi-structured systems where data is managed from multiple sources. Examples of data warehousing is point-of-sales transactions, marketing automation, and customer relations management. Other uses of a data warehouse is for data mining, artifical intelligence and machine learning. Systems do not manipulate data within a data warehouse; instead, data from active databases are sent to a data warehouse for _reporting and analytics_. The process to sending information from active databases and other sources to a data warehouse requires __E__xtracting the data from the various, __T__ransforming the data into a univorm format for specialized processing and __L__oading the extracted data into the data warehouse. This process ic called the __ETL__. 

### Data Mining
There are many forms of discovering patterns using data mining. 
* __Cluster Analysis__ is an unsupervised learning algorithm where similarities between the data reveal associations between two or more data points. These associations lead to clusters of data points in graphed or charted data. This is how social media algorithms work. NOTE: Cluster analysis reveals correlation, not causation.
* __Associations__ are if...then... associations within the data. They use _support_ and _confidence_ to identify important relationships. Support is the frequency of the pre-cursor and confidence is the frequency that the pre-cursor leads to the desired or predicted outcome. An example of an association is that if a student eats a complete breakfast (pre-cursor), they will remember more content from that day's lesson (outcome). 
* __Classifications__ label each data instance in a dataset based on its features. Then modelling algorithms use the labels to predict the class labels of new instances. Example: inbox tagging emails as spam/not spam. In machine learning, this is called supervised training. 
* __Sequence Patterns__ is comparing the sequence of data to find patterns. This feature looks at a list of data instead of individual data points. Wireless WEP encryption algorithms embed the WEP passphrase within each data packet transmitted and recerived over the wireless network. Mendeleev predicted several elements in the periodic table that were not discovered by European science. However, because of the sequential nature of elemental properties, Mendeleev identified missing elements within the sequence. 
* __Forecasting__ uses past and present data to predict the future. Examples include weather patterns and the stock market. 
* __Link Analysis__ visualizes the relationships between different data points, such as people, organizations, events, or transactions. This analysis tends to be multi-modal, which means it links data across various categories. This application of data mining can find anomalies within the data. For example, credit card fraud detection uses location history and purchasing patterns to determine if a current purchase is legitimate. __Deviation Detection__ is when a new event contradicts the current model created from data mining. 

### SQLite vs SQL
* TEXT vs VARCHAR as a datatype. VARCHAR is a datatype for a column that specifies the maximum number of characters available within that field. In the database schema, setting a column to VARCHAR(16) will only allow 16 total characters in that field. 
* CHAR datatype must be a string of specific size. CHAR(1) can only have a single string character, it cannot have a blank. 
* LONG datatype is a really big integer
* DOUBLE datatype is for decimal numbers