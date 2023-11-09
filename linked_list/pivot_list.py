import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    list_head_equal = ListNode()
    list_head_less = ListNode()
    list_head_greater = ListNode()

    list_head_equal_last_node = list_head_equal
    list_head_less_last_node = list_head_less
    list_head_greater_last_node = list_head_greater

    list_iter = l
    while list_iter:
        next_node = list_iter.next
        if list_iter.data == x:
            list_head_equal_last_node.next = list_iter
            list_head_equal_last_node = list_head_equal_last_node.next
            list_head_equal_last_node.next = None
        elif list_iter.data < x:
            list_head_less_last_node.next = list_iter
            list_head_less_last_node = list_head_less_last_node.next
            list_head_less_last_node.next = None
        else:
            list_head_greater_last_node.next = list_iter
            list_head_greater_last_node = list_head_greater_last_node.next
            list_head_greater_last_node.next = None
        list_iter = next_node

    list_head_equal_last_node.next = list_head_greater.next
    list_head_less_last_node.next = list_head_equal.next

    return list_head_less.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
