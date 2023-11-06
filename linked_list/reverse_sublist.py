from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    if L is None or start == finish:
        return L

    sublist_head = dummy_head = ListNode(next=L)
    for i in range(1, start):
        sublist_head = sublist_head.next

    prev_node = sublist_head.next
    curr_node = prev_node.next
    for _ in range(finish - start):
        next_ref = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_ref

    sublist_head.next.next = curr_node
    sublist_head.next = prev_node

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
