"""
File: longest_repeating.py
Description: This module contains a function to find the length of the longest substring
with at most two repeating characters.
Author: Gizachew Kassa
Date: 09/05/2025
"""


def characterReplacement(self, s: str, k: int) -> int:
    """
    Returns the length of the longest substring where you can replace at most `k`
    characters to make all characters in the window the same.

    Uses a variable-size sliding window and tracks the frequency of characters in the window.
    Shrinks the window when the number of replacements needed exceeds `k`.

    Time Complexity: O(n)
    Space Complexity: O(1)  # bounded by 26 uppercase English letters
    """
    left = 0
    max_freq = 0
    char_count = {}
    max_length = 0

    for right in range(len(s)):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1

        max_freq = max(max_freq, char_count[char])

        window_size = right - left + 1

        if window_size - max_freq > k:
            char_count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
