from ds.queue.queue import Queue
from ds.linkedlist import LinkedList, Node


queue = Queue(LinkedList())

queue.push(Node(3))

queue.pop()

[x.data for x in queue]