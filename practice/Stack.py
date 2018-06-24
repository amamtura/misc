from SingleLinkedListNode import SingleLinkedListNode

class Stack:

    def __init__(self):
        self.top = None

    def pop(self):
        if self.top:
            item = self.top.data
            self.top = self.top.next
            return item
        else:
            raise IndexError('pop from empty stack')

    def push(self, item):
        newTop = SingleLinkedListNode(item)
        newTop.next = self.top
        self.top = newTop

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def empty(self):
        isEmpty = True if self.top is None else False
        return isEmpty

