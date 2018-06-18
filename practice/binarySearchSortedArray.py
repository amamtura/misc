#!/usr/bin/env python

import math

l = [0, 2, 5, 8, 11, 14, 17, 23, 44, 95]
print l
q = input('query # ? ')

def doBinarySearchForItemInSortedList(item, sortedList):

    if sortedList == []:
        return 'not found', 0

    minIdx = 0
    maxIdx = len(sortedList) - 1
    matchTries = 0

    if item < sortedList[minIdx] or item > sortedList[maxIdx]:
        return 'not found', 2

    if sortedList[minIdx] == item or sortedList[maxIdx] == item:
        return 'found', 2

    while 1:
        if minIdx > maxIdx:
            returnVal = 'not found'
            break

        matchTries += 1

        compareIdx = int(math.floor((minIdx + maxIdx)/2))
        print minIdx, maxIdx, compareIdx

        if sortedList[compareIdx] == item:
            returnVal = 'found'
            break
        else:
            if item < sortedList[compareIdx]:
                maxIdx = compareIdx - 1
            else:
                minIdx = compareIdx + 1

    return returnVal, matchTries

print doBinarySearchForItemInSortedList(q, l)

