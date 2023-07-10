from dataclasses import dataclass, field
from typing import Any, Protocol, Optional


@dataclass
class TreeNode:
    data: Any
    left: Optional["TreeNode"] = field(default=None)
    right: Optional["TreeNode"] = field(default=None)


class BaseTree(Protocol):
    def push(self, element: TreeNode):
        ...

    def remove(self, element: TreeNode):
        ...


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(0)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3

    n1.as_list()