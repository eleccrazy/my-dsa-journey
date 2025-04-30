"""
File: is_subsequence.py
Description: Check if a string is a subsequence of another string.
Author: Gizachew Kassa
Date: 01/05/2025
"""


def isSubsequence(self, s: str, t: str) -> bool:
    """
    Determines whether string s is a subsequence of string t by scanning t
    linearly for each character in s.

    Time Complexity: O(n * m) in the worst case,
    where n = len(s) and m = len(t).

    Space Complexity: O(1) - constant extra space is used.
    """
    start = 0
    for ch in s:
        checked = False
        for i in range(start, len(t)):
            if ch == t[i]:
                checked = True
                start = i + 1
                break
        if not checked:
            return False
    return True
