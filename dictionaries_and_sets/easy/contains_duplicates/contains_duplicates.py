"""
File: contains_duplicates.py
Description: This module checks if a list contains any duplicates using a set for fast lookup.
Author: Gizachew Kassa
Date: 20-07-2025
"""

from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    """
    Checks for duplicate elements by comparing set size with list size.

    Time Complexity: O(n)
    - Creating a set from the list takes linear time.

    Space Complexity: O(n)
    - The set may contain up to n elements.
    """

    return len(set(nums)) != len(nums)


"""
Alternative implementation using a set for fast lookup:

def containsDuplicate(nums: List[int]) -> bool:

    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

"""
