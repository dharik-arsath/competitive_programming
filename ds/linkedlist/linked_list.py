"""
    Doubly Linked List Implementation by Dharik Arsath

    Date: 05.07.2023
    Time: 4:32 PM
"""
from typing import Optional
from ds.linkedlist import Node
from ds.linkedlist.exceptions import EmptyList, OutOfBound, ImmutableError
from ds.base import BaseDS


class LinkedList(BaseDS):
    def __init__(self):
        start_node  = Node(data = None)
        self.__head = start_node
        self.__tail = start_node

        self.__len  = 1

    def __iter__(self):
        self.iter_cnt = 0
        return self

    def __next__(self):
        if self.iter_cnt >= self.__len:
            raise StopIteration

        data = self.__getitem__(self.iter_cnt)
        # data = self.at( self.iter_cnt )
        self.iter_cnt += 1
        return data

    def __len__(self):
        return self.__len

    def __getitem__(self, index: int):
        element = self.__goto(index)
        return element

    def __goto(self, index: int):
        if index > self.__len - 1:
            raise OutOfBound(f"Cannot access element at {index}, try index within {self.__len - 1}")
        iter_ptr = self.__head
        counter_indx = 0
        while iter_ptr.next is not None and counter_indx < index:
            counter_indx += 1
            iter_ptr = iter_ptr.next

        if counter_indx == index:
            return iter_ptr

    def get_head(self) -> Node:
        return self.__head

    def get_tail(self) -> Node:
        return self.__tail

    def append(self, node: Node) -> None:
        self.insert(node, index = self.__len)

    def insert(self, node: Node, index: int) -> None:
        """
        :param node: Node to insert
        :param index: 0 based indexed position.
        :return: None
        """
        if index > self.__len  or index < 0:
            raise OutOfBound(f"Cannot Insert Element at {index}, try index within {self.__len - 1}")

        if index == 0:
            raise ImmutableError("Head Node cannot be mutated...")

        iter_ptr = self.__goto(index - 1)

        if iter_ptr is not None:
            node.next = iter_ptr.next
            iter_ptr.next = node
            node.prev = iter_ptr
            self.__len += 1
            self.__tail = node

    def pop(self) -> Node:
        if self.__len <= 1:
            raise EmptyList("Head Node cannot be removed...")

        iter_ptr        = self.__head
        while iter_ptr.next is not None and iter_ptr.next.next is not None:
            iter_ptr    = iter_ptr.next

        popped_data     = iter_ptr.next
        iter_ptr.next   = None
        self.__len        -= 1
        self.__tail     = iter_ptr

        return popped_data

    def remove(self, position: int) -> Node:
        if position == 0:
            raise ImmutableError("Head Node Cannot be removed...")

        if position > self.__len__() - 1:
            raise OutOfBound(f"Cannot Access Element at position {position}...")

        iter_ptr = self.__goto(position - 1)
        removable_element = iter_ptr.next
        iter_ptr.next = iter_ptr.next.next

        self.__len -= 1
        return removable_element
