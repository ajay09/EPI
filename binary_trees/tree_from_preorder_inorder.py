from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

"""
Learnings:
How to improve efficiency when we are creating many sub-lists out of the given lists?

The time for list slicing and index manipulation is almost same.
list slicing
Average running time:   33 us
Median running time:     3 us

index manipulation
Average running time:   27 us
Median running time:     3 us
"""


def binary_tree_from_preorder_inorder(preorder: List[int], inorder: List[int]) -> Optional[BinaryTreeNode]:
    node_inorder_index_map = {data: id for id, data in enumerate(inorder)}

    def helper(preorder_start, preorder_end, inorder_start, inorder_end):
        if (preorder_start >= preorder_end) or (inorder_start >= inorder_end):
            return None

        root = BinaryTreeNode(preorder[preorder_start])
        root_index = node_inorder_index_map[root.data]

        lst_len = root_index - inorder_start

        root.left = helper(preorder_start + 1, preorder_start + 1 + lst_len,
                           inorder_start, root_index)
        root.right = helper(preorder_start + 1 + lst_len, preorder_end,
                            root_index + 1, inorder_end)

        return root

    return helper(0, len(preorder), 0, len(inorder))


"""
def binary_tree_from_preorder_inorder(preorder: List[int], inorder: List[int]) -> Optional[BinaryTreeNode]:
    if not preorder and not inorder:
        return None

    root = BinaryTreeNode(preorder[0])
    root_index = inorder.index(root.data)
    root.left = binary_tree_from_preorder_inorder(preorder[1: 1 + root_index], inorder[0: root_index])
    root.right = binary_tree_from_preorder_inorder(preorder[1 + root_index:], inorder[root_index + 1:])

    return root
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
