import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


"""
Given a binary tree, compute a linked list from the leaves of the binary tree. 
The leaves should appear in left-to-right order.
"""


"""
Learnings:
    Good example of completing the left task and right task recursively and the combining the results
"""


def create_list_of_leaves_recursive(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    if tree is None:
        return []
    if tree.left is None and tree.right is None:
        return [tree]
    return create_list_of_leaves_recursive(tree.left) + create_list_of_leaves_recursive(tree.right)


def create_list_of_leaves(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    stack, result = [], []
    node = tree

    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if node.left is None and node.right is None:
            result.append(node)
        node = node.right

    return result
    # return create_list_of_leaves_recursive(tree) or result

@enable_executor_hook
def create_list_of_leaves_wrapper(executor, tree):
    result = executor.run(functools.partial(create_list_of_leaves, tree))

    if any(x is None for x in result):
        raise TestFailure('Result list can\'t contain None')
    return [x.data for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_connect_leaves.py',
                                       'tree_connect_leaves.tsv',
                                       create_list_of_leaves_wrapper))
