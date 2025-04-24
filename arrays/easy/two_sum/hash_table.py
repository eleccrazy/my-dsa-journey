"""
File: hash_table.py
Description: This module contains a hash table solution to the Two Sum problem.
Author: Gizachew Kassa
Date: 2025-04-25
"""

from typing import List, Optional


def two_number_sum_hash_table(array: List[int], target: int) -> Optional[List[int]]:
    """
    Returns two distinct numbers from the array that add up to the target.

    This hash table approach uses a dictionary to store the numbers.
    For each element x, it checks if (target - x) exists in the table. y = target - x.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Returns:
        A list containing the two numbers, or an empty list if no valid pair exists.
    """
    hash_table = {}

    for x in array:
        y = target - x
        if y in hash_table:
            return [x, y]
        hash_table[x] = True

    return []
