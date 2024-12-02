# Chapter 12 - Dynamic Programming (pg. 183)
from typing import Dict, Optional
from unittest import TestCase


def get_nth_fibonacci(n: int, memo: Optional[Dict] = None):
    # Base case
    if n < 2:
        return n
    if memo is None:
        memo = {}

    # Check to see if we have already calculated the result
    result = memo.get(n)

    if result is None:
        # If not, calculate it. However, each call now checks for memoized
        # result, instead of spawning a ton of child recursive calls
        result = get_nth_fibonacci(n - 1) + get_nth_fibonacci(n - 2)
        memo[n] = result

    return result


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
