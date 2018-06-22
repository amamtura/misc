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

n5.leftChild = n1
n5.rightChild = n6

n1.leftChild = n0
n1.rightChild = n3

n3.leftChild = n2
n3.rightChild = n4

n6.rightChild = n8

n8.leftChild = n7

n5.printTree()


# traversal = 0: Pre-order
#             1: In-order
#             2: Post-order
def serialize(root, traversal):

  if root is None: # recursion exit condition
    return '-'
  else:
    if traversal == 0:
      return root.value + serialize(root.leftChild, traversal) + serialize(root.rightChild, traversal) # return concat string
    elif traversal == 1:
      return serialize(root.leftChild, traversal) + root.value + serialize(root.rightChild, traversal)
    elif traversal == 2:
      return serialize(root.leftChild, traversal) + serialize(root.rightChild, traversal) + root.value

serialized = serialize(n5,0)
print serialized

