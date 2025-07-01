"""
File: binary_search.py
Description: This module implements a binary search algorithm.
Author: Gizachew Kassa
Date: 30-06-2025
"""

from typing import List


def search(self, nums: List[int], target: int) -> int:
    """
    Performs binary search on a sorted list to find the index of the target value.

    Time Complexity: O(log n)
    - The search space is halved in every iteration.

    Space Complexity: O(1)
    - No extra space is used beyond a few pointers.

    Returns:
        int: Index of the target if found, otherwise -1.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
