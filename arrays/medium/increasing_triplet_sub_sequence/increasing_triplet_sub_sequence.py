"""
File: increasing_triplet_sub_sequence.py
Description: This module contains a function to determine if there exists an increasing triplet subsequence in a given list.
Author: Gizachew Kassa
Date: 25-05-2025
"""

from typing import List


def increasingTriplet(self, nums: List[int]) -> bool:
    """
    Determines whether there exists an increasing subsequence of length 3
    in the input array using a greedy two-value tracking strategy.

    Time Complexity: O(n) - Single pass through the list
    Space Complexity: O(1) - Only two scalar values are tracked
    """
    first = float("inf")
    second = float("inf")

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True  # Found a third number larger than both

    return False
