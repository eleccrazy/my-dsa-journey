"""
File: majority_element.py
Description: finds the majority element in an array
Author: Gizachew Kassa
Date: 29/04/2025
"""

from typing import List


def majorityElement(self, nums: List[int]) -> int:
    """
    Finds the majority element that appears more than n/2 times using a hash map.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    maj_count = len(nums) // 2
    hash_map = {}

    for num in nums:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1

    max_occurance = float("-inf")
    max_number = None

    for k, v in hash_map.items():
        if v > max_occurance:
            max_occurance = v
            max_number = k

    return max_number
