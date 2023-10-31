import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
Given a string containing a set of words separated by whitespace, we would like to transform it to a string 
in which the words appear in the reverse order. 

For example, "Alice likes Bob" transforms to "Bob likes Alice". We do not need to keep the original string.
Implement a function for reversing the words in a string s.
"""

"""
Learning:
Importance of generators.
"""


def get_space_index(s: list):
    i = 0
    while i < len(s):
        if s[i].isspace():
            yield i
        i += 1
    yield i


def reverse_a_range(s: list, start: int, end: int):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s: list):
    s.reverse()
    word_start_index = 0
    space_index_generator = get_space_index(s)
    while word_start_index < len(s):
        space_index = next(space_index_generator)
        reverse_a_range(s, word_start_index, space_index - 1)
        word_start_index = space_index + 1


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
