"""
File: sub_array_sums_divisible_by_k.py
Description: This module contains a solution to the Subarray Sums Divisible by K problem.
Author: Gizachew Kassa
Date: 17-05-2025
"""

from typing import List


def subarraysDivByK(self, nums: List[int], k: int) -> int:
    """
    Returns the count of non-empty subarrays whose sum is divisible by k.

    Uses prefix sum and a hashmap to store the frequency of each modulo value.
    If two prefix sums have the same mod value, their difference is divisible by k.

    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    prefix_sum = {0: 1}
    result = 0
    current_sum = 0

    for num in nums:
        current_sum += num
        remainder = (current_sum % k + k) % k
        result += prefix_sum.get(remainder, 0)
        prefix_sum[remainder] = 1 + prefix_sum.get(remainder, 0)

    return result
