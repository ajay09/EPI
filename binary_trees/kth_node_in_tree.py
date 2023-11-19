import functools
from typing import Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


def find_kth_node_binary_tree(tree: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:
    node = tree
    while node:
        node_left_subtree_size = node.left.size if node.left else 0
        if k == node_left_subtree_size + 1:
            return node
        elif k <= node_left_subtree_size:
            node = node.left
        else:
            node = node.right
            k = k - (node_left_subtree_size + 1)

    return None



"""
def find_kth_node_binary_tree(tree: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:
    stack = []
    node = tree

    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node
        node = node.right

    return None
"""

@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(functools.partial(find_kth_node_binary_tree, tree,
                                            k))

    if not result:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_node_in_tree.py',
                                       'kth_node_in_tree.tsv',
                                       find_kth_node_binary_tree_wrapper))
