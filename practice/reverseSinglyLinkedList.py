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

def reverseLinkedList(node):
    prev = None

    while node:
        tmp = node.next

        node.next = prev

        prev = node
        node = tmp

x1.printList()
x5.printList()

reverseLinkedList(x1)

x1.printList()
x5.printList()

