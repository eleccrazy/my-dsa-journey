"""
File: max_consecutive.py
Description: This module contains a function to find the maximum number of consecutive 1's in a binary array.
Author: Gizachew Kassa
Date: 12-05-2025
"""

from typing import List


def longestOnes(self, nums: List[int], k: int) -> int:
    """
    Returns the maximum number of consecutive 1s in the array if at most k 0s can be flipped.

    Uses a sliding window approach where the window expands until the number of 0s
    exceeds k. Tracks the number of 1s to determine when the window becomes invalid.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    one_count = 0
    max_cons = 0

    for right in range(len(nums)):
        if nums[right] == 1:
            one_count += 1

        # If more than k zeros in window, shrink from the left
        if (right - left + 1) - one_count > k:
            if nums[left] == 1:
                one_count -= 1
            left += 1

        max_cons = max(max_cons, right - left + 1)

    return max_cons
