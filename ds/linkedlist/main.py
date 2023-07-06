from ds.linkedlist import LinkedList, Node


llist = LinkedList()
llist[0]
llist.get_head()

llist.append(Node(3))

[x.data for x in llist]

for each in llist:
    print(each)