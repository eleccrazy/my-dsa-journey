"""
File: two_pointers.py
Description: Check if a string is a subsequence of another string using the two-pointer technique.
Author: Gizachew Kassa
Date: 01/05/2025
"""


def isSubsequence(self, s: str, t: str) -> bool:
    """
    Determines whether string s is a subsequence of string t using the two-pointer technique.

    Time Complexity: O(n + m), where n = len(s) and m = len(t)
    Space Complexity: O(1)
    """
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
