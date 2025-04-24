"""
File: brute_force.py
Description: This module contains a brute force solution to the Two Sum problem.
Author: Gizachew Kassa
Date: 2025-04-25
"""

from typing import List, Optional


def two_number_sum_bruteforce(array: List, target: int) -> Optional[List[int]]:
    """
    Returns two distinct numbers from the array that add up to the target.

    This brute force approach checks all pairs in a nested loop.

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Returns:
        A list containing the two numbers, or an empty list if no valid pair exists.
    """
    n = len(array)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if array[i] + array[j] == target:
                return [array[i], array[j]]
    return []
