"""
File: jewels_and_stones.py
Description: This module counts how many stones are jewels based on the given jewels string.
Author: Gizachew Kassa
Date: 20-07-2025
"""


def numJewelsInStones(jewels: str, stones: str) -> int:
    """
    Counts how many stones are jewels using a set for fast lookup.

    Time Complexity: O(n + m)
    - n = length of stones
    - m = length of jewels

    Space Complexity: O(m)
    - Space used to store jewels in a set
    """
    counter = 0
    jewels_set = set(jewels)

    for stone in stones:
        if stone in jewels_set:
            counter += 1

    return counter
