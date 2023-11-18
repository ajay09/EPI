from typing import NamedTuple

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


"""
Learnings
- Example of tree problem, where the iteration must end at the leaf.
- and the leaf must finish the computation before returning.

- If we even iterated the children of leaves i.e. None nodes then the output will be 0 as the final returned value
  is 0 for None nodes.
  Also for None node, instead of returning 0 if we returned parent_sum + 0, then the output will be double the 
  expected value. e.g.
        A tree with just one node      ,...........(1).............,
                                       'None                       'None 
        
"""


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def helper(node: BinaryTreeNode, parent_sum) -> int:
        if not node:
            return parent_sum + 0
        current_sum = node.data + parent_sum * 2
        # if not node.left and not node.right:
        #     return current_sum
        return helper(node.left, current_sum) + helper(node.right, current_sum)

    return helper(tree, 0)


"""
# Postorder
class SumLeafData(NamedTuple):
    sum: int
    exponent: list[int]


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def helper(node: BinaryTreeNode) -> SumLeafData:
        if not node:
            return SumLeafData(0, [0])
        if not node.left and not node.right:
            return SumLeafData(node.data, [1])

        left_data = helper(node.left)
        right_data = helper(node.right)

        next_exponent = [entry + 1 for entry in left_data.exponent if entry > 0] + [entry + 1 for entry in right_data.exponent if entry > 0]
        current_sum = (sum([(2 ** entry) * node.data for entry in left_data.exponent if entry > 0]) + right_data.sum +
                       sum([(2 ** entry) * node.data for entry in right_data.exponent if entry > 0]) + left_data.sum)

        return SumLeafData(current_sum, next_exponent)

    return helper(tree).sum
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
