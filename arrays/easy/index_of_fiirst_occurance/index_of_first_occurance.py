"""
File: index_of_first_occurance.py
Description: This file contains a function to find the index of the first occurrence of a target value in a sorted array.
Author: Gizachew Kassa
Date: 28/04/2025
"""


def strStr(self, haystack: str, needle: str) -> int:
    """
    Finds the index of the first occurrence of needle in haystack using a two-pointer sliding window.

    Time Complexity: O((n - m + 1) * m)
    Space Complexity: O(1)
    """
    n, m = len(haystack), len(needle)
    if n < m:
        return -1
    left = 0
    while left <= n - m:
        end = left + m
        if haystack[left:end] == needle:
            return left
        left += 1
    return -1
