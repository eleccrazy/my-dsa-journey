"""
File: permutation_in_string.py
Description: This module contains a function to check if one string is a permutation of another string.
Author: Gizachew Kassa
Date: 06/05/2025
"""


def checkInclusion(self, s1: str, s2: str) -> bool:
    """
    Returns True if s2 contains any permutation of s1 as a substring.

    Uses a sliding window of length len(s1) and maintains character frequency
    maps for both s1 and the current window in s2. Updates the map incrementally
    and compares for matches.

    Time Complexity: O(n), where n = len(s2)
    Space Complexity: O(1), due to a fixed alphabet of lowercase letters
    """
    s1_count, s2_count = {}, {}

    if len(s1) > len(s2):
        return False

    window_size = len(s1)

    for ch in s1:
        s1_count[ch] = s1_count.get(ch, 0) + 1

    for ch in s2[:window_size]:
        s2_count[ch] = s2_count.get(ch, 0) + 1

    if s1_count == s2_count:
        return True

    for i in range(window_size, len(s2)):
        s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        s2_count[s2[i - window_size]] -= 1
        if s2_count[s2[i - window_size]] == 0:
            del s2_count[s2[i - window_size]]

        if s1_count == s2_count:
            return True

    return False
