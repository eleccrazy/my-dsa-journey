"""
File: search_and_insert.py
Description: This module implements a binary search algorithm to find the index of a target value
or the position where it should be inserted in a sorted list.
Author: Gizachew Kassa
Date: 04-07-2025
"""

from typing import List


def searchInsert(self, nums: List[int], target: int) -> int:
    """
    Performs binary search to find the index of the target value,
    or the position where it should be inserted in sorted order.

    Time Complexity: O(log n)
    - Standard binary search reduces the search space by half.

    Space Complexity: O(1)
    - Only constant extra space is used for pointers.

    Args:
        nums (List[int]): Sorted list of distinct integers.
        target (int): The value to search or insert.

    Returns:
        int: Index of the target if found, or insert position.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return left
