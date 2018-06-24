from SingleLinkedListNode import SingleLinkedListNode

class Stack:

  def __init__(self):
    self.top = None

  def pop(self):
    if self.top:
      item = self.top.data
      self.top = self.top.next
      return item
    return None

  def push(self, item):
    t = SingleLinkedListNode(item)
    t.next = self.top
    self.top = t

  def peek(self):
    if self.top:
      return self.top.data
    return None

  def empty(self):
    isEmpty = True if self.top is None else False
    return isEmpty

