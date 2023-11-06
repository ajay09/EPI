import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


"""
Although a linked list is supposed to be a sequence of nodes ending in null, it is possible to create a cycle in a 
linked list by making the next field of an element reference to one of the earlier nodes.
Write a program that takes the head of a singly linked list and retums null if there does not exist a cycle, and the 
node at the start of the cycle, if a cycle is present, (You do not know the length of the list in advance.)
"""

"""
Learning:
    - Use "is" to compare references
    - To find the starting point of the cycle there are 2 methods.
        1- After finding the cycle take a pointer at the head and move the slow_ptr and this new pointer
           one step at a time and they will meet at the starting point of the cycle
        2- Or, first calculate the length of the cycle. Let n = cycle_length
           Now take a pointer and move it n times on the list. This pointer will traverse
           x distance on the non-cycle part and y distance on the cycle part. Thus x + y = n
           Now take another pointer at the head and start moving this and the previous pointer one step
           at a time, they will meet at the starting point of they cycle.  
"""


def find_cycle_start(head, fast_iter):
    slow_iter = head

    while slow_iter is not fast_iter:
        slow_iter = slow_iter.next
        fast_iter = fast_iter.next

    return slow_iter


def get_cycle_len(slow_iter, fast_iter):
    cycle_len = 1
    fast_iter = fast_iter.next

    while slow_iter is not fast_iter:
        cycle_len += 1
        fast_iter = fast_iter.next

    return cycle_len


def find_cycle_start2(head, slow_iter, fast_iter):
    cycle_len = get_cycle_len(slow_iter, fast_iter)

    slow_iter = head
    while cycle_len > 0:
        slow_iter = slow_iter.next
        cycle_len -= 1

    fast_iter = head
    while slow_iter is not fast_iter:
        slow_iter = slow_iter.next
        fast_iter = fast_iter.next

    return slow_iter


def has_cycle(head: ListNode) -> Optional[ListNode]:
    slow_iter = head
    fast_iter = head

    while fast_iter and fast_iter.next:
        slow_iter = slow_iter.next
        fast_iter = fast_iter.next.next
        if slow_iter is fast_iter:
            return find_cycle_start2(head, slow_iter, fast_iter)

    return None


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
