"""
File: space_optimized_solution.py
Description: This module contains a space-optimized solution to compute the product of all elements in an array except for the element at the current index.
Author: Gizachew Kassa
Date: 24-05-2025
"""

from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    """
    Computes product of array except self using O(1) extra space (excluding output array).

    First pass stores prefix products in result.
    Second pass multiplies with postfix products in-place.

    Time Complexity: O(n)
    Space Complexity: O(1) extra (excluding result array)
    """
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result
