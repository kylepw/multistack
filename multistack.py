"""
    multistack.py
    ~~~~~~~~~~~~~

    Example of multiple stacks in one list (array).

    Usage:
    >>> s = MultiStack(num=4, size=4)
    >>> s.push(stack=1, value=35)
    >>> s.push(1, 10)
    >>> s.push(0, 2)
    >>> s.push(2, -33)
    >>> s.peek(stack=1)
    10
    >>> s.pop(stack=2)
    -33
    >>> print(s)
    [None, None, None, 2, None, None, 10, 35, None, None, None, None, None, None, None, None]
"""

import random
import unittest

class MultiStack:
    """`num` number of stacks in one array of `size` size"""
    def __init__(self, num=None, size=None):
        self.num = num or 3
        self.size = size or 3
        self._array = [None] * self.num * self.size
        self._val_count = [0] * self.size
        self._mins = [[] for _ in range(self.num)]

    def __str__(self):
        return str(self._array)

    def _get_top_index(self, stack):
        if stack >= self.num:
            return
        if self.is_empty(stack):
            offset = self.size - 1
        else:
            offset = self.size - self._val_count[stack]
        return stack * self.size + offset

    def peek(self, stack):
        if self._val_count[stack] > 0:
            return self._array[self._get_top_index(stack)]
        else:
            return None

    def push(self, stack, value):
        if self.is_full(stack):
            raise ValueError('Stack %s is full.', stack)
        if self.is_empty(stack):
            index = self._get_top_index(stack)
        else:
            index = self._get_top_index(stack) - 1
        self._array[index] = value
        if not self._mins[stack] or value < self._mins[stack][-1]:
            self._mins[stack].append(value)
        self._val_count[stack] += 1

    def pop(self, stack):
        if self.is_empty(stack):
            raise ValueError('Stack %s is empty', stack)
        value = self._array[self._get_top_index(stack)]
        self._array[self._get_top_index(stack)] = None
        if self._mins[stack] and self._mins[stack][-1] == value:
            self._mins[stack].pop()
        self._val_count[stack] -= 1
        return value

    def min(self, stack):
        if len(self._mins) > stack:
            return self._mins[stack][-1] if self._mins[stack] else None

    def is_empty(self, stack):
        return True if self._val_count[stack] == 0 else False

    def is_full(self, stack):
        return True if self._val_count[stack] >= self.size else False


class TestMultiStack(unittest.TestCase):
    def setUp(self):
        # `N` stacks of size `N`
        N = 4
        self.s = MultiStack(num=N, size=N)

        for i in range(N):
            # Leave a space in each stack empty
            for j in range(N-1):
                self.s.push(i, random.randint(10, 100))

    def test_push(self):
        for stack in range(self.s.num):
            self.assertFalse(self.s.is_empty(stack))
            self.assertFalse(self.s.is_full(stack))

        for stack in range(self.s.num):
            val = random.randint(10, 100)
            self.s.push(stack, val)
            self.assertEqual(self.s.peek(stack), val)

        for stack in range(self.s.num):
            with self.assertRaises(ValueError):
                self.s.push(stack, -1)

    def test_pop(self):
        for stack in range(self.s.num):
            top = self.s.peek(stack)
            self.assertEqual(self.s.pop(stack), top)
            self.assertNotEqual(self.s.peek(stack), top)

        for stack in range(self.s.num):
            with self.assertRaises(ValueError):
                for _ in range(self.s.size):
                    self.s.pop(stack)

    def test_min(self):
        for stack in range(self.s.num):
            m = self.s.min(stack)
            values = []
            print(self.s._array)
            while self.s.peek(stack):
                values.append(self.s.pop(stack))
            self.assertEqual(m, min(values))

if __name__ == '__ main__':
    unittest.main()

