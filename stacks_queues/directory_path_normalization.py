from enum import StrEnum

from test_framework import generic_test


"""
Learning:
This is a tough question to think about test cases, specially condition on line-23 is quite difficult to reason about.
e.g.
What should be the output for ".."?
What should be the output for "../../local"?

"""


class Path(StrEnum):
    FORWARD_SLASH = "/"
    CURRENT_DIR = "."
    PARENT_DIR = ".."


def shortest_equivalent_path(path: str) -> str:
    if len(path) == 0:
        return path

    stack = []
    is_absolute_path = (path[0] == Path.FORWARD_SLASH)

    for token in path.split(Path.FORWARD_SLASH):
        if token == "" or token == Path.CURRENT_DIR:
            continue
        elif token.isalnum():
            stack.append(token)
        elif token == Path.PARENT_DIR:
            if len(stack) == 0 or stack[-1] == Path.PARENT_DIR:
                stack.append(token)
            else:
                stack.pop()

    return (Path.FORWARD_SLASH if is_absolute_path else "") + Path.FORWARD_SLASH.join(stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
