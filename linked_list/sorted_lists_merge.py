from typing import Optional

from list_node import ListNode
from test_framework import generic_test


"""
Learning
Optional[X] is equivalent to  X | None     or     Union[X, None]   
"""


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:

    def extract_first_node(L: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        if L is not None:
            first_node = L
            remaining_list = first_node.next
            first_node.next = None
            return first_node, remaining_list
        return None, None

    merged_list = ListNode(-1, None)
    merged_list_iterator = merged_list

    while L1 and L2:
        if L1.data <= L2.data:
            extracted_node, L1 = extract_first_node(L1)
        else:
            extracted_node, L2 = extract_first_node(L2)
        merged_list_iterator.next = extracted_node
        merged_list_iterator = merged_list_iterator.next

    if L1:
        merged_list_iterator.next = L1
    elif L2:
        merged_list_iterator.next = L2

    return merged_list.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
