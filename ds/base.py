from abc import ABC, abstractmethod


class BaseDS(ABC):

    def __getitem__(self, index: int):
        ...

    @abstractmethod
    def pop(self):
        ...

    @abstractmethod
    def append(self, element):
        ...

    @abstractmethod
    def remove(self, position: int):
        ...

    @abstractmethod
    def insert(self, element, position: int):
        ...