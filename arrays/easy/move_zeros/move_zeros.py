"""
File: move_zeros.py
Description: Move all zeros to the end of the array while maintaining the order of non-zero elements.
Author: Gizachew Kassa
Date: 29/04/2025
"""

from typing import List


def moveZeroes(self, nums: List[int]) -> None:
    """
    Moves all zeros to the end of the array while maintaining the relative order of non-zero elements.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)
    if n < 2:
        return
    left = 0
    right = 1

    while right < n:
        if nums[left] == 0:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
            else:
                right += 1
                continue
        left += 1
        right += 1
