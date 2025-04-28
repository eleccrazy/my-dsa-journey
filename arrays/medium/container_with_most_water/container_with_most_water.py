"""
File: container_with_most_water.py
Description: Container with Most Water
Author: Gizachew Kassa
Date: 29/04/2025
"""

from typing import List


def maxArea(self, height: List[int]) -> int:
    """
    Finds the maximum area of water a container can store using two pointers.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    max_area = float("-inf")
    n = len(height)
    left = 0
    right = n - 1

    while left < right:
        height_chosen = min(height[left], height[right])
        width = right - left
        max_area = max(max_area, width * height_chosen)
        if height[left] == height_chosen:
            left += 1
        else:
            right -= 1

    return max_area
