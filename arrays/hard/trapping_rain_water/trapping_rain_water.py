"""
File: trapping_rain_water.py
Description: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Author: Gizachew Kassa
Date: 30/04/2025
"""

from typing import List


def trap(self, height: List[int]) -> int:
    """
    Calculates how much water can be trapped after raining using the
    precomputed left and right max walls approach.

    Time Complexity: O(n) - Two passes to compute left and right max arrays,
    and one final pass to calculate trapped water.

    Space Complexity: O(n) - Additional space used for left_max_wall and
    right_max_wall arrays.
    """
    trapped_water = 0
    n = len(height)

    left_max_wall = [0] * n
    right_max_wall = [0] * n

    left_max_wall[0] = height[0]
    right_max_wall[n - 1] = height[n - 1]

    for i in range(1, n):
        left_max_wall[i] = max(left_max_wall[i - 1], height[i])
    for i in range(n - 2, -1, -1):
        right_max_wall[i] = max(right_max_wall[i + 1], height[i])

    for i in range(1, n - 1):
        trapped_water += min(left_max_wall[i], right_max_wall[i]) - height[i]

    return trapped_water
