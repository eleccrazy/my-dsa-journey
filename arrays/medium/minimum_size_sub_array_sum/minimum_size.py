"""
File: minimum_size.py
Description: Find the minimal length of a contiguous subarray of which the sum is at least k.
Author: Gizachew Kassa
Date: 11-05-2025
"""

from typing import List


def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    """
    Returns the minimal length of a contiguous subarray
    with a sum >= target. If no such subarray exists, returns 0.

    Uses a sliding window to track the current window sum and
    adjusts the window size to find the shortest valid subarray.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    window_sum = 0
    min_length = float("inf")

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return min_length if min_length != float("inf") else 0
