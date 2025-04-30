"""
File: longest_common_prefix.py
Description: This module contains a function to find the longest common prefix
Author: Gizachew Kassa
Date: 01/05/2025
"""

from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
    """
    Finds the longest common prefix string among a list of strings.

    Iterates character by character up to the shortest string length,
    and checks if all strings have the same character at each position.

    Time Complexity: O(n * m), where n is the number of strings and
    m is the length of the shortest string.

    Space Complexity: O(1) - only uses constant extra space.
    """
    min_length = min(len(string) for string in strs)

    long_prefix = ""

    for i in range(min_length):
        current_char = strs[0][i]
        if all(s[i] == current_char for s in strs):
            long_prefix += current_char
        else:
            break

    return long_prefix
