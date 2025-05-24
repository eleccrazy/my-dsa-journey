"""
File: brute_force.py
Description: This module contains a brute-force solution to compute the product of all elements in an array except for the element at the current index.
Author: Gizachew Kassa
Date: 24-05-2025
"""

from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    """
    Brute-force approach to compute the product of array except self.

    For each index, computes the product of all other elements by iterating through the array.

    Time Complexity: O(n^2) - Nested loop over the input list
    Space Complexity: O(n) - For storing the output result
    """
    n = len(nums)
    result = []

    for i in range(n):
        curr_product = 1
        for j in range(n):
            if i != j:
                curr_product *= nums[j]
        result.append(curr_product)

    return result
