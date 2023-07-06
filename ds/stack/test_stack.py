from .stack import Stack
from ds.linkedlist import LinkedList, Node
from pytest import fixture
import pytest

from ..linkedlist.exceptions import EmptyList


@fixture
def obj():
    llist     = LinkedList()
    stack = Stack(base_ds= llist)
    return stack


def test_append_pass(obj):
    node_to_append = Node(100)
    obj.push(node_to_append)

    data: list = list(obj)
    assert data[-1] == node_to_append


def test_append_multi(obj):
    append_nodes = [Node(300), Node(300), Node(300)]
    for node in append_nodes:
        obj.push(node)

    data: list = list(obj)
    assert data[-1] == append_nodes[-1]
    assert data[-2] == append_nodes[-2]
    assert data[-3] == append_nodes[-3]


def test_pop_fail(obj):
    with pytest.raises(EmptyList):
        popped_data = obj.pop()


def test_pop_pass(obj):
    obj.push(Node(100))

    data = list(obj)
    assert data[-1] == obj.pop()
