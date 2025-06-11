"""
File: closest_number_to_zero.py
Description: This module contains a function to find the closest number to zero in an array.
Author: Gizachew Kassa
Date: 11-06-2025
"""

from typing import List


def findClosestNumber(self, nums: List[int]) -> int:
    """
    Returns the number in the list that is closest to zero.
    If two numbers are equally close, the larger one is returned.

    Time Complexity: O(n)
    - Single pass through the array

    Space Complexity: O(1)
    - Constant extra space used
    """
    min_dist = abs(nums[0])
    current_number = nums[0]

    for num in nums[1:]:
        if abs(num) < min_dist:
            min_dist = abs(num)
            current_number = num
        elif abs(num) == min_dist:
            current_number = max(current_number, num)

    return current_number
