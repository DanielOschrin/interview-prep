# Chapter 12 - Dynamic Programming (pg. 183)
import unittest
from typing import Dict, List, Optional
from unittest import TestCase
from unittest.mock import patch


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


def add_until_100_inefficient(array: List):
    """Problem 1: Optimize this"""
    if len(array) == 0:
        return 0
    if array[0] + add_until_100_inefficient(array[1:]) > 100:
        return add_until_100_inefficient(array[1:])
    else:
        return array[0] + add_until_100_inefficient(array[1:])


def add_until_100_optimized(array: List):
    if len(array) == 0:
        return 0
    # Optimized by ensuring we only recurse once per call
    result_before_adding = add_until_100_optimized(array[1:])
    result_after_adding = result_before_adding + array[0]
    if result_after_adding > 100:
        return result_before_adding
    else:
        return result_after_adding


class AddUntilOneHundredTestCase(TestCase):
    @classmethod
    def get_values(cls):
        return [5, 10, 20, 30, 40]

    def test_inefficient(self):
        with patch(__name__ +
                   '.add_until_100_inefficient',
                   wraps=add_until_100_inefficient) as counter:
            add_until_100_inefficient(self.get_values())
            self.assertEqual(counter.call_count, 63)

    def test_optimized(self):
        with patch(__name__ +
                   '.add_until_100_optimized',
                   wraps=add_until_100_optimized) as counter:
            add_until_100_optimized(self.get_values())
            self.assertEqual(counter.call_count, 6)


if __name__ == '__main__':
    unittest.main()
