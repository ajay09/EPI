import collections
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# BFS with Queue
# def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
#     if tree is None:
#         return []
#
#     tree_depth_order = []
#     bfs_queue = collections.deque()
#     bfs_queue.append(tree)
#
#     while len(bfs_queue) > 0:
#         level_length = len(bfs_queue)
#         curr_level = []
#         for i in range(level_length):
#             node = bfs_queue.popleft()
#             if node:
#                 curr_level.append(node.data)
#                 for child in (node.left, node.right):
#                     if child:
#                         bfs_queue.append(child)
#         if curr_level:
#             tree_depth_order.append(curr_level)
#
#     return tree_depth_order


# BFS with sentinal node
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if tree is None:
        return []

    class SentinalNode:
        pass

    sentinal_node = SentinalNode()
    tree_depth_order = []
    bfs_queue = collections.deque()
    bfs_queue.append(tree)
    bfs_queue.append(sentinal_node)
    level = []

    while len(bfs_queue) > 0:
        node = bfs_queue.popleft()
        if node is not sentinal_node and node is not None:
            level.append(node.data)
            for child in (node.left, node.right):
                if child:
                    bfs_queue.append(child)
        elif node is sentinal_node:
            if level:
                tree_depth_order.append(level)
                level = []
            if len(bfs_queue) > 0:
                bfs_queue.append(sentinal_node)

    return tree_depth_order

"""
# DFS - Level Order Traversal
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    def level_order_traversal(node, level, tree_depth_order) -> None:
        if node is None:
            return
        if level < len(tree_depth_order):
            tree_depth_order[level].append(node.data)
        else:
            tree_depth_order.append([node.data])

        level_order_traversal(node.left, level + 1, tree_depth_order)
        level_order_traversal(node.right, level + 1, tree_depth_order)

    tree_depth_order = []
    level_order_traversal(tree, 0, tree_depth_order)

    return tree_depth_order
"""

"""
#  BFS with list
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    # TODO - you fill in here.
    tree_depth_order = []
    current_level = [tree] if tree else []

    while len(current_level) > 0:
        tree_depth_order.append([node.data for node in current_level])
        next_level = []
        for node in current_level:
            for child in (node.left, node.right):
                if child:
                    next_level.append(child)
        current_level = next_level

    return tree_depth_order
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
