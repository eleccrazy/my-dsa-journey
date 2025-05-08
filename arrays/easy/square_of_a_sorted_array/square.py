"""
File: square.py
Description: This module contains a function to return the square of each number in a sorted array.
Author: Gizachew Kassa
Date: 08/05/2025
"""


def sortedSquares(nums: list[int]) -> list[int]:
    """
    Returns a new array containing the squares of each number from the input array, sorted in non-decreasing order.

    Uses a two-pointer approach to efficiently square and sort the numbers.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(nums)
    left, right = 0, n - 1
    result = [0] * n

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1

    return result
