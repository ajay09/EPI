from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity: int) -> None:
        self._entries = [None] * capacity
        self._capacity = capacity
        self._head = self._tail = self._num_of_elements = 0

    def enqueue(self, x: int) -> None:
        if self._num_of_elements < self._capacity:
            self._entries[self._tail] = x
            self._tail = (self._tail + 1) % self._capacity
            self._num_of_elements += 1
        else:
            new_capacity = self._capacity * self.SCALE_FACTOR
            old_queue_size = self.size()
            self._entries = self._entries[self._head:] + self._entries[:self._head]
            self._entries += [None] * (new_capacity - old_queue_size)
            # Resizing using the same queue
            """
            # Resizing using a new queue
            new_queue = []
            for i in range(old_queue_size):
                new_queue.append(self.dequeue())
            new_queue += [None] * (new_capacity - old_queue_size)
            self._entries = new_queue
            """
            self._capacity = new_capacity
            self._head = 0
            self._num_of_elements = self._tail = old_queue_size
            self.enqueue(x)

    def dequeue(self) -> int:
        if self._num_of_elements > 0:
            head_element = self._entries[self._head]
            self._head = (self._head + 1) % self._capacity
            self._num_of_elements -= 1
            return head_element
        else:
            raise Exception("Queue is empty.")

    def size(self) -> int:
        return self._num_of_elements


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
