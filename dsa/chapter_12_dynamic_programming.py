# Chapter 12 - Dynamic Programming (pg. 183)
from unittest import TestCase


def get_nth_fibonacci(n: int):
    # Base case
    if n < 0:
        raise ValueError("N cannot be less than 0, got" + n)

    if n < 2:
        return n

    return get_nth_fibonacci(n - 1) + get_nth_fibonacci(n - 2)


class GetNthFibonacciTestCase(TestCase):

    def test_zero(self):
        self.assertEqual(get_nth_fibonacci(0), 0)

    def test_one(self):
        self.assertEqual(get_nth_fibonacci(1), 1)

    def test_fibonacci(self):
        self.assertEqual(get_nth_fibonacci(2), 1)
        self.assertEqual(get_nth_fibonacci(3), 2)
        self.assertEqual(get_nth_fibonacci(4), 3)
        self.assertEqual(get_nth_fibonacci(5), 5)
        self.assertEqual(get_nth_fibonacci(8), 21)
        self.assertEqual(get_nth_fibonacci(10), 55)
