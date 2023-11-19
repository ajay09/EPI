import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def find_left_most_node(node):
        while node and node.left:
            node = node.left
        return node

    def find_parent_successor(node):
        while node:
            if node.parent and node.parent.left is node:
                return node.parent
            node = node.parent
        return node

    if node is None:
        return None
    if node.right is None:
        if node.parent and (node.parent.left is node):
            return node.parent
        else:
            return find_parent_successor(node)
    return find_left_most_node(node.right)


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('successor_in_tree.py',
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))
