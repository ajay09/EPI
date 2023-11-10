from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    bracket_map = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for bracket in s:
        if bracket in bracket_map:
            stack.append(bracket_map[bracket])
        elif (len(stack) == 0) or (stack.pop() != bracket):
            return False

    return (len(stack) == 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
