"""
File: remove_duplicates_sorted_array.py

Description: Removes duplicates from a sorted array in-place and returns the number of unique elements.

Author: Gizachew Kassa
Date: 26/04/2025
"""

from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
    """
    Removes duplicates from a sorted array in-place and returns the number of unique elements.

    This solution uses a two-pointer technique to overwrite duplicates without allocating extra space.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0

    idx = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[idx] = nums[i]
            idx += 1

    return idx
