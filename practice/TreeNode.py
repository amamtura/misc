#N-ary Tree Node
class TreeNode:
  def __init__(self, id, value, childList=None):
    self.id = id
    self.value = value
    if childList is None:
      childList = []
    self.childList = childList

  def addChildren(self, childList):
    self.childList.extend(childList)

  def _print(self):
    print '[self] id: %s, value: %s' % (self.id, self.value)
    if self.childList:
      childListValues = []
      for child in self.childList:
        childListValues.append('%s/%s' % (child.id, child.value))
      print 'childList: %s' % ', '.join(childListValues)

