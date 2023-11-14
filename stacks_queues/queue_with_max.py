import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure


class QueueWithMax:
    def __init__(self):
        self._queue = collections.deque()
        self._max_queue = collections.deque()

    def enqueue(self, x: int) -> None:
        self._queue.append(x)
        while len(self._max_queue) > 0 and self._max_queue[-1] < x:
            self._max_queue.pop()
        self._max_queue.append(x)

    def dequeue(self) -> int:
        head = self._queue.popleft()
        if head == self._max_queue[0]:
            self._max_queue.popleft()
        return head

    def max(self) -> int:
        return self._max_queue[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
