"""
File: three_sum.py
Description: This file contains a function to find all unique triplets in an array that sum up to zero.
Author: Gizachew Kassa
Date: 28/04/2025
"""

from typing import List


def threeSum(self, nums: List[int]) -> List[List[int]]:
    """
    Finds all unique triplets in the array which sum to zero.

    Time Complexity: O(n²)
    Space Complexity: O(1) (ignoring output list)

    """
    result = []
    n = len(nums)

    nums.sort()

    for start in range(n - 2):
        if start != 0 and nums[start - 1] == nums[start]:
            continue
        left, right = start + 1, n - 1
        while left < right:
            current_sum = nums[start] + nums[left] + nums[right]
            if current_sum == 0:
                result.append([nums[start], nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result
