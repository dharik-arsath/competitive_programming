from .linked_list import LinkedList, Node
from pytest import fixture
import pytest
from .exceptions import OutOfBound

@fixture
def obj():
    llist = LinkedList()

    nodes: list[Node] = [ Node(100), Node(200), Node(300), Node(400), Node(500), Node(600) ]
    for node in nodes:
        llist.append(node)

    return llist


def test_append_pass(obj):
    node_to_append = Node(100)
    obj.append(node_to_append)

    data: list = list(obj)
    assert data[-1] == node_to_append


def test_append_multi(obj):
    append_nodes = [Node(300), Node(300), Node(300)]
    for node in append_nodes:
        obj.append(node)

    data: list = list(obj)
    assert data[-1] == append_nodes[-1]
    assert data[-2] == append_nodes[-2]
    assert data[-3] == append_nodes[-3]

# def test_insert_at_head(obj):
#     node_to_insert_first = Node(10)
#     obj.insert_at_head(node_to_insert_first)
#
#     new_head = obj.get_head()
#
#     assert node_to_insert_first == new_head
#
def test_goto(obj):
    first_ele = obj[0]
    head_ele  = obj.get_head()

    assert first_ele == head_ele


def test_insertion(obj):
    obj.append(Node(300))
    obj.append(Node(400))
    obj.append(Node(500))
    obj.append(Node(500))
    # obj.append(node_to_insert)
    # obj.append(node_to_insert)
    # obj.append(node_to_insert)

    new_node = Node(1002323)

    insert_index = 2
    obj.insert(new_node, index = insert_index)

    llist: list = list(obj)
    print( [x.data for x in llist] )
    assert llist[insert_index] == new_node


def test_pop(obj):
    data: list = list(obj)
    popped_data = obj.pop()

    assert data[-1] == popped_data


def test_remove(obj):
    data: list = list(obj)
    obj.remove(2)
    new_data: list = list(obj)

    assert data[2] != new_data[2]

