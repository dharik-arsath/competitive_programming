from .queue import Queue
from ds.linkedlist import LinkedList, Node
from pytest import fixture
import pytest

@fixture
def obj():
    llist = LinkedList()
    queue = Queue(llist)

    nodes: list[Node] = [ Node(100), Node(200) ]
    for node in nodes:
        queue.push(node)

    return queue


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


def test_pop(obj: Queue):
    data: list = list(obj)
    popped_data = obj.pop()

    assert data[1] == popped_data
