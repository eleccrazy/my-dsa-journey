"""
File: rotate_array_pythonic.py
Description: Rotate an array to the right by k steps, where k is non-negative.
Author: Gizachew Kassa
Date: 04-05-2025
"""

from typing import List


def rotate(self, nums: List[int], k: int) -> None:
    """
    Rotates the array to the right by k steps using slicing.

    This method creates a new array by taking the last k elements and
    placing them before the rest. It then updates the original list in-place.

    Time Complexity: O(n)
    Space Complexity: O(n) — due to slicing and temporary array creation
    """
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
