from test_framework import generic_test


def look_and_say(n: int) -> str:
    if n == 1:
        return "1"

    prev_look_and_say_num = look_and_say(n - 1)
    curr_look_and_say_num = []

    for digit in prev_look_and_say_num:
        if len(curr_look_and_say_num) == 0 or curr_look_and_say_num[-1] != digit:
            curr_look_and_say_num.extend([1, digit])
        elif curr_look_and_say_num[-1] == digit:
            curr_look_and_say_num[-2] += 1

    return ''.join([str(entry) for entry in curr_look_and_say_num])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
