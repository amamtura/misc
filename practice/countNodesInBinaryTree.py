#!/usr/bin/env python

from BinaryTreeNode import BinaryTreeNode

n0 = BinaryTreeNode('a')
n1 = BinaryTreeNode('b')
n2 = BinaryTreeNode('c')
n3 = BinaryTreeNode('d')
n4 = BinaryTreeNode('e')
n5 = BinaryTreeNode('f')
n6 = BinaryTreeNode('g')
n7 = BinaryTreeNode('h')
n8 = BinaryTreeNode('i')

n0.leftChild = n1
n0.rightChild = n2

n1.leftChild = n3
n1.rightChild = n4

n2.rightChild = n5

n3.leftChild = n6
n3.rightChild = n7

n6.leftChild = n8

n0.printTree()

print ''
print '              a'
print '         b         c'
print '      d     e    f'
print '   g     h'
print 'i'
print ''

def countNodesInBinaryTree(node):
    if node is None:
        return 0
    else:
        return countNodesInBinaryTree(node.leftChild) +\
                countNodesInBinaryTree(node.rightChild) + 1

print countNodesInBinaryTree(n0)

