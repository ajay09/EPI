from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""
Implement an integer to string conversion function, and a string to integer conversison function, 
For example, if the input to the first function is the integer 314,it should retum the string "31.4" 
and if the input to the second function is the string "314" it should return the integer 314.
"""

"""
Learning:
Think of basic test cases:
1, "1"
0, "0"
10, "10"
-10, "-10"
"""


def int_to_string(x: int) -> str:
    is_negative = x < 0
    if is_negative:
        x = -x
    
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
#                    ````````
        x = x // 10
        if x == 0:
#          ``````
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))
#                                                 ```````````
#          ```````````````````````````    ````````````````````


def string_to_int(s: str) -> int:
    is_negative = True if s[0] == '-' else False

    num = 0
    start = 1 if s[0] == '-' or s[0] == '+' else 0
#   ``````````
    for i in range(start, len(s)):
        num = num * 10 + int(s[i])

    return (-1 if is_negative else 1) * num
#          ``````````````````````````


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
