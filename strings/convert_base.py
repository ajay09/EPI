from epi_judge_python.test_framework import generic_test

"""
Write a program that performs base conversion. The input is a string, an integer b1, and another integer b2. 
The string represents an integer in base b1. The output should be the string representing the integer in base b2. 
Assume 2 < b1,b2 < 16. Use "A' to represent 10, "B" for 11,..., and "F" for 15. 
(For example, if the string is "615", b1 is 7 and b2 is 13, then the result should be "1A7", 
since 6x7^2 + 1x7 + 5 = 1x13^2 + 10x13 + 7)
"""


"""
Learning:
We can use a string to convert hexadecimal symbols. 
"""


def convert_num_string_to_int(num_as_string: str, base: int):
    num_as_integer = 0
    symbols_map = {chr(ord('0') + i): i for i in range(10)}
    symbols_map.update({chr(ord('A') + i - 10): i for i in range(10, 16)})
    hex_digits = '0123456789ABCDEF'  # string.hexdigits is a constant = '0123456789abcdefABCDEF'
#   ``````````````````````````````

    for i in range(len(num_as_string)):
        num_as_integer = num_as_integer * base + symbols_map[num_as_string[i]]
        # num_as_integer = num_as_integer * base + hex_digits.index(num_as_string[i])
#       ````````````````````````````````````````````````````````````````````````````

    return num_as_integer


def convert_to_base(num: int, base: int):
    num_in_base = []
    symbols_map = {i: chr(ord('0') + i) for i in range(10)}
    symbols_map.update({i: chr(ord('A') + i - 10) for i in range(10, 16)})
    hex_digits = '0123456789ABCDEF'  # string.hexdigits is a constant = '0123456789abcdefABCDEF'
#   ```````````````````````````````

    while True:
        # num_in_base.append(symbols_map[num % base])
        num_in_base.append(hex_digits[num % base])
#       ``````````````````````````````````````````
        num = num // base
        if num == 0:
            break

    return ''.join(reversed(num_in_base))


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    is_negative = num_as_string[0] == '-'

    start = 1 if is_negative else 0
    num_as_integer = convert_num_string_to_int(num_as_string[start:], b1)

    return ('-' if is_negative else '') + convert_to_base(num_as_integer, b2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))

