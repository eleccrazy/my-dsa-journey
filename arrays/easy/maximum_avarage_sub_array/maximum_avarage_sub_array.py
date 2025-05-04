"""
File: maximum_average_sub_array.py
Description: Find the maximum average value of any contiguous subarray of length k.
Author: Gizachew Kassa
Date: 04-05-2025
"""

from typing import List


def findMaxAverage(self, nums: List[int], k: int) -> float:
    """
    Finds the maximum average value of any contiguous subarray of length k
    using an optimized sliding window approach with running sum.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Initial window sum of the first k elements
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Slide the window across the array
    for i in range(k, len(nums)):
        current_sum += nums[i]  # Add the new element
        current_sum -= nums[i - k]  # Remove the element going out of the window
        max_sum = max(max_sum, current_sum)

    return max_sum / k
