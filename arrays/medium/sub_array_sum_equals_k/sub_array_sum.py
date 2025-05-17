"""
File: sub_array_sum.py
Description: This module contains a solution to the Subarray Sum Equals K problem.
Author: Gizachew Kassa
Date: 14-05-2025
"""

from typing import List


def subarraySum(self, nums: List[int], k: int) -> int:
    """
    Returns the total number of continuous subarrays that sum to k.

    Uses prefix sums and a hashmap to track the number of times a given
    cumulative sum has occurred. At each step, checks if there is a
    previously seen sum such that the current_sum - previous_sum == k.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(nums)
    prefixCount = {0: 1}
    result = 0
    current_sum = 0

    for num in nums:
        current_sum += num
        diff = current_sum - k

        result += prefixCount.get(diff, 0)
        prefixCount[current_sum] = 1 + prefixCount.get(current_sum, 0)

    return result
