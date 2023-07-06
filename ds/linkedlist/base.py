from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class Node:
    data    : Any
    prev    : Optional["Node"] = field(default=None)
    next    : Optional["Node"] = field(default=None)
