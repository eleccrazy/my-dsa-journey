"""
File: brute_force.py
Description: This module contains a brute force solution to the Subarray Sum Equals K problem.
Author: Gizachew Kassa
Date: 17-05-2025
"""

from typing import List


def subarraySum(self, nums: List[int], k: int) -> int:
    """
    This function finds the number of continuous subarrays whose sum equals to k.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    count = 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == k:
                count += 1

    return count
