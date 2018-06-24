#!/usr/bin/env python

from Stack import Stack

class Myqueue:

    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def add(self, item):
        self.inStack.push(item)

    def remove(self):

        if self.outStack.peek():
            return self.outStack.pop()
        else:
            if self.inStack.peek():
                node = self.inStack.pop()
            else:
                return None

            while node:
                self.outStack.push(node)
                if self.inStack.peek():
                    node = self.inStack.pop()
                else:
                    node = None
            return self.outStack.pop()

myQ = Myqueue()

myQ.add(1)
myQ.add(2)

print myQ.remove()
print myQ.remove()
print myQ.remove()

