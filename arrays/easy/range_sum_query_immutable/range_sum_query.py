"""
File: range_sum_query.py
Description: This module contains a solution to the Range Sum Query Immutable problem.
Author: Gizachew Kassa
Date: 13-05-2025
"""

from typing import List


class NumArray:
    """
    A class that supports efficient range sum queries using prefix sums.

    Preprocesses the input array to compute cumulative sums. Each call to sumRange
    returns the sum of the subarray nums[left:right+1] in O(1) time.

    Time Complexity:
        - __init__: O(n)
        - sumRange: O(1)

    Space Complexity: O(1) (modifies input list in-place)
    """

    def __init__(self, nums: List[int]):
        # Precompute prefix sums in-place
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        self.prefixSum = nums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        return self.prefixSum[right] - self.prefixSum[left - 1]
