# a_file_actions.py

"""
title: Basic File Actions
Author: Laksh Chopra
date-created: 31/10/22
"""

FILENAME = "a_file.txt"


# EX 1 - Create, open and close a file
try:
    FILE = open(FILENAME, "x")
    FILE.close()
except FileExistsError:
    FILE = open(FILENAME)
    FILE.close()

# EX 2 - Write to a file
FILE = open(FILENAME, "w")
FILE.write("Hello World")
FILE.close()

# EX 3 - Read a file
FILE = open(FILENAME)
TEXT = FILE.read()
FILE.close()
print(TEXT)

# EX 4 - Updating a File
## Overwrite the contents of a file
FILE = open(FILENAME, "w")
FILE.write("Dolly the Sheep")
FILE.close()
FILE = open(FILENAME)
print(FILE.read())
FILE.close()

## Update contents require the contents to be read first.
FILE = open(FILENAME)
TEXT = FILE.read()
FILE.close()
TEXT = TEXT.upper()
FILE = open(FILENAME, "w")
FILE.write(TEXT)
FILE.close()

## Append Content to the end of the file.
FILE = open(FILENAME, "a")
FILE.write("Sven the reindeer")
FILE.write("\nSven the reindeer") # Add Sven as a new line
FILE.close()
FILE = open(FILENAME)
print(FILE.read())
FILE.close()

# EX 3B - Reading a file line by line
# Using Readlines
FILE = open(FILENAME)
print(FILE.readline())
FILE.close()
FILE = open(FILENAME)
print(FILE.readlines())
FILE.close()
# NOTE: This method is not ideal for splitting lines because of the \n symbol
FILE = open(FILENAME)
LINES = FILE.read().splitlines()
FILE.close()
print(LINES)

# EX 5 - Deleting a File
import os
os.remove(FILENAME)
