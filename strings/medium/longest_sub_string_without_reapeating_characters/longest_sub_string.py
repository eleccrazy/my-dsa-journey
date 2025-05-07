"""
File: longest_sub_string.py
Description: This module contains a function to find the length of the longest substring
without repeating characters.
Author: Gizachew Kassa
Date: 07/05/2025
"""


def lengthOfLongestSubstring(self, s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.

    Uses a sliding window approach with a set to track unique characters in the current window.
    Expands the window by moving the right pointer, and shrinks it from the left when duplicates are found.

    Time Complexity: O(n)
    Space Complexity: O(k), where k is the number of unique characters in the string
    """
    left, right = 0, 0

    character_set = set()
    max_length = 0

    while right < len(s) and left <= right:
        if s[right] not in character_set:
            character_set.add(s[right])
            right += 1
        else:
            character_set.remove(s[left])
            left += 1
        max_length = max(max_length, right - left)

    return max_length
