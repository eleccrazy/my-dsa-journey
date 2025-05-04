"""
File: rotate_array_space_optimized.py
Description: Rotate an array to the right by k steps, where k is non-negative.
Author: Gizachew Kassa
Date: 04-05-2025
"""

from typing import List


def rotate(self, nums: List[int], k: int) -> None:
    """
    Rotates the array to the right by k steps in-place using the reverse method.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def reverse(left: int, right: int) -> None:
        """
        Helper function to reverse the elements in the array from left to right.
        """
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    k = k % len(nums)
    reverse(0, len(nums) - 1)  # Reverse entire array
    reverse(0, k - 1)  # Reverse first k elements
    reverse(k, len(nums) - 1)  # Reverse the rest of the array
