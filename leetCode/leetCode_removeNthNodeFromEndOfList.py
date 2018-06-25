#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode(object):
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

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        for _ in range(n):
            p2 = p2.next
        if p2 is None:
            return p1.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return head

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

s = Solution()
print('input:')
n1.display()
print('remove 2nd from end ...')
head = s.removeNthFromEnd(n1, 2)
print('output:')
head.display()

