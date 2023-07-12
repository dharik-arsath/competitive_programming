"""
    Implementation of Binary Search Tree
"""
from typing import Optional, Any

from ds.tree.base import TreeNode
from ds.tree.traversor import TreeTraversor
from ds.tree.utils import as_list


class BST:
    """
        Implements BST...
    """
    def __init__(self, root: TreeNode):
        self.root = root

    def __push(self, node: TreeNode, parent: Optional[TreeNode] = None):
        if parent is None:
            parent = self.root

        if node.data < parent.data:
            if parent.left:
                self.__push(parent= parent.left, node = node)
            else:
                parent.left = node
        elif node.data > parent.data:
            if parent.right:
                self.__push(node, parent= parent.right)
            else:
                parent.right = node
        else:
            raise NotImplementedError("Not Yet Implemented...")

    def push(self, node: TreeNode):
        """
        Inserts a Tree Node. If the same data already exist in tree it won't insert.

        :param node: Tree Node to be inserted
        :return: None
        """
        return self.__push(node, parent = self.root)

    def __get_node(self, parent: TreeNode, element: Any) -> Optional[TreeNode]:
        if parent is None:
            return

        if parent.data == element:
            return parent

        if parent.data > element:
            left = self.__get_node(parent.left, element)
            if left:
                return left

        elif parent.data < element:
            right = self.__get_node(parent.right, element)
            if right:
                return right

    def get_node(self, element: Any) -> Optional[TreeNode]:
        """
        Provides the node if it presents on the tree.
        :param element: Element to search and get corresponding Tree Node
        :return: TreeNode | None
        """
        return self.__get_node(self.root, element)

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

    def __get_depth(self, node: TreeNode):
        if node is None:
            return 0

        left = self.__get_depth(node.left)
        right = self.__get_depth(node.right)

        if left > right:
            return left + 1
        else:
            return right + 1

    def get_depth(self):
        return self.__get_depth(node = self.root)


    def __get_height(self, node: TreeNode):
        if node is None:
            return 0

        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def get_height(self):
        return self.__get_height(node = self.root)


# if __name__ == "__main__":
#     head_node = TreeNode(10)
#     bst  = BST(root = head_node)
#     # bst.push(TreeNode(100))
#     # data = (TreeNode( 30 ), TreeNode( 50 ), TreeNode( 1 ), TreeNode( 32 ), TreeNode( 45 ))
#     data = TreeNode(30), TreeNode(1)
#     list(map(bst.push, data))
#     disp = TreeTraversor()
#     data = as_list(disp.inorder, bst)
#
#
#     bst.get_node(45)
#     bst.get_depth()
#     bst.get_height()
#
    #
    # head_node = TreeNode(200)
    # bst = BST(root=head_node)
    # # bst.push(TreeNode(100))
    # data = (TreeNode(150), TreeNode(300), TreeNode(75), TreeNode(190), TreeNode(100)
    #         ,TreeNode(202), TreeNode(313)
    #         )
    # list(map(bst.push, data))
    # disp = TreeTraversor()
    # data = as_list(disp.inorder, bst)
    #
    # bst.get_height()
