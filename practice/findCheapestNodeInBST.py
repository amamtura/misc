#!/usr/bin/env python

from BinaryTreeNode import BinaryTreeNode

nodeA = BinaryTreeNode(20)
nodeB = BinaryTreeNode(8)
nodeC = BinaryTreeNode(22)
nodeD = BinaryTreeNode(4)
nodeE = BinaryTreeNode(12)
nodeF = BinaryTreeNode(10)
nodeG = BinaryTreeNode(14)

nodeA.leftChild = nodeB
nodeA.rightChild = nodeC

nodeB.leftChild = nodeD
nodeB.rightChild = nodeE

nodeE.leftChild = nodeF
nodeE.rightChild = nodeG

# BST
nodeA.printTree()

def findLeastValueInBST(node):
    print('\nstarting')
    while node.leftChild:
        print('at %s' % node.value)
        node = node.leftChild
    return node

node = findLeastValueInBST(nodeA)
print('\n%s' % node.value)

