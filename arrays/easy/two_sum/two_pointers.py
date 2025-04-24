"""
File: two_pointers.py
Description: This module contains a two pointers solution to the Two Sum problem.
Author: Gizachew Kassa
Date: 2025-04-25
"""

from typing import List, Optional


def two_number_sum_two_pointers(array: List[int], target: int) -> Optional[List[int]]:
    """
    Returns two distinct numbers from the array that add up to the target.

    This two pointers approach sorts the array and uses two pointers to find the pair.
    It starts with one pointer at the beginning and another at the end of the sorted array.

    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(1)

    Returns:
        A list containing the two numbers, or an empty list if no valid pair exists.
    """
    array.sort()
    left, right = 0, len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target:
            return [array[left], array[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
