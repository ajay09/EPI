from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    decoded_string = []

    count = 0
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else:
            decoded_string += [c] * count
            count = 0

    return ''.join(decoded_string)


def encoding(s: str) -> str:
    encoded_string = []

    prev_char = ''
    count = 0
    for i in range(len(s)):
        if s[i] == prev_char:
            count += 1
        else:
            encoded_string.append(str(count))
            encoded_string.append(prev_char)
            count = 1
            prev_char = s[i]

    if count != 0:
        encoded_string.append(str(count))
        encoded_string.append(prev_char)

    return ''.join(encoded_string[1:])


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
