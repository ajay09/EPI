from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    node = tree
    result = []
    stack = []

    while stack or node:
        while node:
            result.append(node.data)
            stack.append(node)
            node = node.left
        node = stack.pop().right

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
