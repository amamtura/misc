#!/usr/bin/env python
from SingleLinkedListNode import SingleLinkedListNode

x1=SingleLinkedListNode(1)
x2=SingleLinkedListNode(2)
x3=SingleLinkedListNode(3)
x4=SingleLinkedListNode(4)
x5=SingleLinkedListNode(5)
x6=SingleLinkedListNode(6)
x7=SingleLinkedListNode(7)

x1.next = x2
x2.next = x3
x3.next = x4
x4.next = x5
x5.next = x6
x6.next = x7

def detectMiddleNodeInOnePass(snp):

    if snp is None:
        raise ValueError('No linked list was passed into function')

    fnp = snp.next

    while fnp:
#        print snp.data

        fnp = fnp.next
        if fnp:
            snp = snp.next
            fnp = fnp.next

    return snp


x1.printList()
print 'middle node value = %s' % detectMiddleNodeInOnePass(x1).data

