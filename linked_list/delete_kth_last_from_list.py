from typing import Optional

from list_node import ListNode
from test_framework import generic_test


"""
Learning:
This can be done in a single pass
"""

def get_list_len(l: ListNode) -> int:
    list_len = 0
    while l:
        l = l.next
        list_len += 1
    return list_len

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last_multiple_pass(L: ListNode, k: int) -> Optional[ListNode]:
    list_len = get_list_len(L)

    dummy_head = ListNode(next=L)

    prev_iter = dummy_head
    node_iter = L
    for _ in range(list_len - k):
        prev_iter = node_iter
        node_iter = node_iter.next

    prev_iter.next = prev_iter.next.next

    return dummy_head.next


def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    """
    Single pass solution
    """
    first_iter = L
    for _ in range(k):
        first_iter = first_iter.next

    dummy_head = ListNode(0, L)
    second_iter = dummy_head
    while first_iter:
        second_iter = second_iter.next
        first_iter = first_iter.next

    second_iter.next = second_iter.next.next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
