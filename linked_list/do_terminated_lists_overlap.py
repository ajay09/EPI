import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def get_list_len(linked_list: ListNode) -> int:
        length = 0
        while linked_list:
            linked_list = linked_list.next
            length += 1
        return length

    length_l0 = get_list_len(l0)
    length_l1 = get_list_len(l1)

    longer_list, smaller_list = (l0, l1) if length_l0 > length_l1 else (l1, l0)
    longer_list_iter = longer_list

    for _ in range(abs(length_l1 - length_l0)):
        longer_list_iter = longer_list_iter.next

    smaller_list_iter = smaller_list
    while longer_list_iter and smaller_list_iter and longer_list_iter is not smaller_list_iter:
        longer_list_iter = longer_list_iter.next
        smaller_list_iter = smaller_list_iter.next

    return smaller_list_iter if smaller_list_iter is longer_list_iter else None



@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
