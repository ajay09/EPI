from typing import Iterator, List, NamedTuple

from test_framework import generic_test




def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    class Building(NamedTuple):
        id: int
        height: int

    stack = []

    for id, height in enumerate(sequence):
        if len(stack) == 0:
            stack.append(Building(id, height))
        else:
            if height < stack[-1].height:
                stack.append(Building(id, height))
            else:
                while len(stack) > 0 and stack[-1].height <= height:
                    stack.pop()
                stack.append(Building(id, height))

    return [id[0] for id in reversed(stack)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
