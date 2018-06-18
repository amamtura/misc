#Binary Tree Node
class BinaryTreeNode:
  def __init__(self, value, leftChild=None, rightChild=None):
    self.value = value
    self.leftChild = leftChild
    self.rightChild = rightChild

  def _print(self):
    print 'self: %s' % self.value
    if self.leftChild:
      print 'lc: %s' % self.leftChild.value
    if self.rightChild:
      print 'rc: %s' % self.rightChild.value

  def printTree(self):
    if self is None:
      return
    self._print()
    if self.leftChild:
      self.leftChild.printTree()
    if self.rightChild:
      self.rightChild.printTree()

