from typing import NamedTuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


"""
Keep the named tuple definition outside the final function, as keeping inside the function would increase
the running time.
If kept inside the Named Tuple class definition will be created everytime the function is called.
"""


class BalancedStatusWithHeight(NamedTuple):
    is_balanced: bool
    height: int


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def helper(node: BinaryTreeNode) -> BalancedStatusWithHeight:
        if node is None:
            return BalancedStatusWithHeight(True, 0)

        is_left_balanced, left_height = helper(node.left)
        is_right_balanced, right_height = helper(node.right)

        return BalancedStatusWithHeight((is_left_balanced and is_right_balanced and
                                        (abs(left_height - right_height) <= 1)), max(left_height, right_height) + 1)


    return helper(tree).is_balanced




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
