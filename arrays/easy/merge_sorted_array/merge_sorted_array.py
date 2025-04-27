"""
File: merge_sorted_array.py
Description: Merges two sorted integer arrays into a single sorted array.
Author: Gizachew Kassa
Date: 27/04/2025
"""

from typing import List


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merges two sorted arrays in-place so that nums1 contains the sorted merged result.

    This approach appends elements from nums2 into nums1 and sorts the array.

    Time Complexity: O((m + n) log(m + n))
    Space Complexity: O(1)
    """
    for i in range(n):
        nums1[m] = nums2[i]
        m += 1
    nums1.sort()
