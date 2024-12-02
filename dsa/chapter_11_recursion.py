# Chapter 11 - Recursion - page 181
import string
import unittest
from typing import List, Union, Optional


def count_characters_in_string_array(arr: List[str]):
    """Problem 1"""
    # Base case
    # once we have counted the last character, arr[1:] will return an empty list, which will return 0
    if len(arr) == 0:
        return 0
    # Count the characters in the first element of the array, then add
    # it to the total with recursion
    return len(arr[0]) + count_characters_in_string_array(arr[1:])


class CountCharactersInStringArrayTest(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(count_characters_in_string_array([]), 0)

    def test_single_string(self):
        self.assertEqual(count_characters_in_string_array(['a']), 1)

    def test_complex_array(self):
        result = count_characters_in_string_array(['ab', 'c', 'def', 'wick'])
        self.assertEqual(result, 10)


def get_evens_in_number_array(arr: List[Union[int, float]], acc: Optional[List[int]] = None):
    """Problem 2"""
    if acc is None:
        acc = []
    # Base case: We have no items in the array to check for evenness, so we return the accumulator
    if len(arr) == 0:
        return acc
    next_number = arr[0]

    if next_number % 2 == 0:
        acc.append(next_number)

    return get_evens_in_number_array(arr[1:], acc)


class GetEvensInNumberArrayTestCase(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(get_evens_in_number_array([]), [])

    def test_array_with_no_evens(self):
        self.assertEqual(get_evens_in_number_array([1, 3, 5.5]), [])

    def test_array_with_only_evens(self):
        self.assertEqual(get_evens_in_number_array([2, 100]), [2, 100])

    def test_array_with_mixed_evens_and_odds(self):
        self.assertEqual(get_evens_in_number_array([5, 2, 300, 7]), [2, 300])


def get_nth_triangular_number(n: int):
    """Problem 3"""
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recurse by adding n to the 'smaller problem', which would start with 1
    # e.g. get_nth_triangular_number(2) would add 2 to get_nth_triangular number(1), which returns 1
    return n + get_nth_triangular_number(n - 1)


class GetNthTriangularNumberTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(get_nth_triangular_number(0), 0)

    def test_one(self):
        self.assertEqual(get_nth_triangular_number(1), 1)

    def test_n(self):
        self.assertEqual(get_nth_triangular_number(2), 3)
        self.assertEqual(get_nth_triangular_number(3), 6)
        self.assertEqual(get_nth_triangular_number(4), 10)
        self.assertEqual(get_nth_triangular_number(7), 28)


def get_first_index_of_x(target: str):
    """Problem 4"""
    # base case - we found it
    if target[0] == 'x':
        return 0
    # We add 1 to the index because we have 'moved' further into the string
    return 1 + get_first_index_of_x(target[1:])


class GetFirstIndexOfXTestCase(unittest.TestCase):
    # def test_empty_string(self):
    #     self.assertEqual(get_first_index_of_x(''), -1)

    # def test_string_with_no_x(self):
    #     self.assertEqual(get_first_index_of_x('abc'), -1)

    def test_string_with_x(self):
        self.assertEqual(get_first_index_of_x('x'), 0)
        self.assertEqual(get_first_index_of_x('xxx'), 0)
        self.assertEqual(get_first_index_of_x('abc x'), 4)
        self.assertEqual(get_first_index_of_x(string.ascii_lowercase), 23)


def find_unique_paths(n_rows: int, n_columns: int):
    """Problem 5"""
    if n_rows == 0 or n_columns == 0:
        return 0
    if n_rows == 1 and n_columns == 1:
        return 1

    # We are breaking the possibilities down into the sum of the two smaller grids we could create
    # by reducing the dimensions by one.
    return find_unique_paths(n_rows - 1, n_columns) + find_unique_paths(n_rows, n_columns - 1)


class FindUniquePathsTestCase(unittest.TestCase):
    def test_one_by_one_grid(self):
        self.assertEqual(find_unique_paths(1, 1), 1)

    def test_one_by_two_grid(self):
        self.assertEqual(find_unique_paths(1, 2), 1)
        self.assertEqual(find_unique_paths(2, 1), 1)

    def test_one_by_long_grid(self):
        self.assertEqual(find_unique_paths(1, 100), 1)

    def test_two_by_two_grid(self):
        self.assertEqual(find_unique_paths(2, 2), 2)

    def test_complex_grid(self):
        self.assertEqual(find_unique_paths(3, 3), 6)
        self.assertEqual(find_unique_paths(3, 7), 28)


if __name__ == '__main__':
    print('hello')
