from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


"""
Again a problem where the iteration should conclude at leaf node.
"""


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    def helper(node, path_sum, remaining_weight) -> bool:
        if not node:
            return False
        path_sum += node.data
        if node.right == node.left == None:
            return path_sum == remaining_weight
        return helper(node.left, path_sum, remaining_weight) or helper(node.right, path_sum, remaining_weight)

    return helper(tree, 0, remaining_weight)


"""
def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    def helper(node, path_sum, remaining_weight) -> bool:
        if not node:
            return False
        path_sum += node.data
        if node.right == node.left == None:
            return path_sum == remaining_weight
        return helper(node.left, path_sum, remaining_weight) or helper(node.right, path_sum, remaining_weight)

    return helper(tree, 0, remaining_weight)
"""


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
