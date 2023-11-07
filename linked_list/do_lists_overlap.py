import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(l: ListNode) -> bool:
    slow_iter = fast_iter = l

    while fast_iter and fast_iter.next:
        slow_iter = slow_iter.next
        fast_iter = fast_iter.next.next
        if slow_iter is fast_iter:
            return True

    return False


def get_length(l: ListNode) -> int:
    length = 0
    while l:
        l = l.next
        length += 1
    return length

def overlapping_lists_without_cycles(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    len_l0, len_l1 = get_length(l0), get_length(l1)

    bigger_list, smaller_list = (l0, l1) if len_l0 > len_l1 else (l1, l0)

    for _ in range(abs(len_l0 - len_l1)):
        bigger_list = bigger_list.next

    while bigger_list and bigger_list is not smaller_list:
        bigger_list = bigger_list.next
        smaller_list = smaller_list.next

    return bigger_list

def get_cycle_point(l: ListNode) -> Optional[ListNode]:
    slow_iter = fast_iter = l

    while fast_iter and fast_iter.next:
        slow_iter = slow_iter.next
        fast_iter = fast_iter.next.next
        if slow_iter is fast_iter:
            slow_iter = l
            while slow_iter is not fast_iter:
                slow_iter = slow_iter.next
                fast_iter = fast_iter.next
            return slow_iter

    return None

def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    l0_has_cycle, l1_has_cycle = has_cycle(l0), has_cycle(l1)

    if (not l0_has_cycle) and (not l1_has_cycle):
        return overlapping_lists_without_cycles(l0, l1)
    if l0_has_cycle ^ l1_has_cycle:
        return None

    l0_cycle_point, l1_cycle_point = get_cycle_point(l0), get_cycle_point(l1)

    if l0_cycle_point is l1_cycle_point:
        return l0_cycle_point

    node_iter = l0_cycle_point
    while True:
        node_iter = node_iter.next
        if node_iter is l0_cycle_point:
            return None
        elif node_iter is l1_cycle_point:
            return l1_cycle_point


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
