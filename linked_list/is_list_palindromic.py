from list_node import ListNode
from test_framework import generic_test


def reverse_list(L):
    dummy_head = ListNode(next=L)
    curr_iter = L
    prev_iter = dummy_head

    while curr_iter:
        next_node = curr_iter.next
        curr_iter.next = prev_iter
        prev_iter = curr_iter
        curr_iter = next_node

    dummy_head.next.next = None
    dummy_head.next = prev_iter

    return dummy_head.next

def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L or not L.next:
        return True

    slow_iter = fast_iter = L

    prev_to_slow_iter = slow_iter
    while fast_iter and fast_iter.next:
        prev_to_slow_iter = slow_iter
        slow_iter = slow_iter.next
        fast_iter = fast_iter.next.next

    prev_to_slow_iter.next = None
    first_half = L
    second_half = slow_iter
    if fast_iter is not None:
        second_half = second_half.next

    reversed_second_half = reverse_list(second_half)

    while reversed_second_half and first_half:
        if reversed_second_half.data != first_half.data:
            return False
        reversed_second_half = reversed_second_half.next
        first_half = first_half.next

    return reversed_second_half == first_half == None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
