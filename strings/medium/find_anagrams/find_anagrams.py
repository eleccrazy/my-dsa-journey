"""
File: find_anagrams.py
Description: This module contains a function to find all anagrams of a given string in a list of words.
Author: Gizachew Kassa
Date: 06/05/2025
"""

from typing import List


def findAnagrams(self, s: str, p: str) -> List[int]:
    """
    Finds all start indices of anagrams of string p in string s using a sliding window.

    Uses frequency dictionaries to track character counts in a moving window of size len(p).
    Compares the window's character count with p's count at each step.

    Time Complexity: O(n), where n is the length of s.
    Space Complexity: O(1), because the character set is fixed (lowercase English letters).
    """
    window_size = len(p)
    result = []

    if window_size > len(s):
        return result

    p_count, s_count = {}, {}

    for ch in p:
        p_count[ch] = p_count.get(ch, 0) + 1

    for ch in s[:window_size]:
        s_count[ch] = s_count.get(ch, 0) + 1

    if s_count == p_count:
        result.append(0)

    for i in range(window_size, len(s)):
        left_ch = s[i - window_size]
        s_count[left_ch] -= 1
        if s_count[left_ch] == 0:
            del s_count[left_ch]

        s_count[s[i]] = s_count.get(s[i], 0) + 1

        if s_count == p_count:
            result.append(i - window_size + 1)

    return result
