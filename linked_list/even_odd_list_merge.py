from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L

    even_iter = L
    odd_iter = L.next
    odd_list_start = L.next
    even_list_start = L

    while odd_iter and odd_iter.next:
        even_iter.next = even_iter.next.next
        odd_iter.next = odd_iter.next.next
        even_iter = even_iter.next
        odd_iter = odd_iter.next

    even_iter.next = odd_list_start

    return even_list_start


if __name__ == '__main__':
    exit(generic_test.generic_test_main('even_odd_list_merge.py',
                                        'even_odd_list_merge.tsv',
                                        even_odd_merge))
