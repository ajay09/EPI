from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def helper(node: BinaryTreeNode) -> (bool, int):
        if node is None:
            return True, 0

        is_left_balanced, left_height = helper(node.left)
        is_right_balanced, right_height = helper(node.right)

        return (is_left_balanced and is_right_balanced and (abs(left_height - right_height) <= 1)), max(left_height,
                                                                                                        right_height) + 1

    return helper(tree)[0]




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
