from test_framework import generic_test


"""
The look-and-say sequence starts with 1. Subsequent numbers are derived by describing the previous number in terms of 
consecutive digits. Specifically, to generate an entry of the sequence from the previous entry, read off the digits of 
the previous entry, counting the number of digits in grouPs of the same digit. 
For example, 1; one 1; two 1s; one 2 then one 1; one 1, then one 2, then two 1s; three 1s, then two 2s, then one 1. 
The first eight numbers in the look-and-say sequence are <'t, 1.1., 21, 1211, 111221, 31221.1., 13112227, 1113213211> .

Write a Program that takes as input an integer r and returns the nth integer in the look-and-say sequence. 
Return the result as a string.
"""


def get_next_num(num: str):
    if num == "1":
        yield "1"

    while True:
        next_num = []
        i = 0
        while i < len(num):
            count = 1
            curr_digit = num[i]
            while i + 1 < len(num) and curr_digit == num[i + 1]:
                i += 1
                count += 1
            next_num.append(str(count))
            next_num.append(curr_digit)
            i += 1
        result = ''.join(next_num)
        yield result
        num = result


# Iterative
def look_and_say(n: int) -> str:
    result = ""
    look_and_say_gen = get_next_num(str(1))

    for i in range(n):
        result = next(look_and_say_gen)

    return result


# Recursive
# def look_and_say(n: int) -> str:
#     if n == 1:
#         return "1"
#
#     prev_look_and_say_num = look_and_say(n - 1)
#     curr_look_and_say_num = []
#
#     for digit in prev_look_and_say_num:
#         if len(curr_look_and_say_num) == 0 or curr_look_and_say_num[-1] != digit:
#             curr_look_and_say_num.extend([1, digit])
#         elif curr_look_and_say_num[-1] == digit:
#             curr_look_and_say_num[-2] += 1
#
#     return ''.join([str(entry) for entry in curr_look_and_say_num])


if __name__ == '__main__':
    print(look_and_say(3))
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
