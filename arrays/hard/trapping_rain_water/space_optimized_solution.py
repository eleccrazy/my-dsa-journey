"""
File: space_optimized_solution.py
Description: Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Author: Gizachew Kassa
Date: 30/04/2025
"""

from typing import List


def trap(self, height: List[int]) -> int:
    """
    Calculates the total trapped rain water using a two-pointer approach
    with constant space optimization.

    Time Complexity: O(n) - Each index is processed at most once.
    Space Complexity: O(1) - Uses only constant extra space.
    """
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    trapped_water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                trapped_water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                trapped_water += right_max - height[right]
            right -= 1

    return trapped_water
