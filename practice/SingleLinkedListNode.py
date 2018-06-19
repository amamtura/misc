#Singly Linked List Node
class SingleLinkedListNode:
  def __init__(self, data):
    self.data = data
    self.next = None

  def printList(self):
    node = self.next
    if node:
      print self.data,
    else:
      print self.data
    node = self.next
    while (node is not None):
      if node.next:
        print node.data,
      else:
        print node.data
      node = node.next

