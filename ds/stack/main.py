from ds.stack import Stack
from ds.linkedlist import LinkedList, Node


llist = LinkedList()
stack = Stack(llist)
stack.push(Node(100))
stack.pop()

[x.data for x in list(stack) ]