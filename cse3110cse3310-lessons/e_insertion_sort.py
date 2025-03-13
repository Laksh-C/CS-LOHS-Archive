# e_insertion_sort.py

"""
title: Insertion Sort
author: Laksh Chopra
date-created: 18/09/2023
"""

def insertionSort(LIST):
    for i in range(1, len(LIST)):
        INDEX_VALUE = LIST[i]
        SORTED_INDEX = i - 1

        while SORTED_INDEX >= 0 and INDEX_VALUE < LIST[SORTED_INDEX]:
            LIST[SORTED_INDEX + 1] = LIST[SORTED_INDEX]
            SORTED_INDEX = SORTED_INDEX - 1

        LIST[SORTED_INDEX + 1] = INDEX_VALUE

if __name__ == "__main__":
    from myFunctions import *

    TIMES = []

    for i in range(30):
        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        insertionSort(NUMBERS)
        END_TIME = getTime()
        print(i)
        TIMES.append(END_TIME - START_TIME)

    print(getAverage(TIMES))