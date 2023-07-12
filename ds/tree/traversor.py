from ds import Queue
from ds.linkedlist import LinkedList
from ds.tree.base import BaseTree
from ds.tree.base import TreeNode


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

    def inorder(self, tree: BaseTree) -> list[TreeNode]:
        """
        Traverses given tree in in-order.
        :param tree: Tree to traverse in.
        :return: list[TreeNode]
        """
        data: list[TreeNode] = []
        self.__inorder(node=tree.root, data=data)
        return data

    def preorder(self, tree: BaseTree) -> list[TreeNode]:
        """
        Traverses given tree in pre-order
        :param tree: Tree to traverse in.
        :return: list[TreeNode]
        """
        data: list[TreeNode] = []
        self.__preorder(node=tree.root, data=data)
        return data

    def postorder(self, tree: BaseTree) -> list[TreeNode]:
        """
        Traverses given tree in post-order
        :param tree: Tree to traverse in.
        :return: list[TreeNode]
        """
        data: list[TreeNode] = []
        self.__postorder(node=tree.root, data=data)
        return data

    def bfs(self, tree: BaseTree) -> list[TreeNode]:
        """
        Traverses given tree in Breadth First Search.
        :param tree: Tree to traverse in.
        :return: list[TreeNode]
        """
        llist = LinkedList()
        queue = Queue(llist)
        queue.push(tree.root)

        bfs = []
        while len(queue) > 1:
            node_removed = queue.pop()
            print(node_removed.data)
            bfs.append(node_removed)
            if node_removed.left is None:
                continue
            if node_removed.right is None:
                continue

            queue.push(node_removed.left)
            queue.push(node_removed.right)

            print(f"queue is : {[x.data for x in list(llist)] }")

        return bfs
