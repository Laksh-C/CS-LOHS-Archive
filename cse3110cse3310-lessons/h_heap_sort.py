# h_heap_sort.py
"""
title: heap sort algorithm
author: Laksh Chopra
date-created 05/10/2023
"""

def heapify(LIST, LEN_ARRAY, ROOT_INDEX):
    """
    moves the highest value to index 0 (top of the library)
    :param LIST: list
    :param LEN_ARRAY: int
    :param ROOT_INDEX: int
    :return:
    """

    LARGEST_INDEX = ROOT_INDEX

    LEFT_INDEX = 2 * ROOT_INDEX + 1
    RIGHT_INDEX = 2 * ROOT_INDEX + 2

    # check if left child is greater than the parent
    if LEFT_INDEX < LEN_ARRAY and LIST[ROOT_INDEX] < LIST[LEFT_INDEX]:
        LARGEST_INDEX = LEFT_INDEX

    # check if the right child is greater than the parent/left index
    if RIGHT_INDEX < LEN_ARRAY and LIST[LARGEST_INDEX] < LIST[RIGHT_INDEX]:
        LARGEST_INDEX = RIGHT_INDEX

    # change the root/parent with a child if needed
    if LARGEST_INDEX != ROOT_INDEX:
        TEMP = LIST[ROOT_INDEX]
        LIST[ROOT_INDEX] = LIST[LARGEST_INDEX]
        LIST[LARGEST_INDEX] = TEMP

        heapify(LIST, LEN_ARRAY, LARGEST_INDEX)

def heapSort(LIST):
    """
    sorts the arrawy using a binary tree
    :param LIST: list (int)
    :return: none
    """
    LEN_ARRAY = len(LIST)

    # build a max heap (highest number is at the top of each tree)
    for i in range(LEN_ARRAY, - 1, -1):
        heapify(LIST, LEN_ARRAY, i)

    # extract the highest element
    for i in range(LEN_ARRAY-1, 0, -1):
        TEMP = LIST[0]
        LIST[0] = LIST[i]
        LIST[i] = TEMP
        heapify(LIST, i, 0)

if __name__ == "__main__":
    from myFunctions import *

    TIMES = []

    for i in range(30):
        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        heapSort(NUMBERS)
        END_TIME = getTime()
        print(i)
        TIMES.append(END_TIME - START_TIME)

    print(getAverage(TIMES))
