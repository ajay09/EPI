from copy import copy
from typing import List

from test_framework import generic_test, test_utils


"""
Each digit, apart from 0 and 1, in a phone keypad corresponds to one of three or four letters of the alphabet. 
Since words are easier to remember than numbers, it is natural to ask if a 7 or 10-digit phone number can be represented
 by a word. For example, "2276696" corresponds to "ACRONYM" as well as "ABPOMZN".
 
Write a program which takes as input a phone number, specified as a string of digits, and returns all possible 
character sequences that correspond to the phone number. The cell phone keypad is specified by a mapping that takes a 
digit and returns the corresponding set of characters. The character sequences do not have to be legal words or phrases.

"""


"""
https://austinhenley.com/blog/pythonstringsaremutable.html

CPython is clever. If there are no other references to the string, then it will attempt to mutate the string instead 
of allocating a new one. Though it will sometimes need to resize the buffer if the string grows too big, 
much like C++'s vector or C#'s List.

s = ""
addr = id(s)
reallocs = 0
for i in range(100000):
    s += str(i)
    addrCur = id(s)
    if addr != addrCur:
        reallocs += 1
        addr = addrCur

print(reallocs)

It just requires 48 re-allocations!!
"""


# DFS - Using recursion.
def phone_mnemonic(phone_number: str) -> List[str]:
    keypad_map = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

    # Using List : Average running time:   84 us
    #              Median running time:    13 us
    # def phone_mnemonic_helper(index: int):
    #     if index == len(phone_number):
    #         possible_mnemonics.append(''.join(mnemonic))
    #     else:
    #         for key in keypad_map[int(phone_number[index])]:
    #             mnemonic[index] = key
    #             phone_mnemonic_helper(index + 1)
    #
    # possible_mnemonics, mnemonic = [], ['0'] * len(phone_number)
    #
    # phone_mnemonic_helper(0)

    # Using String : Average running time:   77 us
    #                Median running time:    11 us
    #  Theoretically list should have been faster than string!
    def phone_mnemonic_helper(index: int, mnemonic: str):
        if index == len(phone_number):
            possible_mnemonics.append(mnemonic)
        else:
            for key in keypad_map[int(phone_number[index])]:
                phone_mnemonic_helper(index + 1, mnemonic + key)

    possible_mnemonics = []

    phone_mnemonic_helper(0, '')

    return possible_mnemonics


"""
# BFS
def phone_mnemonic(phone_number: str) -> List[str]:
    if len(phone_number) == 0:
        return []

    keypad_map = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

    # With String
    # Average running time:   68 us
    # Median running time:    11 us

    possible_sequences = ['']
    for digit in phone_number:
        new_sequences = []
        for character in keypad_map[int(digit)]:
            for entry in possible_sequences:
                new_sequences.append(entry + character)
        possible_sequences = new_sequences

    # ----------------------------------------------------------------
    
    # With list
    # Average running time:  128 us
    # Median running time:    18 us

    # possible_sequences = [[]]
    # for digit in phone_number:
    #     new_sequences = []
    #     for character in keypad_map[int(digit)]:
    #         for entry in possible_sequences:
    #             entry_copy = copy(entry)
    #             entry_copy.append(character)
    #             new_sequences.append(entry_copy)
    #     possible_sequences = new_sequences

    return [''.join(entry) for entry in possible_sequences]
"""

''' 
def phone_mnemonic(phone_number: str) -> List[str]:
    if len(phone_number) == 0:
        return []

    possible_sequences = ['']
    keypad_map = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

    """
    for digit in phone_number:
        new_sequences = []
        for character in keypad_map[int(digit)]:
            for entry in possible_sequences:
                new_sequences.append(entry + character)
        possible_sequences = new_sequences
    """
    for digit in phone_number:
        new_sequences = []
        for character in keypad_map[int(digit)]:
            new_sequences.extend([entry + character for entry in possible_sequences])
        possible_sequences = new_sequences

    return possible_sequences
'''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
