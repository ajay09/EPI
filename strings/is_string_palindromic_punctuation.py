from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    forward_index = 0
    back_index = len(s) - 1

    while forward_index < back_index:
        if not s[forward_index].isalnum():
            forward_index += 1
        elif not s[back_index].isalnum():
            s[back_index].capitalize()
            back_index -= 1
        elif s[forward_index].lower() != s[back_index].lower():
            return False
        else:
            forward_index += 1
            back_index -= 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
