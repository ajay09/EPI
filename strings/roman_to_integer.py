from test_framework import generic_test


"""
The Roman numeral representation of positive integers uses the symbols I,V,X,L,C,D,M. Each symbol represents a value,
with I being 1,V being 5,X being l0,L being 50,C being l00, D being 500, and M being 1000.

In this problem we give simplified rules for representing numbers in this system. Specifically, define a string over the 
Roman number symbols to be a valid Roman number string if symbols appear in nonincreasing order, with the following 
exceptions allowed:
    - I can immediately precede V and X. 
    - X can immediately precede L and C. 
    - C can immediately precede D and M.
Back-to-back exceptions are not allowed, e.g.,IXC is invalid, as is CDM.

A valid complex Roman number string represents the integer which is the sum of the symbols
that do not correspond to exceptions; for the exceptions, add the difference of the larger symbol and the smaller symbol

For example, the strings "XXXXXIIIIIIII", "LVIII" and "LIX" are valid Roman number strings representing 59. 
The shortest valid complex Roman number string corresponding to the integer 59 is "LIX".

Write a program which takes as input a valid Roman number string s and returns the integer it corresponds to.
"""


def roman_to_integer(s: str) -> int:
    if len(s) == 0:
        return 0
    roman_numeral_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = roman_numeral_map[s[-1]]

    for i in reversed(range(len(s) - 1)):
        if roman_numeral_map[s[i]] < roman_numeral_map[s[i + 1]]:
            result -= roman_numeral_map[s[i]]
        else:
            result += roman_numeral_map[s[i]]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
