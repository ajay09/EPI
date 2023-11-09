from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def get_list_len(L: ListNode) -> int:
    list_len = 0
    while L:
        L = L.next
        list_len += 1
    return list_len

def get_kth_node_from_end(head: ListNode, k: int) -> ListNode:
    first_iter = head.next
    for _ in range(k):
        first_iter = first_iter.next

    second_iter = head
    while first_iter:
        first_iter = first_iter.next
        second_iter = second_iter.next

    return second_iter.next


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    dummy_head = ListNode(next=L)
    list_len = get_list_len(L)

    if not L or (k := k % list_len) == 0:
        return L

    kth_node_from_end = get_kth_node_from_end(dummy_head, k)

    prev_node_to_kth_node = dummy_head
    while prev_node_to_kth_node.next is not kth_node_from_end:
        prev_node_to_kth_node = prev_node_to_kth_node.next

    last_node = L
    while last_node.next:
        last_node = last_node.next

    prev_node_to_kth_node.next = None
    last_node.next = dummy_head.next
    dummy_head.next = kth_node_from_end

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
