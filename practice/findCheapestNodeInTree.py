#!/usr/bin/env python

from TreeNode import TreeNode


def _assignChildlistLessSelf(tnode, allNodes):
    allNodesCopy = allNodes[:]
    allNodesCopy.remove(tnode)
    tnode.addChildren(allNodesCopy)

tnodeA = TreeNode('A', 8)
tnodeB = TreeNode('B', 2)
tnodeC = TreeNode('C', 3)
tnodeJ = TreeNode('J', 6)
tnodeF = TreeNode('F', 3)
tnodeH = TreeNode('H', 1)

allNodes = [tnodeA, tnodeB, tnodeC, tnodeJ, tnodeF, tnodeH]

# WORST CASE, i.e. where every node has a connection to every other -> graph
_assignChildlistLessSelf(tnodeA, allNodes)
_assignChildlistLessSelf(tnodeB, allNodes)
_assignChildlistLessSelf(tnodeC, allNodes)
_assignChildlistLessSelf(tnodeJ, allNodes)
_assignChildlistLessSelf(tnodeF, allNodes)
_assignChildlistLessSelf(tnodeH, allNodes)

tnodeA._print()
tnodeB._print()
tnodeC._print()
tnodeJ._print()
tnodeF._print()
tnodeH._print()
print ''


def findCheapestByWalkingFullTree(node, minNode=None, visited=None, visitCount=0):
    if visited is None:
        visited = [ node ]
        minNode = node

    print 'processing node %s' % node.id
    visitCount += 1
    visited.append(node)

    if node.value < minNode.value:
        print 'updating min value (%s) node to be %s ' % (node.value, node.id)
        minNode = node

    for item in node.childList:
        if item not in visited:
            minNode, visitCount = findCheapestByWalkingFullTree(item, minNode, visited, visitCount)

    return minNode, visitCount


cheapestNode, visitCount = findCheapestByWalkingFullTree(tnodeA)
print '\nCheapest node found:'
cheapestNode._print()
print 'visitCount %d' % visitCount

