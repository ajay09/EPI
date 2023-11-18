from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    stack = []
    result = []

    node = tree
    # while stack or node:
    #     if node:
    #         stack.append(node)
    #         node = node.left
    #     else:
    #         node = stack.pop()
    #         result.append(node.data)
    #         node = node.right

    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        result.append(stack[-1].data)
        node = stack.pop().right

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
