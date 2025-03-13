# myFunctions.py
"""
title: Useful Functions for testing algorithms
author: Laksh Chopra
date-created 14/09/2023
"""

import random, statistics, time

def getSortedList(SIZE):
    """
    returns a sorted list of approximately size SIZE
    :param SIZE: int
    :return: list (int)
    """
    NUMBERS = []
    for i in range(2 * SIZE):
        if random.randrange(2) == 1:
            NUMBERS.append(i)
    return NUMBERS

def getRandomList(SIZE):
    """
    return a randomized list of approximately size SIZE
    :param SIZE: int
    :return: list (int)
    """

    NUMBERS = getSortedList(SIZE)
    random.shuffle(NUMBERS)

    return NUMBERS

def getAverage(LIST):
    """
    returns the average of the given list.
    :param LIST: list (int)
    :return: float
    """
    return statistics.mean(LIST)

def getTime():
    """
    returns perf_counter()
    :return: float
    """
    return time.perf_counter()

if __name__ == "__main__":
    NUM = getRandomList(10)
    print(getAverage([3, 4, 5]))
    print(getTime())
    print(NUM)













