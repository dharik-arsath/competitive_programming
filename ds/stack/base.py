from typing import Protocol, Any, Optional


class BaseStack(Protocol):
    def push(self, element: Any): # TODO: CHANGE IT TO ACCEPT NODE OR YOUR CUSTOM DS
        ...

    def pop(self, element: Any):
        ...
