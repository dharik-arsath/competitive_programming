from ds.tree import BST, TreeNode, TreeTraversor
from pytest import fixture


@fixture
def bst():
    root = TreeNode(10)
    bstree  = BST(root = root)
    data = (TreeNode( 30 ), TreeNode( 50 ), TreeNode( 1 ), TreeNode( 32 ), TreeNode( 45 ))
    list(map(bstree.push, data))

    return bstree


def test_insert(bst):
    trav = TreeTraversor()
    node = TreeNode(100)
    bst.push(node)

    data = trav.inorder(bst)
    is_inserted = any( filter(lambda x: x == node, data) )
    assert is_inserted is True

#
# def test_removal(bst):
#     ...


def test_removal_leaf(bst):
    node_to_remove = bst.get_node(45)
    bst.remove(node_to_remove)

    trav = TreeTraversor()
    data_in_tree: list[TreeNode] = bst.as_list(trav.inorder, bst)
    expected = [1, 10, 30, 32, 50]

    assert data_in_tree == expected



def test_removal_right_none(bst):
    node_to_remove = bst.get_node(50)
    bst.remove(node_to_remove)

    trav = TreeTraversor()
    data_in_tree: list[TreeNode] = bst.as_list(trav.inorder, bst)
    expected = [1, 10, 30, 32, 45, 50]

    expected.remove(node_to_remove.data)
    assert data_in_tree == expected

    node_to_remove1 = bst.get_node(30)
    bst.remove(node_to_remove1)
    expected.remove(node_to_remove1.data)

    data_in_tree = bst.as_list(trav.inorder, bst)
    assert data_in_tree == expected


def test_removal_left_none(bst):
    node_to_remove = bst.get_node(32)
    bst.remove(node_to_remove)

    trav = TreeTraversor()
    data_in_tree: list[TreeNode] = bst.as_list(trav.inorder, bst)
    expected = [1, 10, 30, 32, 45, 50]

    expected.remove(node_to_remove.data)
    assert data_in_tree == expected


def test_update(bst):
    node = bst.get_node(50)
    node.data = 5000
    trav = TreeTraversor()
    out = bst.as_list(trav.inorder, bst)
    expected = [1, 10, 30, 32, 45, 5000]

    assert out == expected

def test_read(bst):
    node = TreeNode(100)
    bst.push(node)

    trav = TreeTraversor()
    print( [x.data for x in trav.inorder(bst) ] )

    assert node is bst.get_node(100)


def test_inorder(bst):
    trav = TreeTraversor()
    data_in_tree:list[TreeNode] = bst.as_list(trav.inorder, bst)
    expected                    = [1, 10, 30, 32, 45, 50]

    assert data_in_tree == expected


def test_preorder(bst):
    disp = TreeTraversor()
    data_as_list: list           = bst.as_list(disp.preorder, bst)
    expected                     = [10, 1, 30, 50, 32, 45]
    assert data_as_list == expected


def test_postorder(bst):
    disp = TreeTraversor()
    data_as_list: list = bst.as_list(disp.postorder, bst)
    expected = [1, 30, 50, 32, 45, 10]
    assert data_as_list == expected
