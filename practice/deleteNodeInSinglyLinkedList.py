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

def deleteNodeInSinglyLinkedList(node, nodeToBeDeleted):
    if node is nodeToBeDeleted:
        return node.next

    startNode = node

    while(node is not None):
        if node.next is nodeToBeDeleted:
            node.next = node.next.next
            return startNode
        node = node.next

x1.printList()
startNode = deleteNodeInSinglyLinkedList(x1, x3)
startNode.printList()

