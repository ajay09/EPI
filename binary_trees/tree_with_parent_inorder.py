from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


"""
Learnings:
Think of stack now just having the previous element and follow the normal inorder traversal.
Once the node is None, we need to find the appropriate parent from the stack.
Since stack now has just one node we need to use the parent pointer to find the appropriate parent.
- if the current node is the left child of its parent, then it means we might have completed the left side so the
   stack should be node.parent
- if the current node is the right child of its parent, then we need to find the top most ancestor whose right might
   have completed
               *  <- This should be on the top of the stack 
              /
             *
            / \
               *
              / \
                 *  <- current node 

"""

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    def get_ancestor_with_right_complete(node1):
        ancestor = node1.parent
        while ancestor and ancestor.parent and ancestor.parent.right is ancestor:
            ancestor = ancestor.parent
        return ancestor

    stack, node = None, tree
    result = []

    while stack or node:
        while node:
            stack = node
            node = node.left
        node = stack
        if node and node.parent and (node.parent.left is node):
            stack = node.parent
        else:
            ancestor_right_complete = get_ancestor_with_right_complete(node)
            stack = ancestor_right_complete and ancestor_right_complete.parent
        result.append(node.data)
        node = node.right

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
