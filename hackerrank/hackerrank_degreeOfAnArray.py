#!/usr/bin/env python3
import collections

def getLengthOfMinSubArrayMatchingDegreeOfArray(listOfInts):
    itemCounts = collections.Counter(listOfInts)
    degree = max(itemCounts.values())
    itemsListForDegree = [item for item, count in itemCounts.items() if count == degree]

    reversedList = listOfInts[::-1]

    lenCounts = []
    for item in itemsListForDegree:
        itemFirstIndex = listOfInts.index(item)
        itemLastIndex = len(listOfInts) - reversedList.index(item) - 1
        lenCounts.append(itemLastIndex - itemFirstIndex + 1)
    return min(lenCounts)

listOfInts = [1, 1, 2, 2, 2, 1, 3, 0, 10]

print('listOfInts: %s' % listOfInts)
print('\noutput:')
print(getLengthOfMinSubArrayMatchingDegreeOfArray(listOfInts))

