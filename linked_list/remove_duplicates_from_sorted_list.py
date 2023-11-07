from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    dummy_head = ListNode(0, L)

    prev_iter = dummy_head
    curr_iter = dummy_head.next

    while curr_iter and curr_iter.next:
        if curr_iter.data == curr_iter.next.data:
            prev_iter.next = curr_iter.next
            curr_iter = curr_iter.next
        else:
            prev_iter = curr_iter
            curr_iter = curr_iter.next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
