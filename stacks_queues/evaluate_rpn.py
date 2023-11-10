from test_framework import generic_test


def evaluate(expression: str) -> int:
    tokens = expression.split(",")
    stack = []

    operation_map = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),
    }

    for token in tokens:
        if token.isnumeric():
            stack.append(int(token))
        else:
            second_operand = stack.pop()
            first_operand = stack.pop()
            stack.append(operation_map[token](first_operand, second_operand))

    return stack[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
