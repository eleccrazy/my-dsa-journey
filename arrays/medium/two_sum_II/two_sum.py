"""
File: two_sum.py
Description: This file contains a function to find two numbers in a sorted array that add up to a specific target.
Author: Gizachew Kassa
Date: 28/04/2025
"""

from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    """
    Finds two numbers in a sorted array that add up to a specific target using a two-pointer approach.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(numbers) - 1
    while True:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum > target:
            right -= 1
        else:
            left += 1
