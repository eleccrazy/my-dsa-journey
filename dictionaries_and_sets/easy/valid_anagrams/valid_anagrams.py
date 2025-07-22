"""
File: valid_anagrams.py
Description: This module checks if two strings are anagrams of each other using a dictionary for character counting.
Author: Gizachew Kassa
Date: 22-07-2025
"""


def isAnagram(s: str, t: str) -> bool:
    """
    Determines if two strings are anagrams by comparing character frequencies.

    Time Complexity: O(n)
    - Each character in both strings is processed once.

    Space Complexity: O(1)
    - Uses a hash map with at most 26 keys (for lowercase English letters).
    """
    if len(t) != len(s):
        return False

    freq_counter = {}

    for ch in t:
        freq_counter[ch] = freq_counter.get(ch, 0) + 1

    for ch in s:
        if freq_counter.get(ch, 0) == 0:
            return False
        freq_counter[ch] -= 1

    return True
