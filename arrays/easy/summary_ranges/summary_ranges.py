"""
File: summary_ranges.py
Description: This module contains a function to summarize ranges in a sorted list of integers.
Author: Gizachew Kassa
Date: 12-06-2025
"""

from typing import List


def summaryRanges(self, nums: List[int]) -> List[str]:
    """
    Returns the smallest sorted list of ranges covering all numbers in the input array.
    A range is represented as "a->b" if a != b, or just "a" if a == b.

    Time Complexity: O(n)
    - Single pass through the array

    Space Complexity: O(1) extra (excluding result list)
    """
    result = []
    n = len(nums)
    if n > 0:
        start = nums[0]

    for i in range(n):
        if i < n - 1:
            if nums[i + 1] - 1 != nums[i]:
                if start == nums[i]:
                    result.append(f"{start}")
                else:
                    result.append(f"{start}->{nums[i]}")
                start = nums[i + 1]
        else:
            if nums[i] - 1 == nums[i - 1]:
                result.append(f"{start}->{nums[i]}")
            else:
                result.append(f"{nums[i]}")

    return result
