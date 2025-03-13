# i_nested_arrays.py

"""
Title: 2D Array Practice
Author: Laksh Chopra
Date-Created: 18/10/22
"""

### Example Problem
def example():
    GRID = []
    # Fill in the GRID
    for row in range(SIZE):
        GRID.append([])  # appends an empty row
        for column in range(SIZE):
            GRID[row].append(row * SIZE + column + 1)
    # OUTPUT
    for row in range(SIZE):
        print(GRID[row])

def prob4():
    print("\nProblem 4")
    GRID = []
    # Fill in the GRID
    for row in range(SIZE):
        GRID.append([])  # appends an empty row
        for column in range(SIZE):
            GRID[row].append(SIZE*SIZE-((row+1)*SIZE)+column+1)
    # OUTPUT
    for row in range(SIZE):
        print(GRID[row])

def prob1():
    print("\nProblem 1")
    GRID = []
    # Fill in the GRID
    for row in range(SIZE):
        GRID.append([])
        for column in range(SIZE):
            GRID[row].append(column)
    # OUTPUT
    for row in range(SIZE):
        print(GRID[row])

def prob2():
    print("\nProblem 2")
    GRID = []
    # Fill in the GRID
    for row in range(SIZE):
        GRID.append([])
        for column in range(SIZE):
            GRID[row].append(row)
    # OUTPUT
    for row in range(SIZE):
        print(GRID[row])

def prob3():
    print("\nProblem 3")
    GRID = []
    # Fill in the GRID
    for row in range(SIZE):
        GRID.append([])
        for column in range(SIZE):
            GRID[row].append((row*SIZE)+SIZE-column)
    # OUTPUT
    for row in range(SIZE):
        print(GRID[row])

def prob5():
    print("\nProblem 5")
    GRID = []
    # Fill in the GRID
    for row in range(SIZE):
        GRID.append([])
        for column in range(SIZE):
            GRID[row].append(SIZE*(SIZE-row)-column)
    # OUTPUT
    for row in range(SIZE):
        print(GRID[row])

def prob6():
    print("\nProblem 6")
    GRID = []
    # Fill in the GRID
    for row in range(SIZE):
        GRID.append([])
        for column in range(SIZE):
            GRID[row].append((SIZE*column+1)+row)
    # OUTPUT
    for row in range(SIZE):
        print(GRID[row])

def prob7():
    print("\nProblem 7")
    GRID = []
    # Fill in the GRID
    for row in range(SIZE):
        GRID.append([])
        for column in range(SIZE):
            if (row+1) %2 == 0:
                GRID[row].append(SIZE*(row+1)-column)
            else:
                GRID[row].append((row*SIZE)+column+1)
    # OUTPUT
    for row in range(SIZE):
        print(GRID[row])

def prob8():
    print("\nProblem 8")
    GRID = []
    # Fill in the GRID
    for row in range(SIZE):
        GRID.append([])
        for column in range(SIZE):
            if (column+1) %2 == 0:
                GRID[row].append((column+1)*SIZE-row)
            else:
                GRID[row].append(column*SIZE+row+1)
    # OUTPUT
    for row in range(SIZE):
        print(GRID[row])

def prob12():
    print("\nProblem 12")
    GRID = []
    # Fill in the GRID
    for row in range(SIZE):
        GRID.append([])
        for column in range(SIZE):
            GRID[row].append(SIZE-2)
        if column+1 == range((SIZE-2)):
            GRID[row].append(SIZE-column-1)
    # OUTPUT
    for row in range(SIZE):
        print(GRID[row])

def prob9():
    print("\nProblem 9")
    GRID = []
    # Fill in the GRID
    for row in range(SIZE):
        GRID.append([])
        for column in range(SIZE):
            GRID[row].append(column+1)
            if(row+1) >= (column+1):
                GRID[row].append("other")


    # OUTPUT
    for row in range(SIZE):
        print(GRID[row])

if __name__ == "__main__":
    SIZE = 5
    example()
    prob1()
    prob2()
    prob3()
    prob4()
    prob5()
    prob6()
    prob7()
    prob8()
    prob9()
    #prob10()
    #prob11()
    #prob12()

