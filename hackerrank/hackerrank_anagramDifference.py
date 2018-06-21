#!/usr/bin/env python3
import operator
from functools import reduce

def getCharacterQtyDiffForAnagram(listA, listB):
    noOfStrings = len(listA)
    results = []

    for i in range(noOfStrings):
        strA = listA[i]
        strB = listB[i]

        if len(strA) != len(strB):
            results.append(-1)
            continue

        concatStr = strA + strB
        if reduce(operator.xor, [ord(x) for x in concatStr]) == 0:
            results.append(0)
            continue

        listOfCharsForA = list(strA)
        listOfCharsForB = list(strB)

        charactersThatAreDifferent = [char for char in listOfCharsForA if char not in listOfCharsForB]
        results.append(len(charactersThatAreDifferent))

    return results

listA = [ 'ate', '' , 'catman', 'aaa' ]
listB = [ 'tea', '1', 'batman', 'bbb' ]

print('inputs:')
print(listA)
print(listB)
print('\noutput:')
print(getCharacterQtyDiffForAnagram(listA, listB))

