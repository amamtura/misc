#!/usr/bin/env python

testString = 'madam'

def isPalindrome(strToTest):
  length = len(strToTest)

  if length == 0 or length == 1:
    return True

  if strToTest[0] == strToTest[-1]:
    return isPalindrome(strToTest[1:-1])
  else:
    return False

print isPalindrome(testString)

