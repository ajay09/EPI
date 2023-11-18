from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def postorder_traversal(tree: BinaryTreeNode) -> List[int]:
    node = tree
    stack = []
    result = []
    first = (-1)
    second = (-2)

    while stack or node:
        while node:
            stack.append(node)
            stack.append(first)
            node = node.left
        times = stack.pop()
        node = stack.pop()
        if times is first:
            stack.append(node)
            stack.append(second)
            node = node.right
        elif times is second:
            result.append(node.data)
            node = None

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_postorder.py',
                                       'tree_postorder.tsv',
                                       postorder_traversal))
