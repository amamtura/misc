#!/usr/bin/env python

from SingleLinkedListNode import SingleLinkedListNode

x1=SingleLinkedListNode(1)
x2=SingleLinkedListNode(2)
x3=SingleLinkedListNode(3)
x4=SingleLinkedListNode(4)
x5=SingleLinkedListNode(5)

x1.next = x2
x2.next = x3
x3.next = x4
x4.next = x5
x5.next = x1 # Loop !
# NOTE: loop possible ONLY from last node to wherever
# (first, intermediate, self/last) ... since SingleLinkedListNode

# Using hare and tortoise method
def detectLoop(slowPtr):

    if slowPtr is None:
        return 'no linked list was passed into function'

    result = 'no loop found'

    if slowPtr.next:
        fastPtr = slowPtr.next.next
    else:
        fastPtr = None

    while slowPtr:

        if fastPtr is None:
            break

        if slowPtr == fastPtr:
            result = 'loop found'
            break

        slowPtr = slowPtr.next

        if fastPtr.next:
            fastPtr = fastPtr.next.next
        else:
            break

    return result

# Some test case inputs:
# 1) Null
# 2) single node list, with n1.next = None
# 3) single node list, with n1.next = n1 (loop)
# 4) 2 node list, with n2.next = None
# 5) 2 node list, with n2.next = n1 (loop)
# 6) multi node list, with last.next = None
# 7) multi node list, with last.next = any node (including self) (loop)

print(detectLoop(x1))

