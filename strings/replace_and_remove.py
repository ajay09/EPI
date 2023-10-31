import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


"""
Consider the following two rules that are to be applied to an array of characters. 
    - Replace each 'a' by two 'd's.
    - Delete each entry containing a 'b'.
For example, applying these rules to the array (a,c,d,b,b,c,a) results in the array (d,d,c,d,c,d,d).
Write a program which takes as input an array of characters, and removes each 'b' and replaces each 'a'by two 'd's.
"""

"""
Learning:
Always first write a solution that is simple, here don't be afraid to do it in multiple iterations.
A single iteration solution if possible can be devised later.
"""


def replace_and_remove(size: int, s: List[str]) -> int:
    a_count, b_count = 0, 0
    for i in range(size):
        if s[i] == 'a':
            a_count += 1
        elif s[i] == 'b':
            b_count += 1

    new_size = size - b_count + a_count

    write_index = 0
    for read_index in range(size):
        if s[read_index] == 'b':
            continue
        else:
            s[write_index] = s[read_index]
            write_index += 1

    write_index = new_size - 1
    for read_index in range(size - b_count - 1, -1, -1):
        if s[read_index] == 'a':
            s[write_index - 1] = s[write_index] = 'd'
            write_index -= 2
        else:
            s[write_index] = s[read_index]
            write_index -= 1
    return new_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))

    # replace_and_remove(8, ['d','c', 'b', 'b','a','a','d','d'],)
