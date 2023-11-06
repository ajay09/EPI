from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    if L is None or start == finish:
        return L
    dummy_head = ListNode(next=L)

    node_before_start = dummy_head
    for i in range(1, start):
        node_before_start = node_before_start.next

    start_node = node_before_start.next
    prev_node = start_node
    curr_node = start_node.next
    while start < finish and curr_node:
        next_ref = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_ref
        start += 1

    start_node.next = curr_node
    node_before_start.next = prev_node

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
