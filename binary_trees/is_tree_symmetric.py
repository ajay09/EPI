from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


"""
A binary tree is symmetric if you can draw a vertical line through the root and then the left subtree is the mirror 
image of the right subtree.

Write a program that checks whether a binary tree is symmetric.
"""


def is_symmetric(tree: BinaryTreeNode) -> bool:

    def helper(left_side: BinaryTreeNode, right_side: BinaryTreeNode) -> bool:
        if not left_side and not right_side:
            return True
        if not left_side or not right_side:
            return False

        if left_side.data != right_side.data:
            return False

        return helper(left_side.left, right_side.right) and helper(left_side.right, right_side.left)

    return True if not tree else helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
