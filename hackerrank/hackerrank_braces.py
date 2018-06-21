#!/usr/bin/env python3

def validateBraces(listOfStrs):
    if len(listOfStrs) < 2:
        raise ValueError('Argument to validateBraces() must be at least ' +
                'a 2 item list (first line with number of strings being ' +
                'passed in to be checked, followed by actual strings)')

    testInputQty = listOfStrs.pop(0) # unused, but hackerrank question defines
                                     # the input parameter (list) to contain the
                                     # string quantity as the first element !

    resultsList = []
    braceComplements = {
            '}': '{',
            ']': '[',
            ')': '('
            }

    openingBracesList = braceComplements.values()

    for item in listOfStrs:
        consumer = []
        for char in item:
            if char in openingBracesList:
                consumer.append(char)
            else:
                expectedComplementChar = braceComplements[char]
                if expectedComplementChar == consumer[-1]:
                    consumer.pop()
                else:
                    break
        if consumer == []:
            resultsList.append('YES')
        else:
            resultsList.append('NO')

    return resultsList


testInputs = [
        0,
        '[{}]', # YES
        '[)]{}', # NO
        '{[()]}', # YES
        '{[(])}', # NO
        '{{[[(())]]}}', # YES
        '', # YES
        '(', # NO
        '({)}' # NO
        ]

print('testInputs:')
for item in testInputs[1:]:
    print("'%s'" % item)
print('\noutput:')
print(validateBraces(testInputs))

