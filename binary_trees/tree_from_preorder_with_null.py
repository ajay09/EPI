import functools
from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


"""
Learnings
Use of iterator or generator:
    Since we need the left most number from the preorder list which has not been consumed we can use iterator or 
    a generator, which would always return the next non-consumed number from the list
"""


# Using generator
def reconstruct_preorder(preorder: List[int]) -> Optional[BinaryTreeNode]:
    def get_next_number_from_preorder(preorder: List[int]):
        for n in preorder:
            yield n

    def helper(preorder_num_gen: iter):
        next_key = next(preorder_num_gen)
        if next_key is None:
            return None

        return BinaryTreeNode(next_key, helper(preorder_num_gen), helper(preorder_num_gen))

    return helper(get_next_number_from_preorder(preorder))


"""
# Using iterator
def reconstruct_preorder(preorder: List[int]) -> Optional[BinaryTreeNode]:
    def helper(preorder_iter: iter):
        next_key = next(preorder_iter)
        if next_key is None:
            return None

        return BinaryTreeNode(next_key, helper(preorder_iter), helper(preorder_iter))

    return helper(iter(preorder))
"""

"""
# Without iterator
def reconstruct_preorder(preorder: List[int]) -> Optional[BinaryTreeNode]:
    def helper(curr_node: int):
        if curr_node > len(preorder) or preorder[curr_node] is None:
            return None, curr_node + 1

        node = BinaryTreeNode(preorder[curr_node])
        next_node = curr_node + 1
        
        node.left, next_node = helper(next_node)
        node.right, next_node = helper(next_node)

        return node, next_node

    return helper(0)[0]
"""

@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
