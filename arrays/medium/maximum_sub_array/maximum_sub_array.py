"""
File: maximum_sub_array.py

Description: Finds the contiguous subarray within a one-dimensional array of numbers which has the largest sum.

Author: Gizachew Kassa
Date: 27/04/2025
"""

from typing import List


def maxSubArray(self, nums: List[int]) -> int:
    """
    Finds the contiguous subarray with the largest sum in a given integer array.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Returns:
        int: The maximum sum of the contiguous subarray.

    """
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
