from dataclasses import dataclass, field
from typing import Any, Protocol, Optional


@dataclass
class TreeNode:
    data: Any
    left: Optional["TreeNode"] = field(default=None)
    right: Optional["TreeNode"] = field(default=None)


class BaseTree(Protocol):
    root: TreeNode

    def push(self, node: TreeNode):
        ...

    def remove(self, node: TreeNode):
        ...

    def get_node(self, element: Any):
        ...

    def get_height(self) -> int:
        ...

    def get_level(self) -> int:
        ...