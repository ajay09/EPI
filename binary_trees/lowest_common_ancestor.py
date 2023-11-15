import functools
from typing import Optional, NamedTuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


"""
Design an algorithm for computing the LCA of two nodes in a binary tree in which nodes do not have a parent field.
"""


class LCAData(NamedTuple):
    node0: bool
    node1: bool
    lca: Optional[BinaryTreeNode]


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    def helper(node: BinaryTreeNode) -> LCAData:
        if not node:
            return LCAData(False, False, None)
        if node is node0 and node is node1:
            return LCAData(True, True, node)

        left_data = helper(node.left)
        right_data = helper(node.right)

        if left_data.lca or right_data.lca:
            return LCAData(True, True, left_data.lca or right_data.lca)

        node0_found = (left_data.node0 or right_data.node0) or (node is node0)
        node1_found = (left_data.node1 or right_data.node1) or (node is node1)
        lca = node if node0_found and node1_found else None

        return LCAData(node0_found, node1_found, lca)

    return helper(tree).lca


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
