#!/usr/bin/env python

from Stack import Stack

testStack = Stack()

print 'stack\n3\n2\n1'
testStack.push(1)
testStack.push(2)
testStack.push(3)
# 3
# 2
# 1

# reverse a stack using recursion and no additional data structures
 
# recursive function that inserts an element at the bottom of a stack.
def _insertAtBottom(stack, item):
    if stack.empty():
        stack.push(item)
    else:
        temp = stack.pop()
        _insertAtBottom(stack, item)
        stack.push(temp)
 
# reverses the given stack using _insertAtBottom()
def reverse(stack):
    if not stack.empty():
        temp = stack.pop()
        reverse(stack)
        _insertAtBottom(stack, temp)

reverse(testStack)

print 'after reversing, pop()s ...'
print testStack.pop()
print testStack.pop()
print testStack.pop()

