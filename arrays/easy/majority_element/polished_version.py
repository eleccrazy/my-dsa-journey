"""
File: polished_version.py
Description: finds the majority element in an array
Author: Gizachew Kassa
Date: 29/04/2025
"""
from typing import List


def majorityElement(self, nums: List[int]) -> int:
    """
    Finds the majority element by counting frequencies and returning immediately once the majority is found.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    maj = len(nums) // 2
    freq_hash = {}

    for num in nums:
        freq_hash[num] = freq_hash.get(num, 0) + 1
        if freq_hash[num] > maj:
            return num
