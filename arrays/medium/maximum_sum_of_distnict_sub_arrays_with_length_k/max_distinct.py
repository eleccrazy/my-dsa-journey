"""
File: max_distinct.py
Description: This module contains a function to find the maximum sum of distinct elements in any subarray of length k.
Author: Gizachew Kassa
Date: 06/05/2025
"""

from typing import List


def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    """
    Finds the maximum sum of all contiguous subarrays of length k that contain only distinct elements.

    Uses a sliding window of size k and a frequency map to ensure each window contains k unique elements.
    The window sum is updated incrementally, and only valid windows contribute to the max sum.

    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    freq_count = {}
    current_sum = sum(nums[:k])

    for num in nums[:k]:
        freq_count[num] = freq_count.get(num, 0) + 1

    max_sum = current_sum if len(freq_count) == k else float("-inf")

    for i in range(k, len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i - k]

        freq_count[nums[i - k]] -= 1
        if freq_count[nums[i - k]] == 0:
            del freq_count[nums[i - k]]

        freq_count[nums[i]] = freq_count.get(nums[i], 0) + 1

        if len(freq_count) == k:
            max_sum = max(max_sum, current_sum)

    return max_sum if max_sum > float("-inf") else 0
