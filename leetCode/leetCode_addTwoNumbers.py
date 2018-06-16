#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def display(self):
        node = self
        displayStr = ''
        while(node):
            if displayStr:
                displayStr += ' -> ' + str(node.val)
            else:
                displayStr = str(node.val)
            node = node.next
        print(displayStr)

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        int1 = linkedListToInteger(l1)
        print(int1)
        l1.display()
        int2 = linkedListToInteger(l2)
        print(int2)
        l2.display()
        sumOf = int1 + int2
        print(sumOf)
        return integerToLinkedList(sumOf)

def linkedListToInteger(ll):
    tempStr = ''
    while(ll):
        tempStr = tempStr + str(ll.val)
        ll = ll.next
    return int(tempStr[::-1])

def integerToLinkedList(i):
    prevCreatedNode = None
    for c in str(i):
        node = ListNode(int(c))
        node.next = prevCreatedNode
        prevCreatedNode = node
    return node

n1_2 = ListNode(2)
n1_4 = ListNode(4)
n1_3 = ListNode(3)
n1_2.next = n1_4
n1_4.next = n1_3

n2_5 = ListNode(5)
n2_6 = ListNode(6)
n2_4 = ListNode(4)
n2_5.next = n2_6
n2_6.next = n2_4

s = Solution()
s.addTwoNumbers(n1_2, n2_5).display()
