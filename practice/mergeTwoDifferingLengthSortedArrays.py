#!/usr/bin/env python

def merge2SortedArrays(listA, listB):

    lenA = len(listA)
    lenB = len(listB)

    idxA = idxB = 0

    merged = []

    while (idxA < lenA and idxB < lenB):
        numFromA = listA[idxA]
        numFromB = listB[idxB]

        if numFromA <= numFromB:
            merged.append(numFromA)
            idxA += 1
        else:
            merged.append(numFromB)
            idxB += 1

    if idxA == lenA:
        merged.extend(listB[idxB:])
    else:
        merged.extend(listA[idxA:])

    return merged


listA = [-10, 0, 2, 9, 13, 18, 50]
listB = [-5, 0, 1, 5, 14, 17, 25, 30, 35, 55]
print merge2SortedArrays(listA, listB)
