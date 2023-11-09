from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    result_head = ListNode()
    result_iter = result_head

    carry = 0
    while L1 or L2 or carry != 0:
        node_sum = (L1.data if L1 else 0) + (L2.data if L2 else 0) + carry
        carry = node_sum // 10
        result_iter.next = ListNode(node_sum % 10)
        result_iter = result_iter.next
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None

    return result_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
