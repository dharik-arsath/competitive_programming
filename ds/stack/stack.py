from ds.linkedlist import LinkedList, Node
from typing import Any, Optional
from ds.base import BaseDS


class Stack:
    def __init__(self, base_ds: BaseDS):
        self.__base_ds = base_ds
        self.__len     = 1

    def __iter__(self):
        self.__iter_cnt     = 0
        return self

    def __next__(self):
        if self.__iter_cnt > self.__len__() - 1:
            raise StopIteration

        data = self.__getitem__(self.__iter_cnt)
        self.__iter_cnt += 1
        return data

    def __len__(self):
        return self.__len

    def __getitem__(self, index: int):
        # return self.__base_ds.at(index)
        return self.__base_ds[index]

    def pop(self):
        res = self.__base_ds.pop()
        self.__len -= 1
        return res

    def push(self, element: Any):
        res = self.__base_ds.append(element)
        self.__len += 1
        return res
