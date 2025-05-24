"""
File: product_of_array_except_itself.py
Author: Gizachew Kassa
Date: 24-05-2025
"""

from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    """
    Computes the product of array elements except self using prefix and postfix arrays.

    For each index, the result is the product of all elements before it (prefix)
    and after it (postfix), excluding the current index.

    Time Complexity: O(n) - Three linear passes through the array
    Space Complexity: O(n) - Additional arrays for prefix, postfix, and result
    """
    n = len(nums)
    result = [0] * n
    prefix = [0] * n
    postfix = [0] * n

    prefix[0] = nums[0]
    postfix[n - 1] = nums[n - 1]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i]

    for i in range(n - 2, -1, -1):
        postfix[i] = postfix[i + 1] * nums[i]

    for i in range(n):
        if i == 0:
            result[i] = postfix[1]
        elif i == n - 1:
            result[i] = prefix[n - 2]
        else:
            result[i] = prefix[i - 1] * postfix[i + 1]

    return result
