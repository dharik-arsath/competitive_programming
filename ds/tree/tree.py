"""
    Implementation of Binary Search Tree
"""
from typing import Optional, Any, Callable

from ds.tree.base import TreeNode


class BST:
    """
        Implements BST...
    """
    def __init__(self, root: TreeNode):
        self.root = root

    def push(self, node: TreeNode, parent: Optional[TreeNode] = None):
        """
        Inserts a Tree Node. If the same data already exist in tree it won't insert.

        :param node: Tree Node to be inserted
        :param parent: Root Node of the tree
        :return: None
        """
        if parent is None:
            parent = self.root

        if node.data < parent.data:
            if parent.left:
                self.push(parent= parent.left, node = node)
            else:
                parent.left = node
        elif node.data > parent.data:
            if parent.right:
                self.push(node, parent= parent.right)
            else:
                parent.right = node
        else:
            raise NotImplementedError("Not Yet Implemented...")

    def __get_node(self, parent: TreeNode, element: Any) -> Optional[TreeNode]:
        if parent is None:
            return

        if parent.data == element:
            return parent

        left = self.__get_node(parent.left, element)
        if left:
            return left
            # self.__get_node(parent.left, element)

        right = self.__get_node(parent.right, element)
        if right:
            return right
            # self.__get_node(parent.right, element)
    def get_node(self, element: Any) -> Optional[TreeNode]:
        """
        Provides the node if it presents on the tree.
        :param element: Element to search and get corresponding Tree Node
        :return: TreeNode | None
        """
        return self.__get_node(self.root, element)

    def as_list(self, traversor: Callable[[...], list[TreeNode]], *args, **kwargs) -> list:
        """
        Provides data in the form  of llist
        :param traversor: traversor such as inorder, preorder, postorder
        :return: list of data
        """
        data: list[TreeNode] = traversor(*args, **kwargs)
        if len(data) < 1:
            return data

        data_list = [x.data for x in data]
        return data_list

    def __remove(self, node: TreeNode, parent: Optional[TreeNode]):

        if parent is None:
            return parent

        if node.left is None and node.right is None: # leaf node
            if parent.left is node:
                parent.left = None

            if parent.right is node:
                parent.right = None

        if parent.right is node:
            if node.right is None:
                parent.right = node.left
            elif node.left is None:
                parent.right = node.right

        if parent.left is node:
            if node.left is None:
                parent.left = node.right

            else:
                pass
        left  = self.__remove(node, parent.left)
        if left:
            return left

        right = self.__remove(node, parent.right)
        if right:
            return right

    def remove(self, node: TreeNode):
        """
        Removes a node from tree
        :param node: Node to remove
        :return: None
        """
        return self.__remove(node, parent= self.root)
class TreeTraversor:
    """
    Class that takes responsibility for traversing the given tree.
    """
    def __init__(self):
        self.llist = []

    def __inorder(self, node: TreeNode, data: list[TreeNode]):
        if node.left:
            self.__inorder(node.left, data)

        data.append(node)

        if node.right:
            self.__inorder(node.right, data)

    def __preorder(self, node: TreeNode, data: list[TreeNode]):
        # print(node.data)
        data.append(node)
        if node.left:
            self.__preorder(node.left, data)

        if node.right:
            self.__preorder(node.right, data)

    def __postorder(self, node: TreeNode, data: list[TreeNode]):
        if node.left:
            self.__preorder(node.left, data)
        if node.right:
            self.__preorder(node.right, data)

        # print(node.data)
        data.append(node)

    def inorder(self, tree: BST) -> list[TreeNode]:
        """
        Traverses given tree in in-order.
        :param tree: Tree to traverse in.
        :return: list[TreeNode]
        """
        data: list[TreeNode] = []
        self.__inorder(node=tree.root, data=data)
        return data

    def preorder(self, tree: BST):
        """
        Traverses given tree in pre-order
        :param tree: Tree to traverse in.
        :return: list[TreeNode]
        """
        data: list[TreeNode] = []
        self.__preorder(node=tree.root, data=data)
        return data

    def postorder(self, tree:BST):
        """
        Traverses given tree in post-order
        :param tree: Tree to traverse in.
        :return: list[TreeNode]
        """
        data: list[TreeNode] = []
        self.__postorder(node=tree.root, data=data)
        return data

#
# if __name__ == "__main__":
#     head_node = TreeNode(10)
#     bst  = BST(root = head_node)
#     bst.push(TreeNode(100))
#     data = (TreeNode( 30 ), TreeNode( 50 ), TreeNode( 1 ), TreeNode( 32 ), TreeNode( 45 ))
#     list(map(bst.push, data))
#     disp = TreeTraversor()
#     data = bst.as_list(disp.inorder, bst)
