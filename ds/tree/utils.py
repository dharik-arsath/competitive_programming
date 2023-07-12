from typing import Callable

from ds.tree.base import TreeNode


def as_list(traversor: Callable[[...], list[TreeNode]], *args, **kwargs) -> list:
    """
    Provides data in the form  of llist
    :param traversor: traversor such as inorder, preorder, postorder
    :return: list of data
    """
    data: list[TreeNode] = traversor(*args, **kwargs)
    data_list = [x.data for x in data]
    return data_list
