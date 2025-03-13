# d_selection_sort.py

"""
title: Selection Sort
author: Laksh Chopra
date-created 18/09/2023
"""

def selectionSort(LIST):
    """
    Compares the current index value with the rest of the set. It will find the lowest value in the set and place it in the lowest position of the unsorted section of the list.
    :param LIST: list (int) -> unsorted
    :return: none
    """
    for i in range(len(LIST)-1):
        MINIMUM_INDEX = i
        for j in range(i+1, len(LIST)):
            if LIST[j] < LIST[MINIMUM_INDEX]:
                MINIMUM_INDEX = j
        if LIST[MINIMUM_INDEX] < LIST[i]:
            TEMP = LIST[i]
            LIST[i] = LIST[MINIMUM_INDEX]
            LIST[MINIMUM_INDEX] = TEMP

if __name__ == "__main__":
    from myFunctions import *

    TIMES = []


    for i in range(30):
        NUMBERS = getRandomList(10000)
        
        START_TIME = getTime()
        selectionSort(NUMBERS)
        END_TIME = getTime()
        TIMES.append(END_TIME - START_TIME)
        print(i)
    print(getAverage(TIMES))
