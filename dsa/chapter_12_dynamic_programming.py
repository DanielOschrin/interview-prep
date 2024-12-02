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


def add_until_100(array: List):
    """Problem 1: Optimize this"""
    if len(array) == 0:
        return 0
    if array[0] + add_until_100(array[1:]) > 100:
        return add_until_100(array[1:])
    else:
        return array[0] + add_until_100(array[1:])


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

    @patch(f'{__name__}.add_until_100',
           wraps=add_until_100)
    def test_inefficient(self, counter):
        self.assertEqual(add_until_100(self.get_values()), 100)
        self.assertEqual(counter.call_count, 63)

    @patch(f'{__name__}.add_until_100_optimized',
           wraps=add_until_100_optimized)
    def test_optimized(self, counter):
        self.assertEqual(add_until_100_optimized(self.get_values()), 100)
        self.assertEqual(counter.call_count, 6)


def golomb(n: int):
    """Problem 2: optimize this with memoization"""
    if n == 1:
        return n
    return 1 + golomb(n - golomb(golomb(n - 1)))


def golomb_memoized(n: int, memo: Dict):
    if n == 1:
        return n
    result = memo.get(n)
    if result is None:
        previous_term = golomb_memoized(n - 1, memo)
        result = 1 + golomb_memoized(
            n - golomb_memoized(previous_term, memo),
            memo
        )
        memo[n] = result
    return memo[n]


class GolombTestCase(TestCase):
    @patch(f'{__name__}.golomb', wraps=golomb)
    def test_inefficient(self, counter):
        self.assertEqual(golomb(5), 3)
        self.assertEqual(counter.call_count, 40)

    @patch(f'{__name__}.golomb_memoized', wraps=golomb_memoized)
    def test_memoized(self, counter):
        self.assertEqual(golomb_memoized(5, {}), 3)
        self.assertEqual(counter.call_count, 13)


if __name__ == '__main__':
    unittest.main()
