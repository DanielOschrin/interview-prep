# Chapter 13 - Recursive Algorithms for Speed (page 200)
import unittest
from typing import List


class QuickSorter:
    @classmethod
    def partition(cls, arr: List[int], index_left: int, index_right: int):
        # Assign the pivot index - for now, always right-most
        index_pivot = index_right
        # Move the right pointer to the left of the pivot
        index_right -= 1
        # Grab the value of the pivot
        pivot_value = arr[index_pivot]
        while True:
            # Move the left pointer to the right as long as it points to a
            # value that is less than the pivot value
            while arr[index_left] < pivot_value:
                index_left += 1

            # Move the right pointer to the left as long as it points to a
            # value that is greater than the pivot value
            while arr[index_right] > pivot_value:
                index_right -= 1

            # Once they have both stopped moving, we check to see whether
            # the left pointer has reached or passed the right pointer. if
            # so, we stop the loop so that we can swap the pivot later on in
            # our code.
            if index_left >= index_right:
                break
            # If the left pointer is still to the left of the right pointer,
            # we swap the values of the left and right pointers
            else:
                arr[index_left], arr[index_right] \
                    = arr[index_right], arr[index_left]

        # Finally, swap the value of the left pointer with the pivot
        arr[index_left], arr[index_pivot] = arr[index_pivot], arr[index_left]
        return index_left


class QuickSorterTestCase(unittest.TestCase):
    # def test_partition_empty_array(self):
    #     arr = []
    #     QuickSorter.partition(arr, 0, 0)
    #     self.assertEqual(arr, [])

    def test_partition_single_element_array(self):
        arr = [1]
        QuickSorter.partition(arr, 0, 0)
        self.assertEqual(arr, [1])

    def test_partition_multi_element_array(self):
        arr = [5, 8, 1, 3, 2]
        next_index = QuickSorter.partition(arr, 0, len(arr) - 1)
        print('arr', arr)
        self.assertEqual(next_index, 1)
        self.assertEqual(arr, [1, 2, 5, 3, 8])


if __name__ == '__main__':
    unittest.main()
