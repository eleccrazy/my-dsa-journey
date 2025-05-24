"""
File: number_of_zero_filled.py
Description: This module contains a function to count the number of zero-filled subarrays in a given list.
Author: Gizachew Kassa
Date: 25-05-2025
"""

from typing import List


def zeroFilledSubarray(self, nums: List[int]) -> int:
    """
    Counts the number of contiguous subarrays filled with 0 using a running counter.

    Each time a 0 is encountered, it contributes 1 new subarray plus
    additional ones formed with previously seen consecutive zeros.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    occurence, count_times = 0, 0

    for num in nums:
        if num == 0:
            occurence += 1 + count_times
            count_times += 1
        else:
            count_times = 0

    return occurence
